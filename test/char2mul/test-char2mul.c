#include <stdio.h>
#include <stdint.h>

// extern 宣告同上
extern uint64_t gf2mul(uint64_t a, uint64_t b);

int main(void) {
    uint64_t x = 0x00000005ULL;
    uint64_t y = 0x00000003ULL;

    uint64_t z = gf2mul(x, y); // 呼叫你的組合語言函式

    printf("Result = 0x%llx\n", (unsigned long long) z);
    return 0;
}
