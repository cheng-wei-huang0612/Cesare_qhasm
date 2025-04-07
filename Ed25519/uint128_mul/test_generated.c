
#include <stdio.h>
#include <stdint.h>

typedef struct {
    // v[0] 是最低 64 bits, v[1] 是最高 64 bits (共 128 bits)
    uint64_t v[2];
} uint128_t;

typedef struct {
    // v[0] 是最低 64 bits, v[3] 是最高 64 bits (共 256 bits)
    uint64_t v[4];
} uint256_t;

typedef struct {
    // v[0] 是最低 64 bits, v[7] 是最高 64 bits (共 512 bits)
    uint64_t v[8];
} uint512_t;

extern void uint128_mul(uint128_t *A, uint128_t *B, uint256_t *R);


int main() {
    // 1) 先宣告 A, B (from python)


    uint128_t A = { 0x7e61e68c1029a52d, 0xc561daf40c20001e };
    uint128_t B = { 0x7e1059b3b03d370b, 0xdc4f1cb95c8271fa };
    uint256_t R = { 0 };

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
