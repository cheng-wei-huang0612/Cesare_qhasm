
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

# qhasm: int64 A1

# qhasm: int64 B0

# qhasm: int64 B1

# qhasm: int64 R0

# qhasm: int64 R1

# qhasm: int64 R2

# qhasm: int64 R3

# qhasm: int64 product_lo

# qhasm: int64 product_hi

# qhasm: enter uint128_mul
.align 4
.global _uint128_mul
.global uint128_mul
_uint128_mul:
uint128_mul:

# qhasm: A0 = mem64[pointer_A]
# asm 1: ldr >A0=int64#4,[<pointer_A=int64#1]
# asm 2: ldr >A0=x3,[<pointer_A=x0]
ldr x3,[x0]

# qhasm: A1 = mem64[pointer_A + 8]
# asm 1: ldr >A1=int64#1,[<pointer_A=int64#1,#8]
# asm 2: ldr >A1=x0,[<pointer_A=x0,#8]
ldr x0,[x0,#8]

# qhasm: B0 = mem64[pointer_B]
# asm 1: ldr >B0=int64#5,[<pointer_B=int64#2]
# asm 2: ldr >B0=x4,[<pointer_B=x1]
ldr x4,[x1]

# qhasm: B1 = mem64[pointer_B + 8]
# asm 1: ldr >B1=int64#2,[<pointer_B=int64#2,#8]
# asm 2: ldr >B1=x1,[<pointer_B=x1,#8]
ldr x1,[x1,#8]

# qhasm: R0 = 0
# asm 1: mov >R0=int64#6, #0
# asm 2: mov >R0=x5, #0
mov x5, #0

# qhasm: R1 = 0
# asm 1: mov >R1=int64#7, #0
# asm 2: mov >R1=x6, #0
mov x6, #0

# qhasm: R2 = 0
# asm 1: mov >R2=int64#8, #0
# asm 2: mov >R2=x7, #0
mov x7, #0

# qhasm: R3 = 0
# asm 1: mov >R3=int64#9, #0
# asm 2: mov >R3=x8, #0
mov x8, #0

# qhasm: product_lo = A0 * B0
# asm 1: mul >product_lo=int64#10,<A0=int64#4,<B0=int64#5
# asm 2: mul >product_lo=x9,<A0=x3,<B0=x4
mul x9,x3,x4

# qhasm: product_hi = A0 * B0 (hi)
# asm 1: umulh >product_hi=int64#11,<A0=int64#4,<B0=int64#5
# asm 2: umulh >product_hi=x10,<A0=x3,<B0=x4
umulh x10,x3,x4

# qhasm: R0 = R0 + product_lo !
# asm 1: adds >R0=int64#6,<R0=int64#6,<product_lo=int64#10
# asm 2: adds >R0=x5,<R0=x5,<product_lo=x9
adds x5,x5,x9

# qhasm: R1 = R1 + product_hi + carry !
# asm 1: adcs >R1=int64#7,<R1=int64#7,<product_hi=int64#11
# asm 2: adcs >R1=x6,<R1=x6,<product_hi=x10
adcs x6,x6,x10

# qhasm: R2 = R2 + carry !
# asm 1: adcs >R2=int64#8,<R2=int64#8, xzr
# asm 2: adcs >R2=x7,<R2=x7, xzr
adcs x7,x7, xzr

# qhasm: product_lo = A0 * B1
# asm 1: mul >product_lo=int64#10,<A0=int64#4,<B1=int64#2
# asm 2: mul >product_lo=x9,<A0=x3,<B1=x1
mul x9,x3,x1

# qhasm: product_hi = A0 * B1 (hi)
# asm 1: umulh >product_hi=int64#4,<A0=int64#4,<B1=int64#2
# asm 2: umulh >product_hi=x3,<A0=x3,<B1=x1
umulh x3,x3,x1

# qhasm: R1 = R1 + product_lo !
# asm 1: adds >R1=int64#7,<R1=int64#7,<product_lo=int64#10
# asm 2: adds >R1=x6,<R1=x6,<product_lo=x9
adds x6,x6,x9

# qhasm: R2 = R2 + product_hi + carry !
# asm 1: adcs >R2=int64#4,<R2=int64#8,<product_hi=int64#4
# asm 2: adcs >R2=x3,<R2=x7,<product_hi=x3
adcs x3,x7,x3

# qhasm: R3 = R3 + carry !
# asm 1: adcs >R3=int64#8,<R3=int64#9, xzr
# asm 2: adcs >R3=x7,<R3=x8, xzr
adcs x7,x8, xzr

# qhasm: product_lo = A1 * B0
# asm 1: mul >product_lo=int64#9,<A1=int64#1,<B0=int64#5
# asm 2: mul >product_lo=x8,<A1=x0,<B0=x4
mul x8,x0,x4

# qhasm: product_hi = A1 * B0 (hi)
# asm 1: umulh >product_hi=int64#5,<A1=int64#1,<B0=int64#5
# asm 2: umulh >product_hi=x4,<A1=x0,<B0=x4
umulh x4,x0,x4

# qhasm: R1 = R1 + product_lo !
# asm 1: adds >R1=int64#7,<R1=int64#7,<product_lo=int64#9
# asm 2: adds >R1=x6,<R1=x6,<product_lo=x8
adds x6,x6,x8

# qhasm: R2 = R2 + product_hi + carry !
# asm 1: adcs >R2=int64#4,<R2=int64#4,<product_hi=int64#5
# asm 2: adcs >R2=x3,<R2=x3,<product_hi=x4
adcs x3,x3,x4

# qhasm: R3 = R3 + carry !
# asm 1: adcs >R3=int64#5,<R3=int64#8, xzr
# asm 2: adcs >R3=x4,<R3=x7, xzr
adcs x4,x7, xzr

# qhasm: product_lo = A1 * B1
# asm 1: mul >product_lo=int64#8,<A1=int64#1,<B1=int64#2
# asm 2: mul >product_lo=x7,<A1=x0,<B1=x1
mul x7,x0,x1

# qhasm: product_hi = A1 * B1 (hi)
# asm 1: umulh >product_hi=int64#1,<A1=int64#1,<B1=int64#2
# asm 2: umulh >product_hi=x0,<A1=x0,<B1=x1
umulh x0,x0,x1

# qhasm: R2 = R2 + product_lo !
# asm 1: adds >R2=int64#2,<R2=int64#4,<product_lo=int64#8
# asm 2: adds >R2=x1,<R2=x3,<product_lo=x7
adds x1,x3,x7

# qhasm: R3 = R3 + product_hi + carry !
# asm 1: adcs >R3=int64#1,<R3=int64#5,<product_hi=int64#1
# asm 2: adcs >R3=x0,<R3=x4,<product_hi=x0
adcs x0,x4,x0

# qhasm: mem64[pointer_R] = R0
# asm 1: str <R0=int64#6,[<pointer_R=int64#3]
# asm 2: str <R0=x5,[<pointer_R=x2]
str x5,[x2]

# qhasm: mem64[pointer_R +  8] = R1
# asm 1: str <R1=int64#7,[<pointer_R=int64#3,#8]
# asm 2: str <R1=x6,[<pointer_R=x2,#8]
str x6,[x2,#8]

# qhasm: mem64[pointer_R + 16] = R2
# asm 1: str <R2=int64#2,[<pointer_R=int64#3,#16]
# asm 2: str <R2=x1,[<pointer_R=x2,#16]
str x1,[x2,#16]

# qhasm: mem64[pointer_R + 24] = R3
# asm 1: str <R3=int64#1,[<pointer_R=int64#3,#24]
# asm 2: str <R3=x0,[<pointer_R=x2,#24]
str x0,[x2,#24]

# qhasm: return
ret
