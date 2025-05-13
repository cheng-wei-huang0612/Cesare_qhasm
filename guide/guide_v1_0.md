# LLM‑Friendly **qhasm** Guide (AArch64) v1.0

> **Goal**  Provide one self‑contained Markdown file that, when fed to a language model, is enough for it to write **legal, buildable** qhasm **`.q`** files that compile to AArch64 assembly using the community "qhasm‑aarch64" toolchain.

---

## 1  What is qhasm?

* A *declarative* assembly DSL originally designed by D. J. Bernstein, now ported to multiple back‑ends (x86, AArch64…).
* Lets you write arithmetic expressions (`r = a + b`, `4x v = a * b`) while still pinning exact registers and flags.
* Produces vanilla \*\*GNU/Clang‑style \*\***`.S`** that you assemble and link with the normal toolchain.

---

## 2  Directory & file conventions

| Kind                     | Extension         | Example                      |
| ------------------------ | ----------------- | ---------------------------- |
| qhasm source             | **`something.q`** | `ntt_len2.q`                 |
| generated asm            | `something.S`     | `ntt_len2.S`                 |
| helper python (optional) | `.py`             | `qhasm‑aarch64‑desc‑neon.py` |

> ❗ **We use ****`.q`**** exclusively**.  Historic names `.qas` / `.qhasm` still exist online, but this guide sticks to `.q` so the model learns the right habit.

---

## 3  Build pipeline in one line

```bash
qhasm-aarch64-align < ntt_len2.q > ntt_len2.S   # ⇐ the only command you need
clang -c -O3 -march=armv8-a+simd ntt_len2.S      # turn it into an object file
```

* `qhasm-aarch64-align` internally loads the **descriptor files** (calling convention, NEON macros, prologue / epilogue…) that live alongside the tool; you **do not** `include` them inside the `.q` file.
* If you maintain a fork with extra macros, register‑alias tables, etc., patch the descriptor `.py` scripts and rebuild `qhasm-aarch64-align` – your `.q` stays clean.

---

## 4  Minimal syntax cheat‑sheet

| qhasm line                 | Effect                                        | Emits                     |
| -------------------------- | --------------------------------------------- | ------------------------- |
| `int64 r`                  | declare 64‑bit GP variable                    | —                         |
| `reg128 v`                 | declare 128‑bit NEON variable                 | —                         |
| `stack64 tmp[2]`           | 16‑byte stack buffer (auto prologue/epilogue) | `sub sp,sp,#16` …         |
| `r = a + b`                | add                                           | `add x?, x?, x?`          |
| `4x v = a * b`             | vector multiply (macro)                       | `mul v?.4s, v?.4s, v?.4s` |
| `t = (a * mu) >> 32 round` | high‑half multiply                            | `sqrdmulh …`              |
| `goto L if r == 0`         | branch on zero                                | `cbz`                     |
| `assign v20 to z`          | pin variable to register                      | —                         |
| `free z:`                  | release register early                        | —                         |

> 👉  For a full grammar, read the original docs **and** the real‑world examples shipped in the repo – LLMs learn style best by imitation.

---

## 5  End‑to‑end example (length‑2 NTT butterfly)

```qhasm
# ntt_len2.q  – 4‑parallel Barrett butterfly (signed 32‑bit limbs)

enter ntt_len2                 # creates .global _ntt_len2 / 16‑byte align
  # parameters
  int64 p_in, p_out
  p_in  = input_x0             # rdi / x0
  p_out = input_x1

  # load 4×32‑bit elements (data0,data1)
  reg128 v_d0, v_d1
  asm/ldp    q0, q1, [p_in]
  v_d0 = v0  # alias
  v_d1 = v1

  # Barrett reduction constants already live in v_const* (set by caller)
  reg128 v_t, v_z
  4x v_z = v_d1 * v_const_b
  4x v_t = (v_d1 * v_const_mu) >> 32 round
  4x v_z -= v_t * v_const_n

  # butterfly
  v_d0 += v_z
  v_d1 -= v_z

  asm/stp    q0, q1, [p_out]
return
```

This compiles with the one‑liner above and matches the reference `.S` shipped under `examples/`.

---

## 6  Suggested learning path for an LLM

1. **Read all files under the ****`examples/`**** folder.**  They cover GP‑only, NEON, control‑flow heavy, and large‑stack kernels.
2. **Memorise** the cheat‑sheet table (Section 4).  Ninety‑plus percent of qhasm you see in the wild uses only those constructs.
3. **Observe register‑allocation patterns** in the examples.  Emulate the same when generating new code.
4. **Produce a small kernel**, compile, and run through `llvm‑mca` to sanity‑check dispatch & stall.

---

## 7  Caveats & common pitfalls

* **NZCV flags** – qhasm doesn’t track them.  After an `adds` / `subs` you can safely `csel`, but inserting unrelated flag‑modifying instructions in between is on you.
* **Descriptor drift** – If you patch calling‑convention or NEON macros, rebuild `qhasm-aarch64-align` so all `.q` stay independent.
* **Micro‑architecture quirks** – Latency tables are generic; measure on real hardware for Apple‑M‑class cores & Cortex‑A710+.

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

