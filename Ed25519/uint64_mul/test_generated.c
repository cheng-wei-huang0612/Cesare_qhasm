
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

extern void uint64_mul(uint64_t *A, uint64_t *B, uint128_t *R);


int main() {
    // 1) 先宣告 A, B (from python)


    uint64_t A = 0x9ae143cabb3705d3;
    uint64_t B = 0x5a52da3ab55a63d0;
    uint128_t R = { 0 };

    // 2) call int64_mul
    uint64_mul(&A, &B, &R);
    
    // 3) print results

    uint64_t r0 = R.v[0];
    uint64_t r1 = R.v[1];


    // print results
    // print r0, r1, r2, r3 in hex
    // Python 端再 parse
    printf("%016llx\n%016llx\n", 
        (unsigned long long)r0,
        (unsigned long long)r1
    );

    return 0;
}
