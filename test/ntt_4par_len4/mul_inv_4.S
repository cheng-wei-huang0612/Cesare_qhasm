
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

# qhasm: int64 pointer_in

# qhasm: int64 pointer_N

# qhasm: int64 pointer_inv4

# qhasm: int64 pointer_mu_inv4

# qhasm: int64 offset

# qhasm: int64 end

# qhasm: int64 step

# qhasm: reg128 n_vec

# qhasm: reg128 inv4_vec

# qhasm: reg128 mu_vec

# qhasm: reg128 data

# qhasm: reg128 z

# qhasm: reg128 t

# qhasm: enter mul_inv_4
.align 4
.global _mul_inv_4
.global mul_inv_4
_mul_inv_4:
mul_inv_4:

# qhasm: n_vec = mem128[pointer_N+0]
# asm 1: ldr >n_vec=reg128#1%qregname,[<pointer_N=int64#1,#0]
# asm 2: ldr >n_vec=q0,[<pointer_N=x0,#0]
ldr q0,[x0,#0]

# qhasm: inv4_vec = mem128[pointer_inv4+0]
# asm 1: ldr >inv4_vec=reg128#2%qregname,[<pointer_inv4=int64#1,#0]
# asm 2: ldr >inv4_vec=q1,[<pointer_inv4=x0,#0]
ldr q1,[x0,#0]

# qhasm: mu_vec   = mem128[pointer_mu_inv4+0]
# asm 1: ldr >mu_vec=reg128#3%qregname,[<pointer_mu_inv4=int64#1,#0]
# asm 2: ldr >mu_vec=q2,[<pointer_mu_inv4=x0,#0]
ldr q2,[x0,#0]

# qhasm: offset = 0
# asm 1: mov >offset=int64#1, #0
# asm 2: mov >offset=x0, #0
mov x0, #0

# qhasm: end    = 64
# asm 1: mov >end=int64#2, #64
# asm 2: mov >end=x1, #64
mov x1, #64

# qhasm: step   = 16
# asm 1: mov >step=int64#3, #16
# asm 2: mov >step=x2, #16
mov x2, #16

# qhasm: loop:
._loop:

# qhasm: int64 new_r

# qhasm: new_r = pointer_in + offset
# asm 1: add >new_r=int64#5,<pointer_in=int64#4,<offset=int64#1
# asm 2: add >new_r=x4,<pointer_in=x3,<offset=x0
add x4,x3,x0

# qhasm: data = mem128[new_r]
# asm 1: ldr >data=reg128#4%qregname,[<new_r=int64#5]
# asm 2: ldr >data=q3,[<new_r=x4]
ldr q3,[x4]

# qhasm: 4x z = data * inv4_vec
# asm 1: mul >z=reg128#5.4s,<data=reg128#4.4s,<inv4_vec=reg128#2.4s
# asm 2: mul >z=v4.4s,<data=v3.4s,<inv4_vec=v1.4s
mul v4.4s,v3.4s,v1.4s

# qhasm: 4x t = (data * mu_vec) >> 32 round
# asm 1: sqrdmulh >t=reg128#4.4s,<data=reg128#4.4s,<mu_vec=reg128#3.4s
# asm 2: sqrdmulh >t=v3.4s,<data=v3.4s,<mu_vec=v2.4s
sqrdmulh v3.4s,v3.4s,v2.4s

# qhasm: 4x z -= t * n_vec
# asm 1: mls <z=reg128#5.4s,<t=reg128#4.4s,<n_vec=reg128#1.4s
# asm 2: mls <z=v4.4s,<t=v3.4s,<n_vec=v0.4s
mls v4.4s,v3.4s,v0.4s

# qhasm: mem128[new_r] = z
# asm 1: str <z=reg128#5%qregname,[<new_r=int64#5]
# asm 2: str <z=q4,[<new_r=x4]
str q4,[x4]

# qhasm: offset += step
# asm 1: add <offset=int64#1,<offset=int64#1,<step=int64#3
# asm 2: add <offset=x0,<offset=x0,<step=x2
add x0,x0,x2

# qhasm: offset - end
# asm 1: cmp <offset=int64#1,<end=int64#2
# asm 2: cmp <offset=x0,<end=x1
cmp x0,x1

# qhasm: goto loop if !unsigned<
b.hs ._loop

# qhasm: return
ret
