
#include <stdio.h>
#include <stdint.h>



typedef struct {
    // v[0] 是最低 64 bits, v[3] 是最高 64 bits (共 256 bits)
    uint64_t v[4];
} uint256_t;

typedef struct {
    // v[0] 是最低 64 bits, v[7] 是最高 64 bits (共 512 bits)
    uint64_t v[8];
} uint512_t;

extern void uint256_mul_mod_p(uint256_t *A, uint256_t *B, uint512_t *R);


int main() {
    // 1) 先宣告 A, B (from python)


    uint256_t A = { 0x49e6edb9ac9a549b, 0x887b4a1ab8a551c7, 0x3cbc20168dc62394, 0xefe4b5767faba3b0 };
    uint256_t B = { 0xb927215fe2f0ef96, 0x030d0bd1f5aefec5, 0x555179e298c58114, 0xe3fded5821d2aace };
    uint512_t R = { 0 };

    // 2) call int128_mul
    uint256_mul_mod_p(&A, &B, &R);
    
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
    printf("%016llx\n%016llx\n%016llx\n%016llx\n%016llx\n%016llx\n%016llx\n%016llx\n", 
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
}
