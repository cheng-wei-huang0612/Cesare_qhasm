# extern void gs_4par_len2_last(
#   int32_t *N, int32_t *in, 
#   int32_t *omegas, int32_t *mu_omegas,
#   int32_t *inv4, int32_t *mu_inv4
# );


int64 pointer_N
int64 pointer_in
int64 pointer_omegas
int64 pointer_mu_omegas
int64 pointer_inv4
int64 pointer_mu_inv4

input pointer_N
input pointer_in
input pointer_omegas
input pointer_mu_omegas
input pointer_inv4
input pointer_mu_inv4

reg128 data0
reg128 data1
reg128 n_vec
reg128 b_vec
reg128 mu_vec

reg128 inv4_vec
reg128 mu_inv4_vec

reg128 z
reg128 t
reg128 tmp0
reg128 tmp1

enter gs_4par_len2_last

# 1) load N[], in[], omegas[], mu_omegas[], inv4, mu_inv4
n_vec       = mem128[pointer_N+0]
data0       = mem128[pointer_in+0]
data1       = mem128[pointer_in+16]
b_vec       = mem128[pointer_omegas+0]
mu_vec      = mem128[pointer_mu_omegas+0]
inv4_vec    = mem128[pointer_inv4+0]
mu_inv4_vec = mem128[pointer_mu_inv4+0]

###############################################################################
# 2) GS butterfly
#   tmp0 = data0 + data1
#   tmp1 = data0 - data1
#   => tmp1 = (tmp1 * b) mod N
###############################################################################

4x tmp0 = data0 + data1
4x tmp1 = data0 - data1

# Barrett mul for tmp1
4x z = tmp1 * b_vec
4x t = (tmp1 * mu_vec) >> 31 round
4x z -= t * n_vec
tmp1 = z

###############################################################################
# 3) 把 tmp0, tmp1 都除以 4 => (tmp0 * inv4) mod N, (tmp1 * inv4) mod N
###############################################################################

# (a) tmp0 = (tmp0 * inv4) mod N
4x z = tmp0 * inv4_vec
4x t = (tmp0 * mu_inv4_vec) >> 31 round
4x z -= t * n_vec
tmp0 = z

# (b) tmp1 = (tmp1 * inv4) mod N
4x z = tmp1 * inv4_vec
4x t = (tmp1 * mu_inv4_vec) >> 31 round
4x z -= t * n_vec
tmp1 = z

###############################################################################
# 4) store back
###############################################################################
mem128[pointer_in+0]   = tmp0
mem128[pointer_in+16]  = tmp1

return
