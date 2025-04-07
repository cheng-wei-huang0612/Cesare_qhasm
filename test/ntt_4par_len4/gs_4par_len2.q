# extern void gs_4par_len2(
#    int32_t *N,           # 4 個 int32 的模數
#    int32_t *in,          # 8 個 int32 (data0, data1)
#    int32_t *omegas,      # 4 個 int32 (twiddle factor)
#    int32_t *mu_omegas    # 4 個 int32 (對應 b 的 mu)
# );

int64 pointer_N
int64 pointer_in
int64 pointer_omegas
int64 pointer_mu_omegas

# 告訴 qhasm 這些是輸入（呼叫慣例對應）
input pointer_N
input pointer_in
input pointer_omegas
input pointer_mu_omegas

reg128 data0
reg128 data1
reg128 n_vec      # lane-wise N
reg128 b_vec      # lane-wise b (twiddle)
reg128 mu_vec     # lane-wise mu(b)
reg128 z          # 用來存 Barrett 的中間結果
reg128 t          # Barrett 的 sqrdmulh 結果
reg128 tmp0
reg128 tmp1

enter gs_4par_len2

###############################################################################
# 1) 載入 N[] (4 個 int32)
###############################################################################
n_vec = mem128[pointer_N+0]       # lane-wise N

###############################################################################
# 2) 讀取 in[] (共 8 個 int32)
#    前 16 bytes -> data0 (in[0..3])
#    後 16 bytes -> data1 (in[4..7])
###############################################################################
data0 = mem128[pointer_in+0]      # [ a0[0], a1[0], a2[0], a3[0] ]
data1 = mem128[pointer_in+16]     # [ a0[1], a1[1], a2[1], a3[1] ]

###############################################################################
# 3) 讀取 omegas[] (4 個 int32), mu_omegas[] (4 個 int32)
###############################################################################
b_vec  = mem128[pointer_omegas+0]     # lane-wise b
mu_vec = mem128[pointer_mu_omegas+0]  # lane-wise mu_b

###############################################################################
# 4) GS 公式:
#
#   tmp0 = data0 + data1
#   tmp1 = (data0 - data1)   <-- 後面會乘 b
#
#   tmp1 => Barrett mul => (tmp1 * b) mod N
#
#   3-instruction Barrett:
#    z = tmp1 * b_vec
#    t = (tmp1 * mu_vec) >> 31 round  (sqrdmulh)
#    z -= t * n_vec
###############################################################################

# 4a) tmp0, tmp1 (尚未乘 b)
4x tmp0 = data0 + data1
4x tmp1 = data0 - data1

# 4b) Barrett mul: z = (tmp1 * b) mod N
# (1) z = tmp1 * b_vec
4x z = tmp1 * b_vec

# (2) t = (tmp1 * mu_vec) >> 31 round  => sqrdmulh
4x t = (tmp1 * mu_vec) >> 31 round

# (3) z -= t * n_vec
4x z -= t * n_vec

###############################################################################
# 5) 寫回 in[]:
#    in[0..3] = tmp0
#    in[4..7] = z
#  (若要在最後一層 GS 做除以 2，請改用 gs_4par_len2_last.q 或之後 div_by_2.q)
###############################################################################

mem128[pointer_in+0]   = tmp0
mem128[pointer_in+16]  = z

return
