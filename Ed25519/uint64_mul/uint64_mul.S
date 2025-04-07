
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

# qhasm: int64 pointer_A

# qhasm: int64 pointer_B

# qhasm: int64 pointer_R

# qhasm: input pointer_A

# qhasm: input pointer_B

# qhasm: input pointer_R

# qhasm: int64 A0

# qhasm: int64 B0

# qhasm: int64 R0

# qhasm: int64 R1

# qhasm: int64 product_lo

# qhasm: int64 product_hi

# qhasm: enter uint64_mul
.align 4
.global _uint64_mul
.global uint64_mul
_uint64_mul:
uint64_mul:

# qhasm: A0 = mem64[pointer_A]
# asm 1: ldr >A0=int64#1,[<pointer_A=int64#1]
# asm 2: ldr >A0=x0,[<pointer_A=x0]
ldr x0,[x0]

# qhasm: B0 = mem64[pointer_B]
# asm 1: ldr >B0=int64#2,[<pointer_B=int64#2]
# asm 2: ldr >B0=x1,[<pointer_B=x1]
ldr x1,[x1]

# qhasm: R0 = 0
# asm 1: mov >R0=int64#4, #0
# asm 2: mov >R0=x3, #0
mov x3, #0

# qhasm: R1 = 0
# asm 1: mov >R1=int64#5, #0
# asm 2: mov >R1=x4, #0
mov x4, #0

# qhasm: product_lo = A0 * B0
# asm 1: mul >product_lo=int64#6,<A0=int64#1,<B0=int64#2
# asm 2: mul >product_lo=x5,<A0=x0,<B0=x1
mul x5,x0,x1

# qhasm: product_hi = A0 * B0 (hi)
# asm 1: umulh >product_hi=int64#1,<A0=int64#1,<B0=int64#2
# asm 2: umulh >product_hi=x0,<A0=x0,<B0=x1
umulh x0,x0,x1

# qhasm: R0 = R0 + product_lo !
# asm 1: adds >R0=int64#2,<R0=int64#4,<product_lo=int64#6
# asm 2: adds >R0=x1,<R0=x3,<product_lo=x5
adds x1,x3,x5

# qhasm: R1 = R1 + product_hi + carry !
# asm 1: adcs >R1=int64#1,<R1=int64#5,<product_hi=int64#1
# asm 2: adcs >R1=x0,<R1=x4,<product_hi=x0
adcs x0,x4,x0

# qhasm: mem64[pointer_R] = R0
# asm 1: str <R0=int64#2,[<pointer_R=int64#3]
# asm 2: str <R0=x1,[<pointer_R=x2]
str x1,[x2]

# qhasm: mem64[pointer_R +  8] = R1
# asm 1: str <R1=int64#1,[<pointer_R=int64#3,#8]
# asm 2: str <R1=x0,[<pointer_R=x2,#8]
str x0,[x2,#8]

# qhasm: return
ret
