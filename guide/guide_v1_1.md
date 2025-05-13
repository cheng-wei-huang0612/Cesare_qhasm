# LLM‑Friendly **qhasm** Guide (AArch64) v1.2

> **Goal**  Provide one self‑contained Markdown file that, when fed to a language model, is enough for it to write **legal, buildable** qhasm **`.q`** files that compile to AArch64 assembly using the community `qhasm‑aarch64` toolchain.

---

## 1  What is qhasm?

* A *declarative* assembly DSL originally designed by D. J. Bernstein, now ported to multiple back‑ends (x86, AArch64…).
* Lets you describe arithmetic at a high level (`r = a + b`, `4x v = a * b`) while still pinning exact registers and flags.
* Emits plain **GNU/Clang‑style `.S`** files that assemble & link with the normal toolchain.

---

## 2  Directory & file conventions

| Kind                     | Extension         | Example                      |
| ------------------------ | ----------------- | ---------------------------- |
| qhasm source             | **`something.q`** | `ntt_len2.q`                 |
| generated asm            | `something.S`     | `ntt_len2.S`                 |
| helper python (optional) | `.py`             | `qhasm‑aarch64‑desc‑neon.py` |

> ❗ **We use `.q` exclusively.**  Historic names `.qas` / `.qhasm` exist online, but this guide sticks to `.q` so models learn the right habit.

---

## 3  Build pipeline in one line

```bash
qhasm-aarch64-align < foo.q > foo.S         # ⇐ translate to asm
clang -c -O3 -march=armv8-a+simd foo.S      # assemble into object file
```

* `qhasm-aarch64-align` implicitly loads the **descriptor files** (calling convention, NEON macros, prologue/epilogue…).  **Do not** `include` them inside the `.q` file.
* If you extend macros or register aliases, patch the descriptor `.py` scripts and rebuild `qhasm-aarch64-align`; your `.q` stays unchanged.

---

## 4  Minimal syntax cheat‑sheet

| qhasm line                 | Effect                                            | Emits          |
| -------------------------- | ------------------------------------------------- | -------------- |
| `int64 r`                  | declare 64‑bit GP variable *(one per line!)*      | —              |
| `reg128 v`                 | declare 128‑bit NEON variable *(one per line!)*   | —              |
| `stack64 tmp[2]`           | 16‑byte stack buffer (auto prologue/epilogue)     | `sub` / `add`  |
| `r = a + b`                | add                                               | `add x?,x?,x?` |
| `4x v = a * b`             | vector multiply (macro)                           | `mul v?.4s,…`  |
| `t = (a * mu) >> 32 round` | high‑half multiply                                | `sqrdmulh …`   |
| `goto L if r == 0`         | branch on zero                                    | `cbz`          |
| `assign v20 to z`          | pin variable to register                          | —              |
| `free z:`                  | release register early                            | —              |
| **`output_x0 = <expr>`**   | set return value (must be done *before* `return`) | —              |
| `return`                   | finish function (`ret`)                           | `ret`          |

> 📝 **Declaration rule**: each `int64` / `reg128` / `stack…` must appear on its **own line**.  Comma‑separated lists are illegal.
>
> 📝 **Return rule**: `return` never carries a value.  Assign to `output_x0` / `output_x1` first, then issue a bare `return`.

---


## 5  Coding styles — Clarity vs Optimised
### 5.1 Teaching / Code‑review (clarity first) Use explicit variable declarations so newcomers can trace each value.

```qhasm
int64 a
int64 b

input a
input b

a = a + b            # one extra move but crystal‑clear
output_x0 = a        # return value
return
```


### 5.2 Hot loop / Micro‑benchmark (optimised) Operate directly on ABI aliases to avoid any superfluous moves:

```qhasm
enter add_two

output_x0 = input_x0 + input_x1   # single‑insn add x0,x0,x1
return
```


The shorthand is legal in modern qhasm‑aarch64.  Use it whenever the goal is lowest latency / smallest code.


---

## 6  Detailed Examples

### Example 1 – 4‑parallel length‑2 butterfly

```qhasm
# extern void ct_4par_len2(
#     int32_t *N,           # 4 moduli (lane‑wise)
#     int32_t *in,          # 4 pairs of length‑2 arrays processed independently
#     int32_t *omegas,      # 4 twiddle factors (b)
#     int32_t *mu_omegas    # 4 Barrett multipliers matching each twiddle factor
# )

int64 pointer_N
int64 pointer_in
int64 pointer_omegas
int64 pointer_mu_omegas

input pointer_N
input pointer_in
input pointer_omegas
input pointer_mu_omegas

reg128 data0
reg128 data1
reg128 n_vec
reg128 b_vec
reg128 mu_vec

reg128 z
reg128 t
reg128 sumv
reg128 diffv

enter ntt_4par_len2

# 1) load moduli   N[0..3]
n_vec  = mem128[pointer_N+0]        # lane‑wise N

# 2) load input    in[0..7]
data0  = mem128[pointer_in+0]       # in[0..3]
data1  = mem128[pointer_in+16]      # in[4..7]

# 3) load twiddle factors (b)
b_vec  = mem128[pointer_omegas+0]

# 4) load Barrett multipliers (mu_b)
mu_vec = mem128[pointer_mu_omegas+0]

# Barrett multiplication (3 instructions):
#   z = data1 * b_vec
#   t = (data1 * mu_vec) >> 31  (rounded high part)
#   z = z ‑ t * n_vec

4x z  = data1 * b_vec                       # mul
4x t  = (data1 * mu_vec) >> 31 round        # sqrdmulh
4x z -= t * n_vec                           # mls

# Radix‑2 butterfly
4x sumv  = data0 + z
4x diffv = data0 - z

# Store results back
mem128[pointer_in+0]  = sumv
mem128[pointer_in+16] = diffv

return
```

---

## 7  Caveats & Common Pitfalls

| Pitfall                                          | Why it bites                                   | Quick fix                                                                                |
| ------------------------------------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Comma‑separated declarations**<br>`int64 a, b` | Illegal syntax → align fails                   | Declare **one symbol per line** (`int64 a` / `int64 b`).                                 |
| **`return r`**                                   | `return` ignores arguments → result is garbage | Assign result explicitly:<br>`output_x0 = r` then a bare `return`.                       |
| **NZCV flag clobber**                            | qhasm doesn’t track flags                      | Keep `adds/subs` and the following `csel` adjacent; avoid extra instructions in between. |
| **Descriptor drift**                             | Changing macros without rebuilding tool        | Re‑run descriptor scripts after any change; regenerate the align binary.                 |
| **µ‑arch latency surprises**                     | Generic tables ≠ real hardware                 | Benchmark on target SoC; adjust scheduling if needed.                                    |

---

## 8  Useful CLI snippets

```bash
# diff generated asm with a golden reference
diff -u ntt_len2_golden.S <(qhasm-aarch64-align < ntt_len2.q)

# throughput estimate on Neoverse‑N2
llvm-mca -march=armv8-a+simd -mcpu=neoverse-n2 ntt_len2.S
```

---

### Happy hacking!  Feed this file to your model, then point it at the `examples/` directory and let it imitate the style.

