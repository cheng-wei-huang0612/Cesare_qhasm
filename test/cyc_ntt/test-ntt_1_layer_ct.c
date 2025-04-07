#include <stdio.h>
#include <stdint.h>

// 從組合語言連結進來
extern void ntt_1_layer_ct(int64_t* a, int64_t* b, int64_t omega);


int main(void) {
    
    int64_t x = 1;
    int64_t y = 1;
    int64_t omega = 2;

    // 呼叫 qhasm+aarch64 產生的函式
    ntt_1_layer_ct(&x, &y, omega);

    // 期待： x = (1 + 1) = 2, y = (1 - 1) = 0
    printf("x = %lld, y = %lld\n",
           (long long)x,
           (long long)y);

    return 0;
}
