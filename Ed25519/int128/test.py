import random
import subprocess
import os

def gen_random_int128():
    """
    隨機產生一個 128-bit 有號整數 (二補數範圍: [-2^127, 2^127-1])
    """
    # 先產生 128-bit 無號
    val = random.getrandbits(128)
    # 隨機考慮把最高 bit 當 sign
    # 這裡簡單: 50%機率 => 讓 val(最高bit=1 => 負數)
    # 也可改更精準: if random.choice([True,False]): val |= (1<<127)
    # 讓 val 變成 [0,2^128-1], 最高bit=1 代表「負數」(二補數)
    # 這裡直接 random, 看起來 50%負, 50%正
    if random.choice([True,False]):
        val |= (1<<127)

    # 以二補數解讀
    if val & (1<<127):  # sign bit=1 => 負
        val = val - (1<<128)
    return val


def format_256_hex_grouped(value: int) -> str:
    """
    將 256-bit 二補數 (Python int) 以 64 hex digits 顯示，
    並且每 16 字元用 '_' 分隔。
    """
    # 1) 取 mod 2^256 (無號)
    mask_256 = (1 << 256) - 1
    uval = value & mask_256

    # 2) 轉成 64 hex digits (不含 '0x')
    hex_str = f"{uval:064x}"

    # 3) 每 16 字元切一段 => 用 '_'
    chunks = [hex_str[i:i+16] for i in range(0, 64, 16)]
    grouped = "_".join(chunks)

    return f"0x{grouped}"

def format_128_hex_grouped(value: int) -> str:
    """
    將 128-bit 二補數 (Python int) 以 64 hex digits 顯示，
    並且每 16 字元用 '_' 分隔。
    """
    # 1) 取 mod 2^128 (無號)
    mask_128 = (1 << 128) - 1
    uval = value & mask_128

    # 2) 轉成 64 hex digits (不含 '0x')
    hex_str = f"{uval:032x}"

    # 3) 每 16 字元切一段 => 用 '_'
    chunks = [hex_str[i:i+16] for i in range(0, 32, 16)]
    grouped = "_".join(chunks)

    return f"0x{grouped}"

def split_int128_to_64(v):
    """
    將一個 Python int (範圍在 [-2^127, 2^127-1])，拆成 (lo, hi) 各 64 bit, (二補數).
    """
    # 先做 mod 2^128
    mask128 = (1 << 128) - 1
    v_mod = v & mask128
    lo = v_mod & ((1<<64) - 1)       # 低64
    hi = (v_mod >> 64) & ((1<<64)-1) # 高64
    return (lo, hi)

def unify_64_to_int128(lo, hi):
    """
    反向: 兩個 64-bit limb => Python int(128bit二補數).
    lo=uint64, hi=uint64. 最高bit=1 => 負數 => val - 2^128
    """
    val_128 = (hi << 64) | lo
    # 看 bit127
    if (hi >> 63) & 1 == 1:
        # 表示負數
        val_128 -= (1<<128)
    return val_128


