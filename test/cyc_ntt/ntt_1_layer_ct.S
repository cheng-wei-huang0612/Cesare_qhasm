
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

# qhasm: int64 pointer_a

# qhasm: int64 pointer_b

# qhasm: int64 omega

# qhasm: int64 temp_a

# qhasm: int64 temp_b

# qhasm: int64 temp_mul

# qhasm: int64 out_a

# qhasm: int64 out_b

# qhasm: input pointer_a

# qhasm: input pointer_b

# qhasm: input omega

# qhasm: enter ntt_1_layer_ct
.align 4
.global _ntt_1_layer_ct
.global ntt_1_layer_ct
_ntt_1_layer_ct:
ntt_1_layer_ct:

# qhasm: temp_a = mem64[pointer_a+0]
# asm 1: ldr >temp_a=int64#4,[<pointer_a=int64#1,#0]
# asm 2: ldr >temp_a=x3,[<pointer_a=x0,#0]
ldr x3,[x0,#0]

# qhasm: temp_b = mem64[pointer_b+0]
# asm 1: ldr >temp_b=int64#5,[<pointer_b=int64#2,#0]
# asm 2: ldr >temp_b=x4,[<pointer_b=x1,#0]
ldr x4,[x1,#0]

# qhasm: temp_mul = omega * temp_b
# asm 1: mul >temp_mul=int64#3,<omega=int64#3,<temp_b=int64#5
# asm 2: mul >temp_mul=x2,<omega=x2,<temp_b=x4
mul x2,x2,x4

# qhasm: out_a = temp_a + temp_mul
# asm 1: add >out_a=int64#5,<temp_a=int64#4,<temp_mul=int64#3
# asm 2: add >out_a=x4,<temp_a=x3,<temp_mul=x2
add x4,x3,x2

# qhasm: out_b = temp_a - temp_mul
# asm 1: sub >out_b=int64#3,<temp_a=int64#4,<temp_mul=int64#3
# asm 2: sub >out_b=x2,<temp_a=x3,<temp_mul=x2
sub x2,x3,x2

# qhasm: mem64[pointer_a+0] = out_a
# asm 1: str <out_a=int64#5,[<pointer_a=int64#1,#0]
# asm 2: str <out_a=x4,[<pointer_a=x0,#0]
str x4,[x0,#0]

# qhasm: mem64[pointer_b+0] = out_b
# asm 1: str <out_b=int64#3,[<pointer_b=int64#2,#0]
# asm 2: str <out_b=x2,[<pointer_b=x1,#0]
str x2,[x1,#0]

# qhasm: return
ret
