# extern void ct_4par_len2(
#    int32_t *N,           # 4 個 int32 的模數
#    int32_t *in,          # 8 個 int32 (data0, data1)
#    int32_t *omegas,      # 4 個 int32 (twiddle factor)
#    int32_t *mu_omegas    # 4 個 int32 (對應 b 的 mu)
# );


int64 pointer_N
int64 pointer_in
int64 pointer_omegas
int64 pointer_mu_omegas

input pointer_N
input pointer_in
input pointer_omegas
input pointer_mu_omegas


reg128 data0
reg128 data1
reg128 n_vec
reg128 b_vec
reg128 mu_vec

reg128 z
reg128 t
reg128 sumv
reg128 diffv

enter ntt_4par_len2

# 1) 讀取 N[] (4 個 int32)
n_vec = mem128[pointer_N+0]      # lane-wise N

# 2) 讀取 in[] (共 8 個 int32 = 32 bytes)
data0 = mem128[pointer_in+0]     # in[0..3]
data1 = mem128[pointer_in+16]    # in[4..7]

# 3) 讀取 omegas[] (4 個 int32)
b_vec = mem128[pointer_omegas+0]  # lane-wise b

# 4) 讀取 mu_omegas[] (4 個 int32)
mu_vec = mem128[pointer_mu_omegas+0]  # lane-wise mu_b

#
# Barrett multiplication (3-instruction):
#   z = data1 * b_vec
#   t = (data1 * mu_vec) >> 31 round   (i.e. sqrdmulh)
#   z = z - (t * n_vec)
#

# (1) z = data1 * b_vec
4x z = data1 * b_vec

# (2) t = (data1 * mu_vec) >> 31 round
4x t = (data1 * mu_vec) >> 31 round

# (3) z -= t * n_vec
4x z -= t * n_vec

#
# 接著做蝴蝶加減
# sumv = data0 + z
# diffv= data0 - z
#
4x sumv  = data0 + z
4x diffv = data0 - z

# 5) 存回
mem128[pointer_in+0]   = sumv
mem128[pointer_in+16]  = diffv

return
