
# qhasm: int64 input_x0

# qhasm: int64 input_x1

# qhasm: int64 input_x2

# qhasm: int64 input_x3

# qhasm: int64 input_x4

# qhasm: int64 input_x5

# qhasm: int64 input_x6

# qhasm: int64 input_x7

# qhasm: int64 output_x0

# qhasm: int64 calleesaved_x18

# qhasm: int64 calleesaved_x19

# qhasm: int64 calleesaved_x20

# qhasm: int64 calleesaved_x21

# qhasm: int64 calleesaved_x22

# qhasm: int64 calleesaved_x23

# qhasm: int64 calleesaved_x24

# qhasm: int64 calleesaved_x25

# qhasm: int64 calleesaved_x26

# qhasm: int64 calleesaved_x27

# qhasm: int64 calleesaved_x28

# qhasm: int64 calleesaved_x29

# qhasm: reg128 input_v0

# qhasm: reg128 input_v1

# qhasm: reg128 input_v2

# qhasm: reg128 input_v3

# qhasm: reg128 input_v4

# qhasm: reg128 input_v5

# qhasm: reg128 input_v6

# qhasm: reg128 input_v7

# qhasm: reg128 output_v0

# qhasm: reg128 calleesaved_v8

# qhasm: reg128 calleesaved_v9

# qhasm: reg128 calleesaved_v10

# qhasm: reg128 calleesaved_v11

# qhasm: reg128 calleesaved_v12

# qhasm: reg128 calleesaved_v13

# qhasm: reg128 calleesaved_v14

# qhasm: reg128 calleesaved_v15

# qhasm: int64 pointer_N

# qhasm: int64 pointer_in

# qhasm: int64 pointer_omegas

# qhasm: int64 pointer_mu_omegas

# qhasm: int64 pointer_inv4

# qhasm: int64 pointer_mu_inv4

# qhasm: input pointer_N

# qhasm: input pointer_in

# qhasm: input pointer_omegas

# qhasm: input pointer_mu_omegas

# qhasm: input pointer_inv4

# qhasm: input pointer_mu_inv4

# qhasm: reg128 data0

# qhasm: reg128 data1

# qhasm: reg128 n_vec

# qhasm: reg128 b_vec

# qhasm: reg128 mu_vec

# qhasm: reg128 inv4_vec

# qhasm: reg128 mu_inv4_vec

# qhasm: reg128 z

# qhasm: reg128 t

# qhasm: reg128 tmp0

# qhasm: reg128 tmp1

# qhasm: enter gs_4par_len2_last
.align 4
.global _gs_4par_len2_last
.global gs_4par_len2_last
_gs_4par_len2_last:
gs_4par_len2_last:

