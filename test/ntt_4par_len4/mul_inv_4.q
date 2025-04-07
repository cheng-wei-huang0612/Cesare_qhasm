#extern void mul_inv_4(
#    int32_t *in,           // 指向 16個 int32
#    const int32_t *N,      // 指向 4個 int32 (N[0..3])
#    const int32_t *inv4,   // 指向 4個 int32 ((1/4) mod N[j])
#    const int32_t *mu_inv4 // 指向 4個 int32 (Barrett常數)
#);


int64 pointer_in
int64 pointer_N
int64 pointer_inv4
int64 pointer_mu_inv4
int64 offset
int64 end
int64 step

reg128 n_vec
reg128 inv4_vec
reg128 mu_vec
reg128 data
reg128 z
reg128 t

enter mul_inv_4

# load
n_vec = mem128[pointer_N+0]
inv4_vec = mem128[pointer_inv4+0]
mu_vec   = mem128[pointer_mu_inv4+0]

offset = 0
end    = 64
step   = 16


loop:


int64 new_r
new_r = pointer_in + offset

data = mem128[new_r]


4x z = data * inv4_vec


4x t = (data * mu_vec) >> 31 round


4x z -= t * n_vec


mem128[new_r] = z


offset += step


offset - end
goto loop if !unsigned<

return