def generate_c_program(A, B, mode = "sch"):
    """
    傳進 128-bit 有號的 A,B。
    拆 limb => A_lo,A_hi, B_lo,B_hi。
    產生一個 C 程式檔案(檔名= test_generated.c)，宣告這些常數、
    呼叫你的 int128_mul(...) 函式、把結果印出來。
    mode = "kar" -> karatsuba
    mode = "sch" -> schoolbook
    """

    assert(mode in {"kar", "sch"})

    if mode == "kar":
        mode = ""
    if mode == "sch":
        mode = "_sch"


    A_lo, A_hi = split_int128_to_64(A)
    B_lo, B_hi = split_int128_to_64(B)

    # 產生 C 程式
    code = f"""
#include <stdio.h>
#include <stdint.h>


typedef struct {{
    // v[0] 是最低 64 bits, v[1] 是最高 64 bits (共 128 bits)
    uint64_t v[2];
}} int128_t;

typedef struct {{
    // v[0] 是最低 64 bits, v[3] 是最高 64 bits (共 256 bits)
    uint64_t v[4];
}} int256_t;

extern void int128_mul(int128_t *A, int128_t *B, int256_t *R);
extern void int128_mul_sch(int128_t *A, int128_t *B, int256_t *R);


int main() {{
    // 1) 先宣告 A, B (from python)


    int128_t A = {{ 0x{A_lo:016x}, 0x{A_hi:016x} }};
    int128_t B = {{ 0x{B_lo:016x}, 0x{B_hi:016x} }};
    int256_t R = {{ 0 }};

    // 2) call int128_mul
    int128_mul{mode}(&A, &B, &R);
    
    // 3) print results

    uint64_t r0 = R.v[0];
    uint64_t r1 = R.v[1];
    uint64_t r2 = R.v[2];
    uint64_t r3 = R.v[3];

    // print results
    // print r0, r1, r2, r3 in hex
    // Python 端再 parse
    printf("%016llx\\n%016llx\\n%016llx\\n%016llx\\n", 
        (unsigned long long)r0,
        (unsigned long long)r1,
        (unsigned long long)r2,
        (unsigned long long)r3
    );

    return 0;
}}
"""
    return code


def main():

    for _ in range(100):
        mode = random.choice(["kar","sch"])

        A = gen_random_int128()
        B = gen_random_int128()



        # 產生 C 程式
        code = generate_c_program(A, B,mode)

        # 寫到 test_generated.c
        with open("test_generated.c", "w") as f:
            f.write(code)
        print("Generated test_generated.c for A,B")

        # 編譯
        cmd_compile = ["gcc", "test_generated.c", "-o", "test_generated"]
        # 如果你要 link 你的 int128.S, 可做:
        cmd_compile = ["gcc", "test_generated.c", "int128_mul.S", "int128_mul_sch.S", "-o", "test_generated"]

        subprocess.run(cmd_compile, check=True)

        # 執行
        cmd_run = ["./test_generated"]
        result = subprocess.run(cmd_run, capture_output=True, check=True, text=True)

        # result.stdout 會是剛才程式印出的
        lines = result.stdout.strip().split("\n")
        if len(lines) < 4:
            print("Output lines < 4 ???", lines)
            return

        r0_hex = lines[0]
        r1_hex = lines[1]
        r2_hex = lines[2]
        r3_hex = lines[3]

        # parse hex => uint64
        r0 = int(r0_hex, 16)
        r1 = int(r1_hex, 16)
        r2 = int(r2_hex, 16)
        r3 = int(r3_hex, 16)

        # unify => 256 bits
        # 256 bits => r3<<192, r2<<128, r1<<64, r0
        # 這裡再將 256 bits 轉成 python int(可能要2^256)
        # 先 unify
        val_256 = (r3 << 192) | (r2 << 128) | (r1 << 64) | r0

        

        # 看最高 bit (bit 255)? => if 1 => negative => val_256 - 2^256
        if (r3 >> 63) & 1 == 1:
            val_256 -= (1<<256)

        # 用 python 大整數算
        correct_result = A * B


        
        # 比對
        if correct_result == val_256:
            print(f"Test {_+1} OK.  result match. Using {mode}")
        else:
            print(f"Test FAIL")


            A_str = format_128_hex_grouped(A)
            B_str = format_128_hex_grouped(B)
            asm_str = format_256_hex_grouped(val_256)
            py_str  = format_256_hex_grouped(correct_result)

            print("The operands are: ")
            print(f"A hex (grouped) = {A_str}")
            print(f"B hex (grouped) = {B_str}")
            print("The results are: ")
            print(f"ASM hex (grouped) = {asm_str}")
            print(f"PY  hex (grouped) = {py_str}")

            difference = val_256 - correct_result
            diff_str = format_256_hex_grouped(difference)
            print(f"difference hex (grouped) = {diff_str}")
            break




if __name__ == "__main__":
    main()
