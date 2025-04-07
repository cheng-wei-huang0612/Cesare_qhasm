
#include <stdio.h>
#include <stdint.h>


typedef struct {
    // v[0] 是最低 64 bits, v[1] 是最高 64 bits (共 128 bits)
    uint64_t v[2];
} int128_t;

typedef struct {
    // v[0] 最低 64 bits, v[3] 最高 64 bits (共 256 bits)
    uint64_t v[4];
} int256_t;

typedef struct {
    // v[0] 最低 64 bits, v[7] 最高 64 bits (共 512 bits)
    uint64_t v[8];
} int512_t;

//extern void int128_mul(int128_t *A, int128_t *B, int256_t *R);
extern void int256_mul(int256_t *A, int256_t *B, int512_t *R);


int main() {
    // 1) 先宣告 A, B (from python)


    int256_t A = { 0x676c0deffc65585f, 0x0540428b90879203, 0x296fbef5754ca57f, 0xeee676f7d92c80c1 };
    int256_t B = { 0x6b807de9742d415f, 0xb104a3893955974a, 0x6cc31c8f048644fb, 0xcbdeef77df0daa8f };
    int512_t R = { 0 };

    // 2) call int256_mul
    int256_mul(&A, &B, &R);
    
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
