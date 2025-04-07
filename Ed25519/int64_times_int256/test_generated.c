
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

typedef struct {
    // v[0] 是最低 64 bits, v[4] 是最高 64 bits (共 320 bits)
    uint64_t v[5];
} int320_t;

extern void int64_times_int256(int64_t *A, int256_t *B, int320_t *R);


int main() {
    // 1) 先宣告 A, B (from python)


    int64_t A =  0xca74cb98dbce0718 ;
    int256_t B = { 0xffffffffffffffed, 0xffffffffffffffff, 0xffffffffffffffff, 0x7fffffffffffffff };
    int320_t R = { 0 };

    // 2) call int128_mul
    int64_times_int256(&A, &B, &R);
    
    // 3) print results

    uint64_t r0 = R.v[0];
    uint64_t r1 = R.v[1];
    uint64_t r2 = R.v[2];
    uint64_t r3 = R.v[3];
    uint64_t r4 = R.v[4];

    // print results
    // print r0, r1, r2, r3 in hex
    // Python 端再 parse
    printf("%016llx\n%016llx\n%016llx\n%016llx\n%016llx\n", 
        (unsigned long long)r0,
        (unsigned long long)r1,
        (unsigned long long)r2,
        (unsigned long long)r3,
        (unsigned long long)r4
    );

    return 0;
}
