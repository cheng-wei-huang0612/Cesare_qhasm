
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

# qhasm: enter matxvec_1664x6528_aarch64
.align 4
.global _matxvec_1664x6528_aarch64
.global matxvec_1664x6528_aarch64
_matxvec_1664x6528_aarch64:
matxvec_1664x6528_aarch64:

# qhasm: input input_x0

# qhasm: input input_x1

# qhasm: input input_x2

# qhasm: caller calleesaved_v8

# qhasm: caller calleesaved_v9

# qhasm: caller calleesaved_v10

# qhasm: caller calleesaved_v11

# qhasm: caller calleesaved_v12

# qhasm: caller calleesaved_v13

# qhasm: caller calleesaved_v14

# qhasm: caller calleesaved_v15

# qhasm: push2x8b calleesaved_v8 , calleesaved_v9
# asm 1: stp <calleesaved_v8=reg128#9%dregname,<calleesaved_v9=reg128#10%dregname,[sp,#-16]!
# asm 2: stp <calleesaved_v8=d8,<calleesaved_v9=d9,[sp,#-16]!
stp d8,d9,[sp,#-16]!

# qhasm: push2x8b calleesaved_v10 , calleesaved_v11
# asm 1: stp <calleesaved_v10=reg128#11%dregname,<calleesaved_v11=reg128#12%dregname,[sp,#-16]!
# asm 2: stp <calleesaved_v10=d10,<calleesaved_v11=d11,[sp,#-16]!
stp d10,d11,[sp,#-16]!

# qhasm: push2x8b calleesaved_v12 , calleesaved_v13
# asm 1: stp <calleesaved_v12=reg128#13%dregname,<calleesaved_v13=reg128#14%dregname,[sp,#-16]!
# asm 2: stp <calleesaved_v12=d12,<calleesaved_v13=d13,[sp,#-16]!
stp d12,d13,[sp,#-16]!

# qhasm: push2x8b calleesaved_v14 , calleesaved_v15
# asm 1: stp <calleesaved_v14=reg128#15%dregname,<calleesaved_v15=reg128#16%dregname,[sp,#-16]!
# asm 2: stp <calleesaved_v14=d14,<calleesaved_v15=d15,[sp,#-16]!
stp d14,d15,[sp,#-16]!

# qhasm: reg128 mi0

# qhasm: reg128 mi1

# qhasm: reg128 mi2

# qhasm: reg128 mi3

# qhasm: reg128 vi0

# qhasm: reg128 vi1

# qhasm: reg128 vi2

# qhasm: reg128 vi3

# qhasm: reg128 di0

# qhasm: reg128 di1

# qhasm: reg128 di2

# qhasm: reg128 di3

# qhasm: reg128 di4

# qhasm: reg128 di5

# qhasm: reg128 di6

# qhasm: reg128 di7

# qhasm: reg128 mask_1

# qhasm: reg128 mask_01234567

# qhasm: int64 index

# qhasm: index = 1
# asm 1: mov >index=int64#4, #1
# asm 2: mov >index=x3, #1
mov x3, #1

# qhasm: 16x mask_1 = index
# asm 1: dup <mask_1=reg128#1.16b, <index=int64#4%wregname
# asm 2: dup <mask_1=v0.16b, <index=w3
dup v0.16b, w3

# qhasm: index = 256
# asm 1: mov >index=int64#4, #256
# asm 2: mov >index=x3, #256
mov x3, #256

# qhasm: index[1/4] = 770
# asm 1: movk <index=int64#4, #770,LSL #16
# asm 2: movk <index=x3, #770,LSL #16
movk x3, #770,LSL #16

# qhasm: index[2/4] = 1284
# asm 1: movk <index=int64#4, #1284,LSL #32
# asm 2: movk <index=x3, #1284,LSL #32
movk x3, #1284,LSL #32

# qhasm: index[3/4] = 1798
# asm 1: movk <index=int64#4, #1798,LSL #48
# asm 2: movk <index=x3, #1798,LSL #48
movk x3, #1798,LSL #48

# qhasm: 2x mask_01234567 = index
# asm 1: dup <mask_01234567=reg128#2.2d, <index=int64#4
# asm 2: dup <mask_01234567=v1.2d, <index=x3
dup v1.2d, x3

# qhasm: int64 row_index

# qhasm: row_index = 208
# asm 1: mov >row_index=int64#4, #208
# asm 2: mov >row_index=x3, #208
mov x3, #208

# qhasm: L_V4START:
._L_V4START:

# qhasm: di0 ^= di0
# asm 1: eor <di0=reg128#3.16b, <di0=reg128#3.16b, <di0=reg128#3.16b
# asm 2: eor <di0=v2.16b, <di0=v2.16b, <di0=v2.16b
eor v2.16b, v2.16b, v2.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_0:
._L_0:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#11%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q10,[<input_x1=x1],#16
ldr q10,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#12%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q11,[<input_x2=x2],#16
ldr q11,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#11.16b, <mi0=reg128#11.16b, <vi0=reg128#12.16b
# asm 2: and <mi0=v10.16b, <mi0=v10.16b, <vi0=v11.16b
and v10.16b, v10.16b, v11.16b

# qhasm: di0 ^= mi0
# asm 1: eor <di0=reg128#3.16b, <di0=reg128#3.16b, <mi0=reg128#11.16b
# asm 2: eor <di0=v2.16b, <di0=v2.16b, <mi0=v10.16b
eor v2.16b, v2.16b, v10.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_0 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_0
# asm 2: cbnz <index=x4 , ._L_0
cbnz x4 , ._L_0

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di1 ^= di1
# asm 1: eor <di1=reg128#4.16b, <di1=reg128#4.16b, <di1=reg128#4.16b
# asm 2: eor <di1=v3.16b, <di1=v3.16b, <di1=v3.16b
eor v3.16b, v3.16b, v3.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_1:
._L_1:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#11%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q10,[<input_x1=x1],#16
ldr q10,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#12%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q11,[<input_x2=x2],#16
ldr q11,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#11.16b, <mi0=reg128#11.16b, <vi0=reg128#12.16b
# asm 2: and <mi0=v10.16b, <mi0=v10.16b, <vi0=v11.16b
and v10.16b, v10.16b, v11.16b

# qhasm: di1 ^= mi0
# asm 1: eor <di1=reg128#4.16b, <di1=reg128#4.16b, <mi0=reg128#11.16b
# asm 2: eor <di1=v3.16b, <di1=v3.16b, <mi0=v10.16b
eor v3.16b, v3.16b, v10.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_1 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_1
# asm 2: cbnz <index=x4 , ._L_1
cbnz x4 , ._L_1

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di2 ^= di2
# asm 1: eor <di2=reg128#5.16b, <di2=reg128#5.16b, <di2=reg128#5.16b
# asm 2: eor <di2=v4.16b, <di2=v4.16b, <di2=v4.16b
eor v4.16b, v4.16b, v4.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_2:
._L_2:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#11%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q10,[<input_x1=x1],#16
ldr q10,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#12%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q11,[<input_x2=x2],#16
ldr q11,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#11.16b, <mi0=reg128#11.16b, <vi0=reg128#12.16b
# asm 2: and <mi0=v10.16b, <mi0=v10.16b, <vi0=v11.16b
and v10.16b, v10.16b, v11.16b

# qhasm: di2 ^= mi0
# asm 1: eor <di2=reg128#5.16b, <di2=reg128#5.16b, <mi0=reg128#11.16b
# asm 2: eor <di2=v4.16b, <di2=v4.16b, <mi0=v10.16b
eor v4.16b, v4.16b, v10.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_2 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_2
# asm 2: cbnz <index=x4 , ._L_2
cbnz x4 , ._L_2

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di3 ^= di3
# asm 1: eor <di3=reg128#6.16b, <di3=reg128#6.16b, <di3=reg128#6.16b
# asm 2: eor <di3=v5.16b, <di3=v5.16b, <di3=v5.16b
eor v5.16b, v5.16b, v5.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_3:
._L_3:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#11%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q10,[<input_x1=x1],#16
ldr q10,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#12%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q11,[<input_x2=x2],#16
ldr q11,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#11.16b, <mi0=reg128#11.16b, <vi0=reg128#12.16b
# asm 2: and <mi0=v10.16b, <mi0=v10.16b, <vi0=v11.16b
and v10.16b, v10.16b, v11.16b

# qhasm: di3 ^= mi0
# asm 1: eor <di3=reg128#6.16b, <di3=reg128#6.16b, <mi0=reg128#11.16b
# asm 2: eor <di3=v5.16b, <di3=v5.16b, <mi0=v10.16b
eor v5.16b, v5.16b, v10.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_3 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_3
# asm 2: cbnz <index=x4 , ._L_3
cbnz x4 , ._L_3

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di4 ^= di4
# asm 1: eor <di4=reg128#7.16b, <di4=reg128#7.16b, <di4=reg128#7.16b
# asm 2: eor <di4=v6.16b, <di4=v6.16b, <di4=v6.16b
eor v6.16b, v6.16b, v6.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_4:
._L_4:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#11%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q10,[<input_x1=x1],#16
ldr q10,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#12%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q11,[<input_x2=x2],#16
ldr q11,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#11.16b, <mi0=reg128#11.16b, <vi0=reg128#12.16b
# asm 2: and <mi0=v10.16b, <mi0=v10.16b, <vi0=v11.16b
and v10.16b, v10.16b, v11.16b

# qhasm: di4 ^= mi0
# asm 1: eor <di4=reg128#7.16b, <di4=reg128#7.16b, <mi0=reg128#11.16b
# asm 2: eor <di4=v6.16b, <di4=v6.16b, <mi0=v10.16b
eor v6.16b, v6.16b, v10.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_4 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_4
# asm 2: cbnz <index=x4 , ._L_4
cbnz x4 , ._L_4

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di5 ^= di5
# asm 1: eor <di5=reg128#8.16b, <di5=reg128#8.16b, <di5=reg128#8.16b
# asm 2: eor <di5=v7.16b, <di5=v7.16b, <di5=v7.16b
eor v7.16b, v7.16b, v7.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_5:
._L_5:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#7%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q6,[<input_x1=x1],#16
ldr q6,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#11%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q10,[<input_x2=x2],#16
ldr q10,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#7.16b, <mi0=reg128#7.16b, <vi0=reg128#11.16b
# asm 2: and <mi0=v6.16b, <mi0=v6.16b, <vi0=v10.16b
and v6.16b, v6.16b, v10.16b

# qhasm: di5 ^= mi0
# asm 1: eor <di5=reg128#8.16b, <di5=reg128#8.16b, <mi0=reg128#7.16b
# asm 2: eor <di5=v7.16b, <di5=v7.16b, <mi0=v6.16b
eor v7.16b, v7.16b, v6.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_5 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_5
# asm 2: cbnz <index=x4 , ._L_5
cbnz x4 , ._L_5

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di6 ^= di6
# asm 1: eor <di6=reg128#9.16b, <di6=reg128#9.16b, <di6=reg128#9.16b
# asm 2: eor <di6=v8.16b, <di6=v8.16b, <di6=v8.16b
eor v8.16b, v8.16b, v8.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_6:
._L_6:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#7%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q6,[<input_x1=x1],#16
ldr q6,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#8%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q7,[<input_x2=x2],#16
ldr q7,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#7.16b, <mi0=reg128#7.16b, <vi0=reg128#8.16b
# asm 2: and <mi0=v6.16b, <mi0=v6.16b, <vi0=v7.16b
and v6.16b, v6.16b, v7.16b

# qhasm: di6 ^= mi0
# asm 1: eor <di6=reg128#9.16b, <di6=reg128#9.16b, <mi0=reg128#7.16b
# asm 2: eor <di6=v8.16b, <di6=v8.16b, <mi0=v6.16b
eor v8.16b, v8.16b, v6.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_6 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_6
# asm 2: cbnz <index=x4 , ._L_6
cbnz x4 , ._L_6

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: di7 ^= di7
# asm 1: eor <di7=reg128#10.16b, <di7=reg128#10.16b, <di7=reg128#10.16b
# asm 2: eor <di7=v9.16b, <di7=v9.16b, <di7=v9.16b
eor v9.16b, v9.16b, v9.16b

# qhasm: index = 51
# asm 1: mov >index=int64#5, #51
# asm 2: mov >index=x4, #51
mov x4, #51

# qhasm: L_7:
._L_7:

# qhasm: mi0 = mem128[input_x1], input_x1 += 16
# asm 1: ldr >mi0=reg128#7%qregname,[<input_x1=int64#2],#16
# asm 2: ldr >mi0=q6,[<input_x1=x1],#16
ldr q6,[x1],#16

# qhasm: vi0 = mem128[input_x2], input_x2 += 16
# asm 1: ldr >vi0=reg128#8%qregname,[<input_x2=int64#3],#16
# asm 2: ldr >vi0=q7,[<input_x2=x2],#16
ldr q7,[x2],#16

# qhasm: mi0 &= vi0
# asm 1: and <mi0=reg128#7.16b, <mi0=reg128#7.16b, <vi0=reg128#8.16b
# asm 2: and <mi0=v6.16b, <mi0=v6.16b, <vi0=v7.16b
and v6.16b, v6.16b, v7.16b

# qhasm: di7 ^= mi0
# asm 1: eor <di7=reg128#10.16b, <di7=reg128#10.16b, <mi0=reg128#7.16b
# asm 2: eor <di7=v9.16b, <di7=v9.16b, <mi0=v6.16b
eor v9.16b, v9.16b, v6.16b

# qhasm: index -= 1 !
# asm 1: subs <index=int64#5,<index=int64#5,#1
# asm 2: subs <index=x4,<index=x4,#1
subs x4,x4,#1

# qhasm: goto L_7 if index != 0
# asm 1: cbnz <index=int64#5 , ._L_7
# asm 2: cbnz <index=x4 , ._L_7
cbnz x4 , ._L_7

# qhasm: input_x2 -= 816
# asm 1: sub <input_x2=int64#3,<input_x2=int64#3,#816
# asm 2: sub <input_x2=x2,<input_x2=x2,#816
sub x2,x2,#816

# qhasm: 2x mi0 = di0[0/2] di1[0/2]
# asm 1: trn1 >mi0=reg128#7.2d,<di0=reg128#3.2d,<di1=reg128#4.2d
# asm 2: trn1 >mi0=v6.2d,<di0=v2.2d,<di1=v3.2d
trn1 v6.2d,v2.2d,v3.2d

# qhasm: 2x mi1 = di0[1/2] di1[1/2]
# asm 1: trn2 >mi1=reg128#3.2d,<di0=reg128#3.2d,<di1=reg128#4.2d
# asm 2: trn2 >mi1=v2.2d,<di0=v2.2d,<di1=v3.2d
trn2 v2.2d,v2.2d,v3.2d

# qhasm: 2x mi2 = di2[0/2] di3[0/2]
# asm 1: trn1 >mi2=reg128#4.2d,<di2=reg128#5.2d,<di3=reg128#6.2d
# asm 2: trn1 >mi2=v3.2d,<di2=v4.2d,<di3=v5.2d
trn1 v3.2d,v4.2d,v5.2d

# qhasm: 2x mi3 = di2[1/2] di3[1/2]
# asm 1: trn2 >mi3=reg128#5.2d,<di2=reg128#5.2d,<di3=reg128#6.2d
# asm 2: trn2 >mi3=v4.2d,<di2=v4.2d,<di3=v5.2d
trn2 v4.2d,v4.2d,v5.2d

# qhasm: di0 = mi0 ^ mi1
# asm 1: eor >di0=reg128#3.16b, <mi0=reg128#7.16b, <mi1=reg128#3.16b
# asm 2: eor >di0=v2.16b, <mi0=v6.16b, <mi1=v2.16b
eor v2.16b, v6.16b, v2.16b

# qhasm: di1 = mi2 ^ mi3
# asm 1: eor >di1=reg128#4.16b, <mi2=reg128#4.16b, <mi3=reg128#5.16b
# asm 2: eor >di1=v3.16b, <mi2=v3.16b, <mi3=v4.16b
eor v3.16b, v3.16b, v4.16b

# qhasm: 2x mi0 = di4[0/2] di5[0/2]
# asm 1: trn1 >mi0=reg128#5.2d,<di4=reg128#7.2d,<di5=reg128#8.2d
# asm 2: trn1 >mi0=v4.2d,<di4=v6.2d,<di5=v7.2d
trn1 v4.2d,v6.2d,v7.2d

# qhasm: 2x mi1 = di4[1/2] di5[1/2]
# asm 1: trn2 >mi1=reg128#6.2d,<di4=reg128#7.2d,<di5=reg128#8.2d
# asm 2: trn2 >mi1=v5.2d,<di4=v6.2d,<di5=v7.2d
trn2 v5.2d,v6.2d,v7.2d

# qhasm: 2x mi2 = di6[0/2] di7[0/2]
# asm 1: trn1 >mi2=reg128#11.2d,<di6=reg128#9.2d,<di7=reg128#10.2d
# asm 2: trn1 >mi2=v10.2d,<di6=v8.2d,<di7=v9.2d
trn1 v10.2d,v8.2d,v9.2d

# qhasm: 2x mi3 = di6[1/2] di7[1/2]
# asm 1: trn2 >mi3=reg128#12.2d,<di6=reg128#9.2d,<di7=reg128#10.2d
# asm 2: trn2 >mi3=v11.2d,<di6=v8.2d,<di7=v9.2d
trn2 v11.2d,v8.2d,v9.2d

# qhasm: di2 = mi0 ^ mi1
# asm 1: eor >di2=reg128#5.16b, <mi0=reg128#5.16b, <mi1=reg128#6.16b
# asm 2: eor >di2=v4.16b, <mi0=v4.16b, <mi1=v5.16b
eor v4.16b, v4.16b, v5.16b

# qhasm: di3 = mi2 ^ mi3
# asm 1: eor >di3=reg128#6.16b, <mi2=reg128#11.16b, <mi3=reg128#12.16b
# asm 2: eor >di3=v5.16b, <mi2=v10.16b, <mi3=v11.16b
eor v5.16b, v10.16b, v11.16b

# qhasm: 4x mi0 = di0[0/4] di0[2/4] di1[0/4] di1[2/4]
# asm 1: uzp1 >mi0=reg128#11.4s, <di0=reg128#3.4s, <di1=reg128#4.4s
# asm 2: uzp1 >mi0=v10.4s, <di0=v2.4s, <di1=v3.4s
uzp1 v10.4s, v2.4s, v3.4s

# qhasm: 4x mi1 = di0[1/4] di0[3/4] di1[1/4] di1[3/4]
# asm 1: uzp2 >mi1=reg128#3.4s, <di0=reg128#3.4s, <di1=reg128#4.4s
# asm 2: uzp2 >mi1=v2.4s, <di0=v2.4s, <di1=v3.4s
uzp2 v2.4s, v2.4s, v3.4s

# qhasm: di0 = mi0 ^ mi1
# asm 1: eor >di0=reg128#3.16b, <mi0=reg128#11.16b, <mi1=reg128#3.16b
# asm 2: eor >di0=v2.16b, <mi0=v10.16b, <mi1=v2.16b
eor v2.16b, v10.16b, v2.16b

# qhasm: 4x mi0 = di2[0/4] di2[2/4] di3[0/4] di3[2/4]
# asm 1: uzp1 >mi0=reg128#4.4s, <di2=reg128#5.4s, <di3=reg128#6.4s
# asm 2: uzp1 >mi0=v3.4s, <di2=v4.4s, <di3=v5.4s
uzp1 v3.4s, v4.4s, v5.4s

# qhasm: 4x mi1 = di2[1/4] di2[3/4] di3[1/4] di3[3/4]
# asm 1: uzp2 >mi1=reg128#11.4s, <di2=reg128#5.4s, <di3=reg128#6.4s
# asm 2: uzp2 >mi1=v10.4s, <di2=v4.4s, <di3=v5.4s
uzp2 v10.4s, v4.4s, v5.4s

# qhasm: di1 = mi0 ^ mi1
# asm 1: eor >di1=reg128#4.16b, <mi0=reg128#4.16b, <mi1=reg128#11.16b
# asm 2: eor >di1=v3.16b, <mi0=v3.16b, <mi1=v10.16b
eor v3.16b, v3.16b, v10.16b

# qhasm: 8x mi0 = di0[0/8] di0[2/8] di1[0/8] di1[2/8]
# asm 1: uzp1 >mi0=reg128#11.8h, <di0=reg128#3.8h, <di1=reg128#4.8h
# asm 2: uzp1 >mi0=v10.8h, <di0=v2.8h, <di1=v3.8h
uzp1 v10.8h, v2.8h, v3.8h

# qhasm: 8x mi1 = di0[1/8] di0[3/8] di1[1/8] di1[3/8]
# asm 1: uzp2 >mi1=reg128#3.8h, <di0=reg128#3.8h, <di1=reg128#4.8h
# asm 2: uzp2 >mi1=v2.8h, <di0=v2.8h, <di1=v3.8h
uzp2 v2.8h, v2.8h, v3.8h

# qhasm: di0 = mi0 ^ mi1
# asm 1: eor >di0=reg128#3.16b, <mi0=reg128#11.16b, <mi1=reg128#3.16b
# asm 2: eor >di0=v2.16b, <mi0=v10.16b, <mi1=v2.16b
eor v2.16b, v10.16b, v2.16b

# qhasm: di1 ^= di1
# asm 1: eor <di1=reg128#4.16b, <di1=reg128#4.16b, <di1=reg128#4.16b
# asm 2: eor <di1=v3.16b, <di1=v3.16b, <di1=v3.16b
eor v3.16b, v3.16b, v3.16b

# qhasm: 16x mi0 = di0[0/16] di0[2/16] di1[0/16] di1[2/16]
# asm 1: uzp1 >mi0=reg128#11.16b, <di0=reg128#3.16b, <di1=reg128#4.16b
# asm 2: uzp1 >mi0=v10.16b, <di0=v2.16b, <di1=v3.16b
uzp1 v10.16b, v2.16b, v3.16b

# qhasm: 16x mi1 = di0[1/16] di0[3/16] di1[1/16] di1[3/16]
# asm 1: uzp2 >mi1=reg128#3.16b, <di0=reg128#3.16b, <di1=reg128#4.16b
# asm 2: uzp2 >mi1=v2.16b, <di0=v2.16b, <di1=v3.16b
uzp2 v2.16b, v2.16b, v3.16b

# qhasm: di0 = mi0 ^ mi1
# asm 1: eor >di0=reg128#3.16b, <mi0=reg128#11.16b, <mi1=reg128#3.16b
# asm 2: eor >di0=v2.16b, <mi0=v10.16b, <mi1=v2.16b
eor v2.16b, v10.16b, v2.16b

# qhasm: 16x di1 = popcnt di0
# asm 1: cnt >di1=reg128#3.16b,<di0=reg128#3.16b
# asm 2: cnt >di1=v2.16b,<di0=v2.16b
cnt v2.16b,v2.16b

# qhasm: di0 = di1 & mask_1
# asm 1: and >di0=reg128#3.16b, <di1=reg128#3.16b, <mask_1=reg128#1.16b
# asm 2: and >di0=v2.16b, <di1=v2.16b, <mask_1=v0.16b
and v2.16b, v2.16b, v0.16b

# qhasm: 16x di0 unsigned<<= mask_01234567
# asm 1: ushl >di0=reg128#3.16b, <di0=reg128#3.16b, <mask_01234567=reg128#2.16b
# asm 2: ushl >di0=v2.16b, <di0=v2.16b, <mask_01234567=v1.16b
ushl v2.16b, v2.16b, v1.16b

# qhasm: 8x di1 = reduce+ di0[0/2]
# asm 1: addv >di1=reg128#4%bregname,<di0=reg128#3.8b
# asm 2: addv >di1=b3,<di0=v2.8b
addv b3,v2.8b

# qhasm: mem8[input_x0] = di1,input_x0 += 1
# asm 1: str <di1=reg128#4%bregname, [<input_x0=int64#1], #1
# asm 2: str <di1=b3, [<input_x0=x0], #1
str b3, [x0], #1

# qhasm: row_index -= 1 !
# asm 1: subs <row_index=int64#4,<row_index=int64#4,#1
# asm 2: subs <row_index=x3,<row_index=x3,#1
subs x3,x3,#1

# qhasm: goto L_V4START if row_index != 0
# asm 1: cbnz <row_index=int64#4 , ._L_V4START
# asm 2: cbnz <row_index=x3 , ._L_V4START
cbnz x3 , ._L_V4START

# qhasm: L_FEND:
._L_FEND:

# qhasm: pop2x8b calleesaved_v14 , calleesaved_v15
# asm 1: ldp >calleesaved_v14=reg128#15%dregname,>calleesaved_v15=reg128#16%dregname,[sp],#16
# asm 2: ldp >calleesaved_v14=d14,>calleesaved_v15=d15,[sp],#16
ldp d14,d15,[sp],#16

# qhasm: pop2x8b calleesaved_v12 , calleesaved_v13
# asm 1: ldp >calleesaved_v12=reg128#13%dregname,>calleesaved_v13=reg128#14%dregname,[sp],#16
# asm 2: ldp >calleesaved_v12=d12,>calleesaved_v13=d13,[sp],#16
ldp d12,d13,[sp],#16

# qhasm: pop2x8b calleesaved_v10 , calleesaved_v11
# asm 1: ldp >calleesaved_v10=reg128#11%dregname,>calleesaved_v11=reg128#12%dregname,[sp],#16
# asm 2: ldp >calleesaved_v10=d10,>calleesaved_v11=d11,[sp],#16
ldp d10,d11,[sp],#16

# qhasm: pop2x8b calleesaved_v8 , calleesaved_v9
# asm 1: ldp >calleesaved_v8=reg128#9%dregname,>calleesaved_v9=reg128#10%dregname,[sp],#16
# asm 2: ldp >calleesaved_v8=d8,>calleesaved_v9=d9,[sp],#16
ldp d8,d9,[sp],#16

# qhasm: return
ret