# qhasm: n_vec       = mem128[pointer_N+0]
# asm 1: ldr >n_vec=reg128#1%qregname,[<pointer_N=int64#1,#0]
# asm 2: ldr >n_vec=q0,[<pointer_N=x0,#0]
ldr q0,[x0,#0]

# qhasm: data0       = mem128[pointer_in+0]
# asm 1: ldr >data0=reg128#2%qregname,[<pointer_in=int64#2,#0]
# asm 2: ldr >data0=q1,[<pointer_in=x1,#0]
ldr q1,[x1,#0]

# qhasm: data1       = mem128[pointer_in+16]
# asm 1: ldr >data1=reg128#3%qregname,[<pointer_in=int64#2,#16]
# asm 2: ldr >data1=q2,[<pointer_in=x1,#16]
ldr q2,[x1,#16]

# qhasm: b_vec       = mem128[pointer_omegas+0]
# asm 1: ldr >b_vec=reg128#4%qregname,[<pointer_omegas=int64#3,#0]
# asm 2: ldr >b_vec=q3,[<pointer_omegas=x2,#0]
ldr q3,[x2,#0]

# qhasm: mu_vec      = mem128[pointer_mu_omegas+0]
# asm 1: ldr >mu_vec=reg128#5%qregname,[<pointer_mu_omegas=int64#4,#0]
# asm 2: ldr >mu_vec=q4,[<pointer_mu_omegas=x3,#0]
ldr q4,[x3,#0]

# qhasm: inv4_vec    = mem128[pointer_inv4+0]
# asm 1: ldr >inv4_vec=reg128#6%qregname,[<pointer_inv4=int64#5,#0]
# asm 2: ldr >inv4_vec=q5,[<pointer_inv4=x4,#0]
ldr q5,[x4,#0]

# qhasm: mu_inv4_vec = mem128[pointer_mu_inv4+0]
# asm 1: ldr >mu_inv4_vec=reg128#7%qregname,[<pointer_mu_inv4=int64#6,#0]
# asm 2: ldr >mu_inv4_vec=q6,[<pointer_mu_inv4=x5,#0]
ldr q6,[x5,#0]

# qhasm: 4x tmp0 = data0 + data1
# asm 1: add >tmp0=reg128#8.4s,<data0=reg128#2.4s,<data1=reg128#3.4s
# asm 2: add >tmp0=v7.4s,<data0=v1.4s,<data1=v2.4s
add v7.4s,v1.4s,v2.4s

# qhasm: 4x tmp1 = data0 - data1
# asm 1: sub >tmp1=reg128#2.4s,<data0=reg128#2.4s,<data1=reg128#3.4s
# asm 2: sub >tmp1=v1.4s,<data0=v1.4s,<data1=v2.4s
sub v1.4s,v1.4s,v2.4s

# qhasm: 4x z = tmp1 * b_vec
# asm 1: mul >z=reg128#3.4s,<tmp1=reg128#2.4s,<b_vec=reg128#4.4s
# asm 2: mul >z=v2.4s,<tmp1=v1.4s,<b_vec=v3.4s
mul v2.4s,v1.4s,v3.4s

# qhasm: 4x t = (tmp1 * mu_vec) >> 32 round
# asm 1: sqrdmulh >t=reg128#2.4s,<tmp1=reg128#2.4s,<mu_vec=reg128#5.4s
# asm 2: sqrdmulh >t=v1.4s,<tmp1=v1.4s,<mu_vec=v4.4s
sqrdmulh v1.4s,v1.4s,v4.4s

# qhasm: 4x z -= t * n_vec
# asm 1: mls <z=reg128#3.4s,<t=reg128#2.4s,<n_vec=reg128#1.4s
# asm 2: mls <z=v2.4s,<t=v1.4s,<n_vec=v0.4s
mls v2.4s,v1.4s,v0.4s

# qhasm: tmp1 = z
# asm 1: mov >tmp1=reg128#2.16b,<z=reg128#3.16b
# asm 2: mov >tmp1=v1.16b,<z=v2.16b
mov v1.16b,v2.16b

# qhasm: 4x z = tmp0 * inv4_vec
# asm 1: mul >z=reg128#3.4s,<tmp0=reg128#8.4s,<inv4_vec=reg128#6.4s
# asm 2: mul >z=v2.4s,<tmp0=v7.4s,<inv4_vec=v5.4s
mul v2.4s,v7.4s,v5.4s

# qhasm: 4x t = (tmp0 * mu_inv4_vec) >> 32 round
# asm 1: sqrdmulh >t=reg128#4.4s,<tmp0=reg128#8.4s,<mu_inv4_vec=reg128#7.4s
# asm 2: sqrdmulh >t=v3.4s,<tmp0=v7.4s,<mu_inv4_vec=v6.4s
sqrdmulh v3.4s,v7.4s,v6.4s

# qhasm: 4x z -= t * n_vec
# asm 1: mls <z=reg128#3.4s,<t=reg128#4.4s,<n_vec=reg128#1.4s
# asm 2: mls <z=v2.4s,<t=v3.4s,<n_vec=v0.4s
mls v2.4s,v3.4s,v0.4s

# qhasm: tmp0 = z
# asm 1: mov >tmp0=reg128#3.16b,<z=reg128#3.16b
# asm 2: mov >tmp0=v2.16b,<z=v2.16b
mov v2.16b,v2.16b

# qhasm: 4x z = tmp1 * inv4_vec
# asm 1: mul >z=reg128#4.4s,<tmp1=reg128#2.4s,<inv4_vec=reg128#6.4s
# asm 2: mul >z=v3.4s,<tmp1=v1.4s,<inv4_vec=v5.4s
mul v3.4s,v1.4s,v5.4s

# qhasm: 4x t = (tmp1 * mu_inv4_vec) >> 32 round
# asm 1: sqrdmulh >t=reg128#2.4s,<tmp1=reg128#2.4s,<mu_inv4_vec=reg128#7.4s
# asm 2: sqrdmulh >t=v1.4s,<tmp1=v1.4s,<mu_inv4_vec=v6.4s
sqrdmulh v1.4s,v1.4s,v6.4s

# qhasm: 4x z -= t * n_vec
# asm 1: mls <z=reg128#4.4s,<t=reg128#2.4s,<n_vec=reg128#1.4s
# asm 2: mls <z=v3.4s,<t=v1.4s,<n_vec=v0.4s
mls v3.4s,v1.4s,v0.4s

# qhasm: tmp1 = z
# asm 1: mov >tmp1=reg128#1.16b,<z=reg128#4.16b
# asm 2: mov >tmp1=v0.16b,<z=v3.16b
mov v0.16b,v3.16b

# qhasm: mem128[pointer_in+0]   = tmp0
# asm 1: str <tmp0=reg128#3%qregname,[<pointer_in=int64#2,#0]
# asm 2: str <tmp0=q2,[<pointer_in=x1,#0]
str q2,[x1,#0]

# qhasm: mem128[pointer_in+16]  = tmp1
# asm 1: str <tmp1=reg128#1%qregname,[<pointer_in=int64#2,#16]
# asm 2: str <tmp1=q0,[<pointer_in=x1,#16]
str q0,[x1,#16]

# qhasm: return
ret
