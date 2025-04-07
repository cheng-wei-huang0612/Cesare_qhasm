
#include <stdio.h>
#include <stdint.h>


typedef struct {
    // v[0] 是最低 64 bits, v[1] 是最高 64 bits (共 128 bits)
    uint64_t v[2];
} int128_t;

typedef struct {
    // v[0] 是最低 64 bits, v[3] 是最高 64 bits (共 256 bits)
    uint64_t v[4];
} int256_t;

extern void int128_mul(int128_t *A, int128_t *B, int256_t *R);
extern void int128_mul_sch(int128_t *A, int128_t *B, int256_t *R);


int main() {
    // 1) 先宣告 A, B (from python)


    int128_t A = { 0x8b3d67bda3f4096e, 0x190ffb916c496d9b };
    int128_t B = { 0xc5ef13871ea47204, 0x8f64f4f523693740 };
    int256_t R = { 0 };

    // 2) call int128_mul
    int128_mul_sch(&A, &B, &R);
    
    // 3) print results

    uint64_t r0 = R.v[0];
    uint64_t r1 = R.v[1];
    uint64_t r2 = R.v[2];
    uint64_t r3 = R.v[3];

    // print results
    // print r0, r1, r2, r3 in hex
    // Python 端再 parse
    printf("%016llx\n%016llx\n%016llx\n%016llx\n", 
        (unsigned long long)r0,
        (unsigned long long)r1,
        (unsigned long long)r2,
        (unsigned long long)r3
    );

    return 0;
}
