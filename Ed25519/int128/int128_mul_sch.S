
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

# qhasm: int64 A_lo

# qhasm: int64 A_hi

# qhasm: int64 B_lo

# qhasm: int64 B_hi

# qhasm: int64 sign_A

# qhasm: int64 sign_B

# qhasm: int64 mask_A

# qhasm: int64 mask_B

# qhasm: int64 r0

# qhasm: int64 r1

# qhasm: int64 r2

# qhasm: int64 r3

# qhasm: int64 sign_R

# qhasm: int64 mask_R

# qhasm: int64 product_lo

# qhasm: int64 product_hi

# qhasm: enter int128_mul_sch
.align 4
.global _int128_mul_sch
.global int128_mul_sch
_int128_mul_sch:
int128_mul_sch:

# qhasm: A_lo = mem64[pointer_A]
# asm 1: ldr >A_lo=int64#4,[<pointer_A=int64#1]
# asm 2: ldr >A_lo=x3,[<pointer_A=x0]
ldr x3,[x0]

# qhasm: A_hi = mem64[pointer_A + 8]
# asm 1: ldr >A_hi=int64#1,[<pointer_A=int64#1,#8]
# asm 2: ldr >A_hi=x0,[<pointer_A=x0,#8]
ldr x0,[x0,#8]

# qhasm: B_lo = mem64[pointer_B]
# asm 1: ldr >B_lo=int64#5,[<pointer_B=int64#2]
# asm 2: ldr >B_lo=x4,[<pointer_B=x1]
ldr x4,[x1]

# qhasm: B_hi = mem64[pointer_B + 8]
# asm 1: ldr >B_hi=int64#2,[<pointer_B=int64#2,#8]
# asm 2: ldr >B_hi=x1,[<pointer_B=x1,#8]
ldr x1,[x1,#8]

# qhasm: sign_A = A_hi >> 63
# asm 1: lsr >sign_A=int64#6,<A_hi=int64#1,#63
# asm 2: lsr >sign_A=x5,<A_hi=x0,#63
lsr x5,x0,#63

# qhasm: sign_B = B_hi >> 63
# asm 1: lsr >sign_B=int64#7,<B_hi=int64#2,#63
# asm 2: lsr >sign_B=x6,<B_hi=x1,#63
lsr x6,x1,#63

# qhasm: mask_A = - sign_A
# asm 1: neg >mask_A=int64#8,<sign_A=int64#6
# asm 2: neg >mask_A=x7,<sign_A=x5
neg x7,x5

# qhasm: A_lo ^= mask_A
# asm 1: eor >A_lo=int64#4,<A_lo=int64#4,<mask_A=int64#8
# asm 2: eor >A_lo=x3,<A_lo=x3,<mask_A=x7
eor x3,x3,x7

# qhasm: A_hi ^= mask_A
# asm 1: eor >A_hi=int64#1,<A_hi=int64#1,<mask_A=int64#8
# asm 2: eor >A_hi=x0,<A_hi=x0,<mask_A=x7
eor x0,x0,x7

# qhasm: A_lo = A_lo + sign_A!
# asm 1: adds >A_lo=int64#4,<A_lo=int64#4,<sign_A=int64#6
# asm 2: adds >A_lo=x3,<A_lo=x3,<sign_A=x5
adds x3,x3,x5

# qhasm: A_hi = A_hi + carry !
# asm 1: adcs >A_hi=int64#1,<A_hi=int64#1, xzr
# asm 2: adcs >A_hi=x0,<A_hi=x0, xzr
adcs x0,x0, xzr

# qhasm: mask_B = - sign_B
# asm 1: neg >mask_B=int64#8,<sign_B=int64#7
# asm 2: neg >mask_B=x7,<sign_B=x6
neg x7,x6

# qhasm: B_lo ^= mask_B
# asm 1: eor >B_lo=int64#5,<B_lo=int64#5,<mask_B=int64#8
# asm 2: eor >B_lo=x4,<B_lo=x4,<mask_B=x7
eor x4,x4,x7

# qhasm: B_hi ^= mask_B
# asm 1: eor >B_hi=int64#2,<B_hi=int64#2,<mask_B=int64#8
# asm 2: eor >B_hi=x1,<B_hi=x1,<mask_B=x7
eor x1,x1,x7

# qhasm: B_lo = B_lo + sign_B!
# asm 1: adds >B_lo=int64#5,<B_lo=int64#5,<sign_B=int64#7
# asm 2: adds >B_lo=x4,<B_lo=x4,<sign_B=x6
adds x4,x4,x6

# qhasm: B_hi = B_hi + carry !
# asm 1: adcs >B_hi=int64#2,<B_hi=int64#2, xzr
# asm 2: adcs >B_hi=x1,<B_hi=x1, xzr
adcs x1,x1, xzr

# qhasm: sign_R = sign_A ^ sign_B
# asm 1: eor >sign_R=int64#6,<sign_A=int64#6,<sign_B=int64#7
# asm 2: eor >sign_R=x5,<sign_A=x5,<sign_B=x6
eor x5,x5,x6

# qhasm: r0 = 0
# asm 1: mov >r0=int64#7, #0
# asm 2: mov >r0=x6, #0
mov x6, #0

# qhasm: r1 = 0
# asm 1: mov >r1=int64#8, #0
# asm 2: mov >r1=x7, #0
mov x7, #0

# qhasm: r2 = 0
# asm 1: mov >r2=int64#9, #0
# asm 2: mov >r2=x8, #0
mov x8, #0

# qhasm: r3 = 0
# asm 1: mov >r3=int64#10, #0
# asm 2: mov >r3=x9, #0
mov x9, #0

# qhasm: product_lo = A_lo * B_lo
# asm 1: mul >product_lo=int64#11,<A_lo=int64#4,<B_lo=int64#5
# asm 2: mul >product_lo=x10,<A_lo=x3,<B_lo=x4
mul x10,x3,x4

# qhasm: product_hi = A_lo * B_lo (hi)
# asm 1: umulh >product_hi=int64#12,<A_lo=int64#4,<B_lo=int64#5
# asm 2: umulh >product_hi=x11,<A_lo=x3,<B_lo=x4
umulh x11,x3,x4

# qhasm: r0 = r0 + product_lo !
# asm 1: adds >r0=int64#7,<r0=int64#7,<product_lo=int64#11
# asm 2: adds >r0=x6,<r0=x6,<product_lo=x10
adds x6,x6,x10

# qhasm: r1 = r1 + product_hi + carry !
# asm 1: adcs >r1=int64#8,<r1=int64#8,<product_hi=int64#12
# asm 2: adcs >r1=x7,<r1=x7,<product_hi=x11
adcs x7,x7,x11

# qhasm: product_lo = A_lo * B_hi
# asm 1: mul >product_lo=int64#11,<A_lo=int64#4,<B_hi=int64#2
# asm 2: mul >product_lo=x10,<A_lo=x3,<B_hi=x1
mul x10,x3,x1

# qhasm: product_hi = A_lo * B_hi (hi)
# asm 1: umulh >product_hi=int64#4,<A_lo=int64#4,<B_hi=int64#2
# asm 2: umulh >product_hi=x3,<A_lo=x3,<B_hi=x1
umulh x3,x3,x1

# qhasm: r1 = r1 + product_lo !
# asm 1: adds >r1=int64#8,<r1=int64#8,<product_lo=int64#11
# asm 2: adds >r1=x7,<r1=x7,<product_lo=x10
adds x7,x7,x10

# qhasm: r2 = r2 + product_hi + carry !
# asm 1: adcs >r2=int64#4,<r2=int64#9,<product_hi=int64#4
# asm 2: adcs >r2=x3,<r2=x8,<product_hi=x3
adcs x3,x8,x3

# qhasm: r3 = r3 + carry !
# asm 1: adcs >r3=int64#9,<r3=int64#10, xzr
# asm 2: adcs >r3=x8,<r3=x9, xzr
adcs x8,x9, xzr

# qhasm: product_lo = A_hi * B_lo
# asm 1: mul >product_lo=int64#10,<A_hi=int64#1,<B_lo=int64#5
# asm 2: mul >product_lo=x9,<A_hi=x0,<B_lo=x4
mul x9,x0,x4

# qhasm: product_hi = A_hi * B_lo (hi)
# asm 1: umulh >product_hi=int64#5,<A_hi=int64#1,<B_lo=int64#5
# asm 2: umulh >product_hi=x4,<A_hi=x0,<B_lo=x4
umulh x4,x0,x4

# qhasm: r1 = r1 + product_lo !
# asm 1: adds >r1=int64#8,<r1=int64#8,<product_lo=int64#10
# asm 2: adds >r1=x7,<r1=x7,<product_lo=x9
adds x7,x7,x9

# qhasm: r2 = r2 + product_hi + carry !
# asm 1: adcs >r2=int64#4,<r2=int64#4,<product_hi=int64#5
# asm 2: adcs >r2=x3,<r2=x3,<product_hi=x4
adcs x3,x3,x4

# qhasm: r3 = r3 + carry !
# asm 1: adcs >r3=int64#5,<r3=int64#9, xzr
# asm 2: adcs >r3=x4,<r3=x8, xzr
adcs x4,x8, xzr

# qhasm: product_lo = A_hi * B_hi
# asm 1: mul >product_lo=int64#9,<A_hi=int64#1,<B_hi=int64#2
# asm 2: mul >product_lo=x8,<A_hi=x0,<B_hi=x1
mul x8,x0,x1

# qhasm: product_hi = A_hi * B_hi (hi)
# asm 1: umulh >product_hi=int64#1,<A_hi=int64#1,<B_hi=int64#2
# asm 2: umulh >product_hi=x0,<A_hi=x0,<B_hi=x1
umulh x0,x0,x1

# qhasm: r2 = r2 + product_lo !
# asm 1: adds >r2=int64#2,<r2=int64#4,<product_lo=int64#9
# asm 2: adds >r2=x1,<r2=x3,<product_lo=x8
adds x1,x3,x8

# qhasm: r3 = r3 + product_hi + carry !
# asm 1: adcs >r3=int64#1,<r3=int64#5,<product_hi=int64#1
# asm 2: adcs >r3=x0,<r3=x4,<product_hi=x0
adcs x0,x4,x0

# qhasm: mask_R = - sign_R
# asm 1: neg >mask_R=int64#4,<sign_R=int64#6
# asm 2: neg >mask_R=x3,<sign_R=x5
neg x3,x5

# qhasm: r0 ^= mask_R
# asm 1: eor >r0=int64#5,<r0=int64#7,<mask_R=int64#4
# asm 2: eor >r0=x4,<r0=x6,<mask_R=x3
eor x4,x6,x3

# qhasm: r1 ^= mask_R
# asm 1: eor >r1=int64#7,<r1=int64#8,<mask_R=int64#4
# asm 2: eor >r1=x6,<r1=x7,<mask_R=x3
eor x6,x7,x3

# qhasm: r2 ^= mask_R
# asm 1: eor >r2=int64#2,<r2=int64#2,<mask_R=int64#4
# asm 2: eor >r2=x1,<r2=x1,<mask_R=x3
eor x1,x1,x3

# qhasm: r3 ^= mask_R
# asm 1: eor >r3=int64#1,<r3=int64#1,<mask_R=int64#4
# asm 2: eor >r3=x0,<r3=x0,<mask_R=x3
eor x0,x0,x3

# qhasm: r0 = r0 + sign_R!
# asm 1: adds >r0=int64#4,<r0=int64#5,<sign_R=int64#6
# asm 2: adds >r0=x3,<r0=x4,<sign_R=x5
adds x3,x4,x5

# qhasm: r1 = r1 + carry !
# asm 1: adcs >r1=int64#5,<r1=int64#7, xzr
# asm 2: adcs >r1=x4,<r1=x6, xzr
adcs x4,x6, xzr

# qhasm: r2 = r2 + carry !
# asm 1: adcs >r2=int64#2,<r2=int64#2, xzr
# asm 2: adcs >r2=x1,<r2=x1, xzr
adcs x1,x1, xzr

# qhasm: r3 = r3 + carry !
# asm 1: adcs >r3=int64#1,<r3=int64#1, xzr
# asm 2: adcs >r3=x0,<r3=x0, xzr
adcs x0,x0, xzr

# qhasm: mem64[pointer_R] = r0
# asm 1: str <r0=int64#4,[<pointer_R=int64#3]
# asm 2: str <r0=x3,[<pointer_R=x2]
str x3,[x2]

# qhasm: mem64[pointer_R + 8] = r1
# asm 1: str <r1=int64#5,[<pointer_R=int64#3,#8]
# asm 2: str <r1=x4,[<pointer_R=x2,#8]
str x4,[x2,#8]

# qhasm: mem64[pointer_R + 16] = r2
# asm 1: str <r2=int64#2,[<pointer_R=int64#3,#16]
# asm 2: str <r2=x1,[<pointer_R=x2,#16]
str x1,[x2,#16]

# qhasm: mem64[pointer_R + 24] = r3
# asm 1: str <r3=int64#1,[<pointer_R=int64#3,#24]
# asm 2: str <r3=x0,[<pointer_R=x2,#24]
str x0,[x2,#24]

# qhasm: return
ret
