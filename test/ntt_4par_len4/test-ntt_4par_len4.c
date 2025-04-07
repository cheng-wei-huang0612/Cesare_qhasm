#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "data.h"

// 1) 宣告匯入的組合語言函式介面 (與 .S/.q 檔案對應)
extern void ct_4par_len2(
    int32_t *N,           
    int32_t *in,          
    int32_t *omegas,      
    int32_t *mu_omegas    
);

extern void gs_4par_len2(
    int32_t *N,           
    int32_t *in,          
    int32_t *omegas,      
    int32_t *mu_omegas    
);

extern void gs_4par_len2_last(
    int32_t *N, int32_t *in, 
    int32_t *omegas, int32_t *mu_omegas,
    int32_t *inv4, int32_t *mu_inv4
);

extern void mul_inv_4(
    int32_t *in,          
    const int32_t *N,     
    const int32_t *inv4,  
    const int32_t *mu_inv4
);

extern void pointmul_4(
    int32_t *inA,  
    int32_t *inB,  
    int32_t *N,    
    int32_t *muN   
);



// ----------------------------------------------------------------------------
// 3) 純 C 版本 (模擬) - 僅示範邏輯，不代表真正的 CT/GS/mul_inv 演算法正確
//    只用來檢查最終結果位置與呼叫順序是否符合
// ----------------------------------------------------------------------------
static void ct_4par_len2_ref(int32_t *N, int32_t *in,
                             int32_t *omegas, int32_t *mu_omegas)
{
    // in[] = data0(4 int32) + data1(4 int32)
    // 做 2-point butterfly (Cooley–Tukey) + mul
    // 這裡僅作示範: data1[i] *= omegas[i] 
    for(int i=0; i<4; i++){
        int32_t tmp = in[i+4];
        // mod 省略..., 只做 *omegas
        in[i+4] = tmp * omegas[i];
    }
    // 省略 butterfly ...
}

static void gs_4par_len2_ref(int32_t *N, int32_t *in,
                             int32_t *omegas, int32_t *mu_omegas)
{
    // GS 反變換 - 只示範: tmp1 = (data0 - data1) * omegas
    // in[0..3], in[4..7]
    for(int i=0;i<4;i++){
        int32_t d0 = in[i];
        int32_t d1 = in[i+4];
        // 省略 mod, 只乘 ...
        int32_t diff = (d0 - d1)*omegas[i];
        in[i+4] = diff;
    }
}

static void gs_4par_len2_last_ref(int32_t *N, int32_t *in,
                                  int32_t *omegas, int32_t *mu_omegas,
                                  int32_t *inv4, int32_t *mu_inv4)
{
    // 做 GS + 最後除以 4
    gs_4par_len2_ref(N, in, omegas, mu_omegas);
    // 再把 in[0..7] 各元素 /4
    for(int i=0;i<8;i++){
        in[i] /= 4; 
    }
}

static void mul_inv_4_ref(int32_t *in,
                          const int32_t *N,
                          const int32_t *inv4,
                          const int32_t *mu_inv4)
{
    // 把 in[] 8 個數，每4 int32 block -> (x * inv4) % N?
    // 只示範: x[i] /= 4
    for(int i=0;i<8;i++){
        in[i] /= 4; 
    }
}

static void pointmul_4_ref(int32_t *inA, int32_t *inB,
                           int32_t *N, int32_t *muN)
{
    // 把 inA[i] = inA[i] * inB[i]
    for(int i=0;i<8;i++){
        inA[i] *= inB[i];
    }
}

// ----------------------------------------------------------------------------
// 4) 測試流程
// ----------------------------------------------------------------------------
int main(void)
{
    // 資料: 
    int32_t inA[16]     = {0}; 
    int32_t inB[16]     = {0}; 

    for (size_t i = 0; i < 16; i+=4)
    {
        inA[i] = a0[i];
        inA[i + 1] = a1[i];
        inA[i + 2] = a2[i];
        inA[i + 3] = a3[i];
        inB[i] = b0[i];
        inB[i + 1] = b1[i];
        inB[i + 2] = b2[i];
        inB[i + 3] = b3[i];
        
    }
    printf("inA: ");
    for (size_t i = 0; i < 16; i++)
    {
        printf("%d ", inA[i]);
    }
    printf("\n");
    printf("inB: ");
    for (size_t i = 0; i < 16; i++)
    {
        printf("%d ", inB[i]);
    }

    // 先拷貝 inA/inB 作為參考
    int32_t inA_backup[16];
    int32_t inB_backup[16];
    memcpy(inA_backup, inA, sizeof(inA));
    memcpy(inB_backup, inB, sizeof(inB));

    // ------------------------------------------------------------------------
    // (1) scenario #1:
    //
    //    ct_4par_len2()  * 4
    //    pointmul_4()
    //    gs_4par_len2() * 4
    //    mul_inv_4()
    // ------------------------------------------------------------------------
    printf("Scenario #1: ct4 x4 -> pointmul -> gs4 x4 -> mul_inv_4\n");

    

    return 0;
}
