import random
import subprocess
import os

def gen_random_int128():
    val = random.getrandbits(128)
    return val


def split_uint128_to_64(v):
    """
    Splits a 128-bit unsigned integer into two 64-bit unsigned integers.

    Args:
        v (int): A 128-bit unsigned integer.

    Returns:
        tuple: A tuple containing two 64-bit unsigned integers (v0, v1), where
               v0 is the lower 64 bits and v1 is the upper 64 bits of the input integer.
    """
    v1 = v >> 64
    v0 = v - ((v1) << 64)
    return (v0, v1)


def split_uint256_to_64(v):
    """
    Splits a 256-bit integer into four 64-bit integers.

    This function takes a 256-bit integer `v` and splits it into four 64-bit integers.
    It does so by repeatedly shifting the input integer to the right by 64 bits and
    masking out the lower 64 bits.

    Args:
        v (int): A 256-bit unsigned integer to be split.

    Returns:
        tuple: A tuple containing four 64-bit integers (v0, v1, v2, v3), where:
            - v0 is the least significant 64 bits of the input integer.
            - v1 is the next 64 bits.
            - v2 is the next 64 bits.
            - v3 is the most significant 64 bits.
    """
    v0 = v - ((v >> 64) << 64)
    v = v >> 64

    v1 = v - ((v >> 64) << 64)
    v = v >> 64

    v2 = v - ((v >> 64) << 64)
    v = v >> 64

    v3 = v - ((v >> 64) << 64)
    v = v >> 64
    return (v0, v1, v2, v3)






def format_128_hex_grouped(value: int) -> str:
    """
    Return the hex string of the given value, little endian.
    """
    v0, v1 = split_uint128_to_64(value)
    r_str = f"{v1:016x}_{v0:016x}"
    return r_str

def format_256_hex_grouped(value: int) -> str:
    """
    Return the hex string of the given value, little endian.
    """
    v0, v1, v2, v3 = split_uint256_to_64(value)
    r_str = f"{v3:016x}_{v2:016x}_{v1:016x}_{v0:016x}"
    return r_str



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


def unify_limbs_to_uint256(v0,v1,v2,v3):
    """
    Combines four 64-bit unsigned integers into a 256-bit unsigned integer.

    Args:
        v0, v1, v2, v3 (int): Four 64-bit unsigned integers.

    Returns:
        int: A 256-bit unsigned integer.
    """
    val_256 = (v3 << 192) | (v2 << 128) | (v1 << 64) | v0
    return val_256



def generate_c_program(A, B):
    """
    傳進 128-bit 有號的 A,B。
    拆 limb => A_lo,A_hi, B_lo,B_hi。
    產生一個 C 程式檔案(檔名= test_generated.c)，宣告這些常數、
    呼叫你的 int128_mul(...) 函式、把結果印出來。
    mode = "kar" -> karatsuba
    mode = "sch" -> schoolbook
    """




    A0, A1 = split_uint128_to_64(A)
    B0, B1 = split_uint128_to_64(B)

    # 產生 C 程式
    code = f"""
#include <stdio.h>
#include <stdint.h>

typedef struct {{
    // v[0] 是最低 64 bits, v[1] 是最高 64 bits (共 128 bits)
    uint64_t v[2];
}} uint128_t;

typedef struct {{
    // v[0] 是最低 64 bits, v[3] 是最高 64 bits (共 256 bits)
    uint64_t v[4];
}} uint256_t;

typedef struct {{
    // v[0] 是最低 64 bits, v[7] 是最高 64 bits (共 512 bits)
    uint64_t v[8];
}} uint512_t;

extern void uint128_mul(uint128_t *A, uint128_t *B, uint256_t *R);


int main() {{
    // 1) 先宣告 A, B (from python)


    uint128_t A = {{ 0x{A0:016x}, 0x{A1:016x} }};
    uint128_t B = {{ 0x{B0:016x}, 0x{B1:016x} }};
    uint256_t R = {{ 0 }};

    // 2) call int128_mul
    uint128_mul(&A, &B, &R);
    
    // 3) print results

    uint64_t r0 = R.v[0];
    uint64_t r1 = R.v[1];
    uint64_t r2 = R.v[2];
    uint64_t r3 = R.v[3];
    uint64_t r4 = R.v[4];
    uint64_t r5 = R.v[5];
    uint64_t r6 = R.v[6];
    uint64_t r7 = R.v[7];

    // print results
    // print r0, r1, r2, r3 in hex
    // Python 端再 parse
    printf("%016llx\\n%016llx\\n%016llx\\n%016llx\\n%016llx\\n%016llx\\n%016llx\\n%016llx\\n", 
        (unsigned long long)r0,
        (unsigned long long)r1,
        (unsigned long long)r2,
        (unsigned long long)r3,
        (unsigned long long)r4,
        (unsigned long long)r5,
        (unsigned long long)r6,
        (unsigned long long)r7
    );

    return 0;
}}
"""
    return code


def main():



    for _ in range(1):

        A = gen_random_int128()
        B = gen_random_int128()





        # 產生 C 程式
        code = generate_c_program(A, B)

        # 寫到 test_generated.c
        with open("test_generated.c", "w") as f:
            f.write(code)
        print("Generated test_generated.c for A,B")

        # 編譯
        cmd_compile = ["gcc", "test_generated.c", "-o", "test_generated"]
        # 如果你要 link 你的 int128.S, 可做:
        cmd_compile = ["gcc", "test_generated.c", "uint128_mul.S", "-o", "test_generated"]

        subprocess.run(cmd_compile, check=True)

        # 執行
        cmd_run = ["./test_generated"]
        result = subprocess.run(cmd_run, capture_output=True, check=True, text=True)

        # result.stdout 會是剛才程式印出的
        lines = result.stdout.strip().split("\n")
        if len(lines) < 8:
            print("Output lines < 8 ???", lines)
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


        # unify => 320 bits

        val_asm = unify_limbs_to_uint256(v0=r0, v1=r1, v2=r2, v3=r3)


        # 用 python 大整數算
        correct_result = A * B


        
        # 比對
        if correct_result == val_asm:
            print(f"Test {_+1} OK.  result match. ")
        else:
            print(f"Test FAIL")


        A_str = format_128_hex_grouped(A)
        B_str = format_128_hex_grouped(B)
        asm_str = format_256_hex_grouped(val_asm) 
        py_str  = format_256_hex_grouped(correct_result)

        print("The operands are: ")
        print(f"A hex (grouped) = {A_str}")
        print(f"B hex (grouped) = {B_str}")
        print("The results are: ")
        print(f"ASM hex (grouped) = {asm_str}")
        print(f"PY  hex (grouped) = {py_str}")

        difference = val_asm - correct_result
        diff_str = format_256_hex_grouped(difference)
        print(f"difference hex (grouped) = {diff_str}")
        break




if __name__ == "__main__":
    main()
