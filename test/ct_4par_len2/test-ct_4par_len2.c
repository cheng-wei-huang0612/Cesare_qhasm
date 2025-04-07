#include <stdio.h>
#include <stdint.h>
#include <math.h>    // 為了使用 round/nearbyint等

// 這是你的 NEON 版本 (組合語言實現):
// 現在仍然只宣告 2 參數，依你目前的 .S/.q 寫法
extern void ntt_4par_len2(int32_t *N, int32_t *in, int32_t *omegas, int32_t *mu_omegas);

// -------------------
// 1) 計算 mu 的函式
//    mu = round( (b * 2^32) / (2*N) )
static int32_t get_mu(int32_t b, int32_t N)
{
    // 注意：我們可以先用 64-bit 做乘法，避免溢位
    //       這邊用 double 也行，但要留意誤差。
    // 這裡示範用 double，計算 (b * 2^32)/(2*N) 然後 round。
    // 假設 b, N < 2^31，不會超過 double 的精度太多。
    double val = ((double)b * (double)((uint64_t)1 << 32)) / (2.0 * (double)N);
    // 你可以用 round(), nearbyint() 等
    double r = nearbyint(val);  // 取最接近整數
    if (r > 2147483647.0) r = 2147483647.0;
    if (r < -2147483648.0) r = -2147483648.0;
    return (int32_t)r;
}

// -------------------
// 2) 參考版 ntt_4par_len2_ref (模擬三條指令，但實際用 % 做 mod)
//    多帶參數 mu_omegas[]、N[]，以示範
void ntt_4par_len2_ref(int32_t *N, int32_t *in,  int32_t *omegas, 
                        int32_t *mu_omegas)
{
    // data0, data1 各 4
    int32_t data0[4], data1[4];
    for (int i = 0; i < 4; i++) {
        data0[i] = in[i];      // aX[0]
        data1[i] = in[i + 4];  // aX[1]
    }

    // 做 barrett mul =>  z = ( data1 * omegas[i] ) mod N[i]
    // 這邊直接做 (data1[i] * omegas[i]) % N[i]
    // 之後再 butterfly
    int32_t z[4];
    for (int i = 0; i < 4; i++) {
        // 先乘
        int64_t tmp = (int64_t)data1[i] * (int64_t)omegas[i];
        // 再 mod
        // 如果 N[i] == 0 (不應該發生)，這裡要避開。暫且假設 N[i]>0
        int32_t mm = (int32_t)(tmp % N[i]);
        // signed representation
        if (mm >  (N[i]>>1))  mm -= N[i];
        if (mm <= -(N[i]>>1)) mm += N[i];
        z[i] = mm;
    }

    // 接著做 butterfly
    int32_t sumv[4], diffv[4];
    for (int i = 0; i < 4; i++) {
        sumv[i]  = data0[i] + z[i];   // data0 + z
        diffv[i] = data0[i] - z[i];   // data0 - z
    }

    // 寫回 in
    for (int i = 0; i < 4; i++) {
        in[i]     = sumv[i];
        in[i + 4] = diffv[i];
    }
}


int main(void)
{
    // 範例:
    // N[4], in[8], omegas[4]
    // 然後計算 mu_omegas[4] 供參考。
    int32_t N[4] = { 17, 23, 25, 29 };  // 假設每 lane 一個 mod
    int32_t in[8] = {1, 2, 3, 4,  10, 11, 12, 13};
    int32_t in_ref[8];
    int32_t omegas[4] = {5, 6, 7, 8};    // 每 lane 一個 b
    int32_t mu_omegas[4];

    // 計算 mu_omegas
    for (int i = 0; i < 4; i++) {
        mu_omegas[i] = get_mu(omegas[i], N[i]);
    }

    // Copy
    for (int i = 0; i < 8; i++) {
        in_ref[i] = in[i];
    }

    // NEON 版本 (組合語言):
    // 目前你只定義了 ntt_4par_len2(int32_t *in, int32_t *omegas)
    // => 你可能暫時無法帶入 N, mu_omegas(除非改 .S 介面)
    // => 此處只示範 "b" = omegas
    //    => reduction 可能還沒做好 in NEON?
    // 先呼叫看看
    ntt_4par_len2(N, in, omegas, mu_omegas);

    // 參考版本
    ntt_4par_len2_ref(N,in_ref, omegas, mu_omegas);

    // 印出
    printf("NEON version:\n");
    for (int i = 0; i < 8; i++) {
        printf("  in[%d] = %d\n", i, in[i]);
    }

    printf("Reference version:\n");
    for (int i = 0; i < 8; i++) {
        printf("  in_ref[%d] = %d\n", i, in_ref[i]);
    }


    return 0;
}
