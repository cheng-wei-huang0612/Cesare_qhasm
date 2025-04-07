
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

# qhasm: int64 pointer_inA

# qhasm: int64 pointer_inB

# qhasm: int64 pointer_N

# qhasm: int64 pointer_muN

# qhasm: input pointer_inA

# qhasm: input pointer_inB

# qhasm: input pointer_N

# qhasm: input pointer_muN

# qhasm: int64 offset

# qhasm: int64 end

# qhasm: int64 step

# qhasm: reg128 a_vec

# qhasm: reg128 b_vec

# qhasm: reg128 n_vec

# qhasm: reg128 mu_vec

# qhasm: reg128 z

# qhasm: reg128 t

# qhasm: enter pointmul
.align 4
.global _pointmul
.global pointmul
_pointmul:
pointmul:

# qhasm: n_vec  = mem128[pointer_N+0]
# asm 1: ldr >n_vec=reg128#1%qregname,[<pointer_N=int64#3,#0]
# asm 2: ldr >n_vec=q0,[<pointer_N=x2,#0]
ldr q0,[x2,#0]

# qhasm: mu_vec = mem128[pointer_muN+0]
# asm 1: ldr >mu_vec=reg128#2%qregname,[<pointer_muN=int64#4,#0]
# asm 2: ldr >mu_vec=q1,[<pointer_muN=x3,#0]
ldr q1,[x3,#0]

# qhasm: offset = 0
# asm 1: mov >offset=int64#3, #0
# asm 2: mov >offset=x2, #0
mov x2, #0

# qhasm: end    = 64    
# asm 1: mov >end=int64#4, #64
# asm 2: mov >end=x3, #64
mov x3, #64

# qhasm: step   = 16
# asm 1: mov >step=int64#5, #16
# asm 2: mov >step=x4, #16
mov x4, #16

# qhasm: pointmul_loop:
._pointmul_loop:

# qhasm: int64 newA

# qhasm: int64 newB

# qhasm: newA = pointer_inA + offset
# asm 1: add >newA=int64#6,<pointer_inA=int64#1,<offset=int64#3
# asm 2: add >newA=x5,<pointer_inA=x0,<offset=x2
add x5,x0,x2

# qhasm: newB = pointer_inB + offset
# asm 1: add >newB=int64#7,<pointer_inB=int64#2,<offset=int64#3
# asm 2: add >newB=x6,<pointer_inB=x1,<offset=x2
add x6,x1,x2

# qhasm: a_vec = mem128[newA]
# asm 1: ldr >a_vec=reg128#3%qregname,[<newA=int64#6]
# asm 2: ldr >a_vec=q2,[<newA=x5]
ldr q2,[x5]

# qhasm: b_vec = mem128[newB]
# asm 1: ldr >b_vec=reg128#4%qregname,[<newB=int64#7]
# asm 2: ldr >b_vec=q3,[<newB=x6]
ldr q3,[x6]

# qhasm: 4x z = a_vec * b_vec                    
# asm 1: mul >z=reg128#4.4s,<a_vec=reg128#3.4s,<b_vec=reg128#4.4s
# asm 2: mul >z=v3.4s,<a_vec=v2.4s,<b_vec=v3.4s
mul v3.4s,v2.4s,v3.4s

# qhasm: 4x t = (a_vec * mu_vec) >> 32 round     
# asm 1: sqrdmulh >t=reg128#3.4s,<a_vec=reg128#3.4s,<mu_vec=reg128#2.4s
# asm 2: sqrdmulh >t=v2.4s,<a_vec=v2.4s,<mu_vec=v1.4s
sqrdmulh v2.4s,v2.4s,v1.4s

# qhasm: 4x z -= t * n_vec                       
# asm 1: mls <z=reg128#4.4s,<t=reg128#3.4s,<n_vec=reg128#1.4s
# asm 2: mls <z=v3.4s,<t=v2.4s,<n_vec=v0.4s
mls v3.4s,v2.4s,v0.4s

# qhasm: mem128[newA] = z
# asm 1: str <z=reg128#4%qregname,[<newA=int64#6]
# asm 2: str <z=q3,[<newA=x5]
str q3,[x5]

# qhasm: offset += step
# asm 1: add <offset=int64#3,<offset=int64#3,<step=int64#5
# asm 2: add <offset=x2,<offset=x2,<step=x4
add x2,x2,x4

# qhasm: offset - end 
# asm 1: cmp <offset=int64#3,<end=int64#4
# asm 2: cmp <offset=x2,<end=x3
cmp x2,x3

# qhasm: goto pointmul_loop if !unsigned<
b.hs ._pointmul_loop

# qhasm: return
ret
