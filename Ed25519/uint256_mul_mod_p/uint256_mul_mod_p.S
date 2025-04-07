
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

# qhasm: int64 A2

# qhasm: int64 A3

# qhasm: int64 B0

# qhasm: int64 B1

# qhasm: int64 B2

# qhasm: int64 B3

# qhasm: int64 R0

# qhasm: int64 R1

# qhasm: int64 R2

# qhasm: int64 R3

# qhasm: int64 R4

# qhasm: int64 R5

# qhasm: int64 R6

# qhasm: int64 R7

# qhasm: int64 product_lo

# qhasm: int64 product_hi

# qhasm: enter uint256_mul_mod_p
.align 4
.global _uint256_mul_mod_p
.global uint256_mul_mod_p
_uint256_mul_mod_p:
uint256_mul_mod_p:

# qhasm: A0 = mem64[pointer_A]
# asm 1: ldr >A0=int64#4,[<pointer_A=int64#1]
# asm 2: ldr >A0=x3,[<pointer_A=x0]
ldr x3,[x0]

# qhasm: A1 = mem64[pointer_A + 8]
# asm 1: ldr >A1=int64#5,[<pointer_A=int64#1,#8]
# asm 2: ldr >A1=x4,[<pointer_A=x0,#8]
ldr x4,[x0,#8]

# qhasm: A2 = mem64[pointer_A + 16]
# asm 1: ldr >A2=int64#6,[<pointer_A=int64#1,#16]
# asm 2: ldr >A2=x5,[<pointer_A=x0,#16]
ldr x5,[x0,#16]

# qhasm: A3 = mem64[pointer_A + 24]
# asm 1: ldr >A3=int64#1,[<pointer_A=int64#1,#24]
# asm 2: ldr >A3=x0,[<pointer_A=x0,#24]
ldr x0,[x0,#24]

# qhasm: B0 = mem64[pointer_B]
# asm 1: ldr >B0=int64#7,[<pointer_B=int64#2]
# asm 2: ldr >B0=x6,[<pointer_B=x1]
ldr x6,[x1]

# qhasm: B1 = mem64[pointer_B + 8]
# asm 1: ldr >B1=int64#8,[<pointer_B=int64#2,#8]
# asm 2: ldr >B1=x7,[<pointer_B=x1,#8]
ldr x7,[x1,#8]

# qhasm: B2 = mem64[pointer_B + 16]
# asm 1: ldr >B2=int64#9,[<pointer_B=int64#2,#16]
# asm 2: ldr >B2=x8,[<pointer_B=x1,#16]
ldr x8,[x1,#16]

# qhasm: B3 = mem64[pointer_B + 24]
# asm 1: ldr >B3=int64#2,[<pointer_B=int64#2,#24]
# asm 2: ldr >B3=x1,[<pointer_B=x1,#24]
ldr x1,[x1,#24]

# qhasm: R0 = 0
# asm 1: mov >R0=int64#10, #0
# asm 2: mov >R0=x9, #0
mov x9, #0

# qhasm: R1 = 0
# asm 1: mov >R1=int64#11, #0
# asm 2: mov >R1=x10, #0
mov x10, #0

# qhasm: R2 = 0
# asm 1: mov >R2=int64#12, #0
# asm 2: mov >R2=x11, #0
mov x11, #0

# qhasm: R3 = 0
# asm 1: mov >R3=int64#13, #0
# asm 2: mov >R3=x12, #0
mov x12, #0

# qhasm: R4 = 0
# asm 1: mov >R4=int64#14, #0
# asm 2: mov >R4=x13, #0
mov x13, #0

# qhasm: R5 = 0
# asm 1: mov >R5=int64#15, #0
# asm 2: mov >R5=x14, #0
mov x14, #0

# qhasm: R6 = 0
# asm 1: mov >R6=int64#16, #0
# asm 2: mov >R6=x15, #0
mov x15, #0

# qhasm: R7 = 0
# asm 1: mov >R7=int64#17, #0
# asm 2: mov >R7=x16, #0
mov x16, #0

# qhasm: product_lo = A0 * B0 
# asm 1: mul >product_lo=int64#18,<A0=int64#4,<B0=int64#7
# asm 2: mul >product_lo=x17,<A0=x3,<B0=x6
mul x17,x3,x6

# qhasm: product_hi = A0 * B0 (hi)
# asm 1: umulh >product_hi=int64#19,<A0=int64#4,<B0=int64#7
# asm 2: umulh >product_hi=x18,<A0=x3,<B0=x6
umulh x18,x3,x6

# qhasm: R0 = R0 + product_lo
# asm 1: add >R0=int64#10,<R0=int64#10,<product_lo=int64#18
# asm 2: add >R0=x9,<R0=x9,<product_lo=x17
add x9,x9,x17

# qhasm: R1 = R1 + product_hi
# asm 1: add >R1=int64#11,<R1=int64#11,<product_hi=int64#19
# asm 2: add >R1=x10,<R1=x10,<product_hi=x18
add x10,x10,x18

# qhasm: product_lo = A0 * B1
# asm 1: mul >product_lo=int64#18,<A0=int64#4,<B1=int64#8
# asm 2: mul >product_lo=x17,<A0=x3,<B1=x7
mul x17,x3,x7

# qhasm: product_hi = A0 * B1 (hi)
# asm 1: umulh >product_hi=int64#19,<A0=int64#4,<B1=int64#8
# asm 2: umulh >product_hi=x18,<A0=x3,<B1=x7
umulh x18,x3,x7

# qhasm: R1 = R1 + product_lo !
# asm 1: adds >R1=int64#11,<R1=int64#11,<product_lo=int64#18
# asm 2: adds >R1=x10,<R1=x10,<product_lo=x17
adds x10,x10,x17

# qhasm: R2 = R2 + product_hi + carry !
# asm 1: adcs >R2=int64#12,<R2=int64#12,<product_hi=int64#19
# asm 2: adcs >R2=x11,<R2=x11,<product_hi=x18
adcs x11,x11,x18

# qhasm: R3 = R3 + carry !
# asm 1: adcs >R3=int64#13,<R3=int64#13, xzr
# asm 2: adcs >R3=x12,<R3=x12, xzr
adcs x12,x12, xzr

# qhasm: product_lo = A1 * B0
# asm 1: mul >product_lo=int64#18,<A1=int64#5,<B0=int64#7
# asm 2: mul >product_lo=x17,<A1=x4,<B0=x6
mul x17,x4,x6

# qhasm: product_hi = A1 * B0 (hi)
# asm 1: umulh >product_hi=int64#19,<A1=int64#5,<B0=int64#7
# asm 2: umulh >product_hi=x18,<A1=x4,<B0=x6
umulh x18,x4,x6

# qhasm: R1 = R1 + product_lo !
# asm 1: adds >R1=int64#11,<R1=int64#11,<product_lo=int64#18
# asm 2: adds >R1=x10,<R1=x10,<product_lo=x17
adds x10,x10,x17

# qhasm: R2 = R2 + product_hi + carry !
# asm 1: adcs >R2=int64#12,<R2=int64#12,<product_hi=int64#19
# asm 2: adcs >R2=x11,<R2=x11,<product_hi=x18
adcs x11,x11,x18

# qhasm: R3 = R3 + carry !
# asm 1: adcs >R3=int64#13,<R3=int64#13, xzr
# asm 2: adcs >R3=x12,<R3=x12, xzr
adcs x12,x12, xzr

# qhasm: product_lo = A0 * B2
# asm 1: mul >product_lo=int64#18,<A0=int64#4,<B2=int64#9
# asm 2: mul >product_lo=x17,<A0=x3,<B2=x8
mul x17,x3,x8

# qhasm: product_hi = A0 * B2 (hi)
# asm 1: umulh >product_hi=int64#19,<A0=int64#4,<B2=int64#9
# asm 2: umulh >product_hi=x18,<A0=x3,<B2=x8
umulh x18,x3,x8

# qhasm: R2 = R2 + product_lo !
# asm 1: adds >R2=int64#12,<R2=int64#12,<product_lo=int64#18
# asm 2: adds >R2=x11,<R2=x11,<product_lo=x17
adds x11,x11,x17

# qhasm: R3 = R3 + product_hi + carry !
# asm 1: adcs >R3=int64#13,<R3=int64#13,<product_hi=int64#19
# asm 2: adcs >R3=x12,<R3=x12,<product_hi=x18
adcs x12,x12,x18

# qhasm: R4 = R4 + carry !
# asm 1: adcs >R4=int64#14,<R4=int64#14, xzr
# asm 2: adcs >R4=x13,<R4=x13, xzr
adcs x13,x13, xzr

# qhasm: product_lo = A1 * B1
# asm 1: mul >product_lo=int64#18,<A1=int64#5,<B1=int64#8
# asm 2: mul >product_lo=x17,<A1=x4,<B1=x7
mul x17,x4,x7

# qhasm: product_hi = A1 * B1 (hi)
# asm 1: umulh >product_hi=int64#19,<A1=int64#5,<B1=int64#8
# asm 2: umulh >product_hi=x18,<A1=x4,<B1=x7
umulh x18,x4,x7

# qhasm: R2 = R2 + product_lo !
# asm 1: adds >R2=int64#12,<R2=int64#12,<product_lo=int64#18
# asm 2: adds >R2=x11,<R2=x11,<product_lo=x17
adds x11,x11,x17

# qhasm: R3 = R3 + product_hi + carry !
# asm 1: adcs >R3=int64#13,<R3=int64#13,<product_hi=int64#19
# asm 2: adcs >R3=x12,<R3=x12,<product_hi=x18
adcs x12,x12,x18

# qhasm: R4 = R4 + carry !
# asm 1: adcs >R4=int64#14,<R4=int64#14, xzr
# asm 2: adcs >R4=x13,<R4=x13, xzr
adcs x13,x13, xzr

# qhasm: product_lo = A2 * B0
# asm 1: mul >product_lo=int64#18,<A2=int64#6,<B0=int64#7
# asm 2: mul >product_lo=x17,<A2=x5,<B0=x6
mul x17,x5,x6

# qhasm: product_hi = A2 * B0 (hi)
# asm 1: umulh >product_hi=int64#19,<A2=int64#6,<B0=int64#7
# asm 2: umulh >product_hi=x18,<A2=x5,<B0=x6
umulh x18,x5,x6

# qhasm: R2 = R2 + product_lo !
# asm 1: adds >R2=int64#12,<R2=int64#12,<product_lo=int64#18
# asm 2: adds >R2=x11,<R2=x11,<product_lo=x17
adds x11,x11,x17

# qhasm: R3 = R3 + product_hi + carry !
# asm 1: adcs >R3=int64#13,<R3=int64#13,<product_hi=int64#19
# asm 2: adcs >R3=x12,<R3=x12,<product_hi=x18
adcs x12,x12,x18

# qhasm: R4 = R4 + carry !
# asm 1: adcs >R4=int64#14,<R4=int64#14, xzr
# asm 2: adcs >R4=x13,<R4=x13, xzr
adcs x13,x13, xzr

# qhasm: product_lo = A0 * B3
# asm 1: mul >product_lo=int64#18,<A0=int64#4,<B3=int64#2
# asm 2: mul >product_lo=x17,<A0=x3,<B3=x1
mul x17,x3,x1

# qhasm: product_hi = A0 * B3 (hi)
# asm 1: umulh >product_hi=int64#4,<A0=int64#4,<B3=int64#2
# asm 2: umulh >product_hi=x3,<A0=x3,<B3=x1
umulh x3,x3,x1

# qhasm: R3 = R3 + product_lo !
# asm 1: adds >R3=int64#13,<R3=int64#13,<product_lo=int64#18
# asm 2: adds >R3=x12,<R3=x12,<product_lo=x17
adds x12,x12,x17

# qhasm: R4 = R4 + product_hi + carry !
# asm 1: adcs >R4=int64#4,<R4=int64#14,<product_hi=int64#4
# asm 2: adcs >R4=x3,<R4=x13,<product_hi=x3
adcs x3,x13,x3

# qhasm: R5 = R5 + carry !
# asm 1: adcs >R5=int64#14,<R5=int64#15, xzr
# asm 2: adcs >R5=x13,<R5=x14, xzr
adcs x13,x14, xzr

# qhasm: product_lo = A1 * B2
# asm 1: mul >product_lo=int64#15,<A1=int64#5,<B2=int64#9
# asm 2: mul >product_lo=x14,<A1=x4,<B2=x8
mul x14,x4,x8

# qhasm: product_hi = A1 * B2 (hi)
# asm 1: umulh >product_hi=int64#18,<A1=int64#5,<B2=int64#9
# asm 2: umulh >product_hi=x17,<A1=x4,<B2=x8
umulh x17,x4,x8

# qhasm: R3 = R3 + product_lo !
# asm 1: adds >R3=int64#13,<R3=int64#13,<product_lo=int64#15
# asm 2: adds >R3=x12,<R3=x12,<product_lo=x14
adds x12,x12,x14

# qhasm: R4 = R4 + product_hi + carry !
# asm 1: adcs >R4=int64#4,<R4=int64#4,<product_hi=int64#18
# asm 2: adcs >R4=x3,<R4=x3,<product_hi=x17
adcs x3,x3,x17

# qhasm: R5 = R5 + carry !
# asm 1: adcs >R5=int64#14,<R5=int64#14, xzr
# asm 2: adcs >R5=x13,<R5=x13, xzr
adcs x13,x13, xzr

# qhasm: product_lo = A2 * B1
# asm 1: mul >product_lo=int64#15,<A2=int64#6,<B1=int64#8
# asm 2: mul >product_lo=x14,<A2=x5,<B1=x7
mul x14,x5,x7

# qhasm: product_hi = A2 * B1 (hi)
# asm 1: umulh >product_hi=int64#18,<A2=int64#6,<B1=int64#8
# asm 2: umulh >product_hi=x17,<A2=x5,<B1=x7
umulh x17,x5,x7

# qhasm: R3 = R3 + product_lo !
# asm 1: adds >R3=int64#13,<R3=int64#13,<product_lo=int64#15
# asm 2: adds >R3=x12,<R3=x12,<product_lo=x14
adds x12,x12,x14

# qhasm: R4 = R4 + product_hi + carry !
# asm 1: adcs >R4=int64#4,<R4=int64#4,<product_hi=int64#18
# asm 2: adcs >R4=x3,<R4=x3,<product_hi=x17
adcs x3,x3,x17

# qhasm: R5 = R5 + carry !
# asm 1: adcs >R5=int64#14,<R5=int64#14, xzr
# asm 2: adcs >R5=x13,<R5=x13, xzr
adcs x13,x13, xzr

# qhasm: product_lo = A3 * B0
# asm 1: mul >product_lo=int64#15,<A3=int64#1,<B0=int64#7
# asm 2: mul >product_lo=x14,<A3=x0,<B0=x6
mul x14,x0,x6

# qhasm: product_hi = A3 * B0 (hi)
# asm 1: umulh >product_hi=int64#7,<A3=int64#1,<B0=int64#7
# asm 2: umulh >product_hi=x6,<A3=x0,<B0=x6
umulh x6,x0,x6

# qhasm: R3 = R3 + product_lo !
# asm 1: adds >R3=int64#13,<R3=int64#13,<product_lo=int64#15
# asm 2: adds >R3=x12,<R3=x12,<product_lo=x14
adds x12,x12,x14

# qhasm: R4 = R4 + product_hi + carry !
# asm 1: adcs >R4=int64#4,<R4=int64#4,<product_hi=int64#7
# asm 2: adcs >R4=x3,<R4=x3,<product_hi=x6
adcs x3,x3,x6

# qhasm: R5 = R5 + carry !
# asm 1: adcs >R5=int64#7,<R5=int64#14, xzr
# asm 2: adcs >R5=x6,<R5=x13, xzr
adcs x6,x13, xzr

# qhasm: product_lo = A1 * B3
# asm 1: mul >product_lo=int64#14,<A1=int64#5,<B3=int64#2
# asm 2: mul >product_lo=x13,<A1=x4,<B3=x1
mul x13,x4,x1

# qhasm: product_hi = A1 * B3 (hi)
# asm 1: umulh >product_hi=int64#5,<A1=int64#5,<B3=int64#2
# asm 2: umulh >product_hi=x4,<A1=x4,<B3=x1
umulh x4,x4,x1

# qhasm: R4 = R4 + product_lo !
# asm 1: adds >R4=int64#4,<R4=int64#4,<product_lo=int64#14
# asm 2: adds >R4=x3,<R4=x3,<product_lo=x13
adds x3,x3,x13

# qhasm: R5 = R5 + product_hi + carry !
# asm 1: adcs >R5=int64#5,<R5=int64#7,<product_hi=int64#5
# asm 2: adcs >R5=x4,<R5=x6,<product_hi=x4
adcs x4,x6,x4

# qhasm: R6 = R6 + carry !
# asm 1: adcs >R6=int64#7,<R6=int64#16, xzr
# asm 2: adcs >R6=x6,<R6=x15, xzr
adcs x6,x15, xzr

# qhasm: product_lo = A2 * B2
# asm 1: mul >product_lo=int64#14,<A2=int64#6,<B2=int64#9
# asm 2: mul >product_lo=x13,<A2=x5,<B2=x8
mul x13,x5,x8

# qhasm: product_hi = A2 * B2 (hi)
# asm 1: umulh >product_hi=int64#15,<A2=int64#6,<B2=int64#9
# asm 2: umulh >product_hi=x14,<A2=x5,<B2=x8
umulh x14,x5,x8

# qhasm: R4 = R4 + product_lo !
# asm 1: adds >R4=int64#4,<R4=int64#4,<product_lo=int64#14
# asm 2: adds >R4=x3,<R4=x3,<product_lo=x13
adds x3,x3,x13

# qhasm: R5 = R5 + product_hi + carry !
# asm 1: adcs >R5=int64#5,<R5=int64#5,<product_hi=int64#15
# asm 2: adcs >R5=x4,<R5=x4,<product_hi=x14
adcs x4,x4,x14

# qhasm: R6 = R6 + carry !
# asm 1: adcs >R6=int64#7,<R6=int64#7, xzr
# asm 2: adcs >R6=x6,<R6=x6, xzr
adcs x6,x6, xzr

# qhasm: product_lo = A3 * B1
# asm 1: mul >product_lo=int64#14,<A3=int64#1,<B1=int64#8
# asm 2: mul >product_lo=x13,<A3=x0,<B1=x7
mul x13,x0,x7

# qhasm: product_hi = A3 * B1 (hi)
# asm 1: umulh >product_hi=int64#8,<A3=int64#1,<B1=int64#8
# asm 2: umulh >product_hi=x7,<A3=x0,<B1=x7
umulh x7,x0,x7

# qhasm: R4 = R4 + product_lo !
# asm 1: adds >R4=int64#4,<R4=int64#4,<product_lo=int64#14
# asm 2: adds >R4=x3,<R4=x3,<product_lo=x13
adds x3,x3,x13

# qhasm: R5 = R5 + product_hi + carry !
# asm 1: adcs >R5=int64#5,<R5=int64#5,<product_hi=int64#8
# asm 2: adcs >R5=x4,<R5=x4,<product_hi=x7
adcs x4,x4,x7

# qhasm: R6 = R6 + carry !
# asm 1: adcs >R6=int64#7,<R6=int64#7, xzr
# asm 2: adcs >R6=x6,<R6=x6, xzr
adcs x6,x6, xzr

# qhasm: product_lo = A2 * B3
# asm 1: mul >product_lo=int64#8,<A2=int64#6,<B3=int64#2
# asm 2: mul >product_lo=x7,<A2=x5,<B3=x1
mul x7,x5,x1

# qhasm: product_hi = A2 * B3 (hi)
# asm 1: umulh >product_hi=int64#6,<A2=int64#6,<B3=int64#2
# asm 2: umulh >product_hi=x5,<A2=x5,<B3=x1
umulh x5,x5,x1

# qhasm: R5 = R5 + product_lo !
# asm 1: adds >R5=int64#5,<R5=int64#5,<product_lo=int64#8
# asm 2: adds >R5=x4,<R5=x4,<product_lo=x7
adds x4,x4,x7

# qhasm: R6 = R6 + product_hi + carry !
# asm 1: adcs >R6=int64#6,<R6=int64#7,<product_hi=int64#6
# asm 2: adcs >R6=x5,<R6=x6,<product_hi=x5
adcs x5,x6,x5

# qhasm: R7 = R7 + carry !
# asm 1: adcs >R7=int64#7,<R7=int64#17, xzr
# asm 2: adcs >R7=x6,<R7=x16, xzr
adcs x6,x16, xzr

# qhasm: product_lo = A3 * B2
# asm 1: mul >product_lo=int64#8,<A3=int64#1,<B2=int64#9
# asm 2: mul >product_lo=x7,<A3=x0,<B2=x8
mul x7,x0,x8

# qhasm: product_hi = A3 * B2 (hi)
# asm 1: umulh >product_hi=int64#9,<A3=int64#1,<B2=int64#9
# asm 2: umulh >product_hi=x8,<A3=x0,<B2=x8
umulh x8,x0,x8

# qhasm: R5 = R5 + product_lo !
# asm 1: adds >R5=int64#5,<R5=int64#5,<product_lo=int64#8
# asm 2: adds >R5=x4,<R5=x4,<product_lo=x7
adds x4,x4,x7

# qhasm: R6 = R6 + product_hi + carry !
# asm 1: adcs >R6=int64#6,<R6=int64#6,<product_hi=int64#9
# asm 2: adcs >R6=x5,<R6=x5,<product_hi=x8
adcs x5,x5,x8

# qhasm: R7 = R7 + carry !
# asm 1: adcs >R7=int64#7,<R7=int64#7, xzr
# asm 2: adcs >R7=x6,<R7=x6, xzr
adcs x6,x6, xzr

# qhasm: product_lo = A3 * B3
# asm 1: mul >product_lo=int64#8,<A3=int64#1,<B3=int64#2
# asm 2: mul >product_lo=x7,<A3=x0,<B3=x1
mul x7,x0,x1

# qhasm: product_hi = A3 * B3 (hi)
# asm 1: umulh >product_hi=int64#1,<A3=int64#1,<B3=int64#2
# asm 2: umulh >product_hi=x0,<A3=x0,<B3=x1
umulh x0,x0,x1

# qhasm: R6 = R6 + product_lo !
# asm 1: adds >R6=int64#2,<R6=int64#6,<product_lo=int64#8
# asm 2: adds >R6=x1,<R6=x5,<product_lo=x7
adds x1,x5,x7

# qhasm: R7 = R7 + product_hi + carry !
# asm 1: adcs >R7=int64#1,<R7=int64#7,<product_hi=int64#1
# asm 2: adcs >R7=x0,<R7=x6,<product_hi=x0
adcs x0,x6,x0

# qhasm: mem64[pointer_R] = R0
# asm 1: str <R0=int64#10,[<pointer_R=int64#3]
# asm 2: str <R0=x9,[<pointer_R=x2]
str x9,[x2]

# qhasm: mem64[pointer_R +  8] = R1
# asm 1: str <R1=int64#11,[<pointer_R=int64#3,#8]
# asm 2: str <R1=x10,[<pointer_R=x2,#8]
str x10,[x2,#8]

# qhasm: mem64[pointer_R + 16] = R2
# asm 1: str <R2=int64#12,[<pointer_R=int64#3,#16]
# asm 2: str <R2=x11,[<pointer_R=x2,#16]
str x11,[x2,#16]

# qhasm: mem64[pointer_R + 24] = R3
# asm 1: str <R3=int64#13,[<pointer_R=int64#3,#24]
# asm 2: str <R3=x12,[<pointer_R=x2,#24]
str x12,[x2,#24]

# qhasm: mem64[pointer_R + 32] = R4
# asm 1: str <R4=int64#4,[<pointer_R=int64#3,#32]
# asm 2: str <R4=x3,[<pointer_R=x2,#32]
str x3,[x2,#32]

# qhasm: mem64[pointer_R + 40] = R5
# asm 1: str <R5=int64#5,[<pointer_R=int64#3,#40]
# asm 2: str <R5=x4,[<pointer_R=x2,#40]
str x4,[x2,#40]

# qhasm: mem64[pointer_R + 48] = R6
# asm 1: str <R6=int64#2,[<pointer_R=int64#3,#48]
# asm 2: str <R6=x1,[<pointer_R=x2,#48]
str x1,[x2,#48]

# qhasm: mem64[pointer_R + 56] = R7
# asm 1: str <R7=int64#1,[<pointer_R=int64#3,#56]
# asm 2: str <R7=x0,[<pointer_R=x2,#56]
str x0,[x2,#56]

# qhasm: return
ret
