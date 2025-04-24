
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

# qhasm: int64 pointer_delta

# qhasm: int64 pointer_fuv

# qhasm: int64 pointer_grs

# qhasm: input pointer_delta

# qhasm: input pointer_fuv

# qhasm: input pointer_grs

# qhasm: int64 delta

# qhasm: int64 fuv

# qhasm: int64 grs

# qhasm: int64 g0_and_1

# qhasm: int64 cond

# qhasm: int64 delta_tmp

# qhasm: int64 c_mask

# qhasm: int64 n_mask

# qhasm: int64 fuv_new

# qhasm: int64 grs_new

# qhasm: int64 tmp

# qhasm: int64 neg_fuv

# qhasm: int64 neg_delta

# qhasm: int64 delta_swapper

# qhasm: enter divstep
.align 4
.global _divstep
.global divstep
_divstep:
divstep:

# qhasm: delta = mem64[pointer_delta]
# asm 1: ldr >delta=int64#1, [<pointer_delta=int64#1]
# asm 2: ldr >delta=x0, [<pointer_delta=x0]
ldr x0, [x0]

# qhasm: fuv = mem64[pointer_fuv]
# asm 1: ldr >fuv=int64#2, [<pointer_fuv=int64#2]
# asm 2: ldr >fuv=x1, [<pointer_fuv=x1]
ldr x1, [x1]

# qhasm: grs = mem64[pointer_grs]
# asm 1: ldr >grs=int64#3, [<pointer_grs=int64#3]
# asm 2: ldr >grs=x2, [<pointer_grs=x2]
ldr x2, [x2]

# qhasm: g0_and_1 = grs & 1
# asm 1: and >g0_and_1=int64#4, <grs=int64#3, #1
# asm 2: and >g0_and_1=x3, <grs=x2, #1
and x3, x2, #1

# qhasm: delta - 0!
# asm 1: cmp <delta=int64#1,#0
# asm 2: cmp <delta=x0,#0
cmp x0,#0

# qhasm: c_mask = g0_and_1 if signed> else 0 
# asm 1: csel >c_mask=int64#4, <g0_and_1=int64#4, xzr, gt
# asm 2: csel >c_mask=x3, <g0_and_1=x3, xzr, gt
csel x3, x3, xzr, gt

# qhasm: c_mask = -c_mask!
# asm 1: negs >c_mask=int64#4,<c_mask=int64#4
# asm 2: negs >c_mask=x3,<c_mask=x3
negs x3,x3

# qhasm: neg_fuv = -fuv
# asm 1: neg >neg_fuv=int64#5,<fuv=int64#2
# asm 2: neg >neg_fuv=x4,<fuv=x1
neg x4,x1

# qhasm: neg_delta = -delta
# asm 1: neg >neg_delta=int64#1,<delta=int64#1
# asm 2: neg >neg_delta=x0,<delta=x0
neg x0,x0

# qhasm: fuv_new = grs if negative else fuv
# asm 1: csel >fuv_new=int64#2,<grs=int64#3,<fuv=int64#2,mi
# asm 2: csel >fuv_new=x1,<grs=x2,<fuv=x1,mi
csel x1,x2,x1,mi

# qhasm: return 
ret
