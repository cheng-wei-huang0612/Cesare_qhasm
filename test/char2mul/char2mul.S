
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

# qhasm: int64 a

# qhasm: int64 b

# qhasm: int64 c

# qhasm: int64 temp0

# qhasm: int64 temp1

# qhasm: int64 temp2

# qhasm: int64 temp3

# qhasm: int64 mask0

# qhasm: int64 mask1

# qhasm: int64 mask2

# qhasm: int64 mask3

# qhasm: int64 shiftA0

# qhasm: int64 shiftA1

# qhasm: int64 shiftA2

# qhasm: int64 shiftA3

# qhasm: int64 part0

# qhasm: int64 part1

# qhasm: int64 part2

# qhasm: int64 part3

# qhasm: input a

# qhasm: input b

# qhasm: enter gf2mul
.align 4
.global _gf2mul
.global gf2mul
_gf2mul:
gf2mul:

# qhasm: c = 0
# asm 1: mov >c=int64#3, #0
# asm 2: mov >c=x2, #0
mov x2, #0

# qhasm: temp0 = b >> 0
# asm 1: lsr  >temp0=int64#4,<b=int64#2,#0
# asm 2: lsr  >temp0=x3,<b=x1,#0
lsr  x3,x1,#0

# qhasm: mask0 = temp0 & 1
# asm 1: and  >mask0=int64#4,<temp0=int64#4,#1
# asm 2: and  >mask0=x3,<temp0=x3,#1
and  x3,x3,#1

# qhasm: mask0 = -mask0
# asm 1: neg >mask0=int64#4,<mask0=int64#4
# asm 2: neg >mask0=x3,<mask0=x3
neg x3,x3

# qhasm: shiftA0 = a << 0
# asm 1: lsl  >shiftA0=int64#5,<a=int64#1,#0
# asm 2: lsl  >shiftA0=x4,<a=x0,#0
lsl  x4,x0,#0

# qhasm: part0 = shiftA0 & mask0
# asm 1: and  >part0=int64#4,<shiftA0=int64#5,<mask0=int64#4
# asm 2: and  >part0=x3,<shiftA0=x4,<mask0=x3
and  x3,x4,x3

# qhasm: c ^= part0
# asm 1: eor >c=int64#3,<c=int64#3,<part0=int64#4
# asm 2: eor >c=x2,<c=x2,<part0=x3
eor x2,x2,x3

# qhasm: temp1 = b >> 1
# asm 1: lsr  >temp1=int64#4,<b=int64#2,#1
# asm 2: lsr  >temp1=x3,<b=x1,#1
lsr  x3,x1,#1

# qhasm: mask1 = temp1 & 1
# asm 1: and  >mask1=int64#4,<temp1=int64#4,#1
# asm 2: and  >mask1=x3,<temp1=x3,#1
and  x3,x3,#1

# qhasm: mask1 = -mask1
# asm 1: neg >mask1=int64#4,<mask1=int64#4
# asm 2: neg >mask1=x3,<mask1=x3
neg x3,x3

# qhasm: shiftA1 = a << 1
# asm 1: lsl  >shiftA1=int64#5,<a=int64#1,#1
# asm 2: lsl  >shiftA1=x4,<a=x0,#1
lsl  x4,x0,#1

# qhasm: part1 = shiftA1 & mask1
# asm 1: and  >part1=int64#4,<shiftA1=int64#5,<mask1=int64#4
# asm 2: and  >part1=x3,<shiftA1=x4,<mask1=x3
and  x3,x4,x3

# qhasm: c ^= part1
# asm 1: eor >c=int64#3,<c=int64#3,<part1=int64#4
# asm 2: eor >c=x2,<c=x2,<part1=x3
eor x2,x2,x3

# qhasm: temp2 = b >> 2
# asm 1: lsr  >temp2=int64#4,<b=int64#2,#2
# asm 2: lsr  >temp2=x3,<b=x1,#2
lsr  x3,x1,#2

# qhasm: mask2 = temp2 & 1
# asm 1: and  >mask2=int64#4,<temp2=int64#4,#1
# asm 2: and  >mask2=x3,<temp2=x3,#1
and  x3,x3,#1

# qhasm: mask2 = -mask2
# asm 1: neg >mask2=int64#4,<mask2=int64#4
# asm 2: neg >mask2=x3,<mask2=x3
neg x3,x3

# qhasm: shiftA2 = a << 2
# asm 1: lsl  >shiftA2=int64#5,<a=int64#1,#2
# asm 2: lsl  >shiftA2=x4,<a=x0,#2
lsl  x4,x0,#2

# qhasm: part2 = shiftA2 & mask2
# asm 1: and  >part2=int64#4,<shiftA2=int64#5,<mask2=int64#4
# asm 2: and  >part2=x3,<shiftA2=x4,<mask2=x3
and  x3,x4,x3

# qhasm: c ^= part2
# asm 1: eor >c=int64#3,<c=int64#3,<part2=int64#4
# asm 2: eor >c=x2,<c=x2,<part2=x3
eor x2,x2,x3

# qhasm: temp3 = b >> 3
# asm 1: lsr  >temp3=int64#2,<b=int64#2,#3
# asm 2: lsr  >temp3=x1,<b=x1,#3
lsr  x1,x1,#3

# qhasm: mask3 = temp3 & 1
# asm 1: and  >mask3=int64#2,<temp3=int64#2,#1
# asm 2: and  >mask3=x1,<temp3=x1,#1
and  x1,x1,#1

# qhasm: mask3 = -mask3
# asm 1: neg >mask3=int64#2,<mask3=int64#2
# asm 2: neg >mask3=x1,<mask3=x1
neg x1,x1

# qhasm: shiftA3 = a << 3
# asm 1: lsl  >shiftA3=int64#1,<a=int64#1,#3
# asm 2: lsl  >shiftA3=x0,<a=x0,#3
lsl  x0,x0,#3

# qhasm: part3 = shiftA3 & mask3
# asm 1: and  >part3=int64#1,<shiftA3=int64#1,<mask3=int64#2
# asm 2: and  >part3=x0,<shiftA3=x0,<mask3=x1
and  x0,x0,x1

# qhasm: c ^= part3
# asm 1: eor >c=int64#1,<c=int64#3,<part3=int64#1
# asm 2: eor >c=x0,<c=x2,<part3=x0
eor x0,x2,x0

# qhasm: return
ret
