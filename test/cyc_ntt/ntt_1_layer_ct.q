int64 pointer_a
int64 pointer_b
int64 omega

int64 temp_a
int64 temp_b
int64 temp_mul

int64 out_a
int64 out_b

# 告訴 qhasm：pointer_a 與 pointer_b 是輸入參數
# (對應在 AArch64 呼叫慣例中通常是 x0, x1)
# 也就是 C 裏的 (uint64_t *a, uint64_t *b)
input pointer_a
input pointer_b
input omega

# qhasm: enter ntt_1_layer_ct
enter ntt_1_layer_ct

# 1) 讀取 *a, *b
temp_a = mem64[pointer_a+0]
temp_b = mem64[pointer_b+0]

# 2) 計算 temp_mul = omega * temp_b
temp_mul = omega * temp_b

# 3) out_a = temp_a + temp_mul
out_a = temp_a + temp_mul

# 4) out_b = temp_a - temp_mul
out_b = temp_a - temp_mul

# 5) 存回記憶體
mem64[pointer_a+0] = out_a
mem64[pointer_b+0] = out_b

# 結束
return


