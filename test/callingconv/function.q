enter matxvec_1664x6528_aarch64
input input_x0
input input_x1
input input_x2

caller calleesaved_v8
caller calleesaved_v9
caller calleesaved_v10
caller calleesaved_v11
caller calleesaved_v12
caller calleesaved_v13
caller calleesaved_v14
caller calleesaved_v15

push2x8b calleesaved_v8 , calleesaved_v9
push2x8b calleesaved_v10 , calleesaved_v11
push2x8b calleesaved_v12 , calleesaved_v13
push2x8b calleesaved_v14 , calleesaved_v15

#
# Program start
#


reg128 mi0
reg128 mi1
reg128 mi2
reg128 mi3
reg128 vi0
reg128 vi1
reg128 vi2
reg128 vi3

reg128 di0
reg128 di1
reg128 di2
reg128 di3

reg128 di4
reg128 di5
reg128 di6
reg128 di7

reg128 mask_1
reg128 mask_01234567

int64 index
index = 1
16x mask_1 = index
index = 256
index[1/4] = 770
index[2/4] = 1284
index[3/4] = 1798
2x mask_01234567 = index


int64 row_index
row_index = 208
L_V4START:

# 51 = 48 + 3

di0 ^= di0
index = 51
L_0:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di0 ^= mi0
index -= 1 !
goto L_0 if index != 0
input_x2 -= 816

di1 ^= di1
index = 51
L_1:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di1 ^= mi0
index -= 1 !
goto L_1 if index != 0
input_x2 -= 816

di2 ^= di2
index = 51
L_2:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di2 ^= mi0
index -= 1 !
goto L_2 if index != 0
input_x2 -= 816

di3 ^= di3
index = 51
L_3:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di3 ^= mi0
index -= 1 !
goto L_3 if index != 0
input_x2 -= 816


di4 ^= di4
index = 51
L_4:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di4 ^= mi0
index -= 1 !
goto L_4 if index != 0
input_x2 -= 816


di5 ^= di5
index = 51
L_5:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di5 ^= mi0
index -= 1 !
goto L_5 if index != 0
input_x2 -= 816


di6 ^= di6
index = 51
L_6:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di6 ^= mi0
index -= 1 !
goto L_6 if index != 0
input_x2 -= 816


di7 ^= di7
index = 51
L_7:
mi0 = mem128[input_x1], input_x1 += 16
vi0 = mem128[input_x2], input_x2 += 16
mi0 &= vi0
di7 ^= mi0
index -= 1 !
goto L_7 if index != 0
input_x2 -= 816


# reduce
2x mi0 = di0[0/2] di1[0/2]
2x mi1 = di0[1/2] di1[1/2]
2x mi2 = di2[0/2] di3[0/2]
2x mi3 = di2[1/2] di3[1/2]
di0 = mi0 ^ mi1
di1 = mi2 ^ mi3

2x mi0 = di4[0/2] di5[0/2]
2x mi1 = di4[1/2] di5[1/2]
2x mi2 = di6[0/2] di7[0/2]
2x mi3 = di6[1/2] di7[1/2]
di2 = mi0 ^ mi1
di3 = mi2 ^ mi3

4x mi0 = di0[0/4] di0[2/4] di1[0/4] di1[2/4]
4x mi1 = di0[1/4] di0[3/4] di1[1/4] di1[3/4]
di0 = mi0 ^ mi1

4x mi0 = di2[0/4] di2[2/4] di3[0/4] di3[2/4]
4x mi1 = di2[1/4] di2[3/4] di3[1/4] di3[3/4]
di1 = mi0 ^ mi1

8x mi0 = di0[0/8] di0[2/8] di1[0/8] di1[2/8]
8x mi1 = di0[1/8] di0[3/8] di1[1/8] di1[3/8]
di0 = mi0 ^ mi1

di1 ^= di1
16x mi0 = di0[0/16] di0[2/16] di1[0/16] di1[2/16]
16x mi1 = di0[1/16] di0[3/16] di1[1/16] di1[3/16]
di0 = mi0 ^ mi1

16x di1 = popcnt di0

di0 = di1 & mask_1
16x di0 unsigned<<= mask_01234567
8x di1 = reduce+ di0[0/2]

mem8[input_x0] = di1,input_x0 += 1


row_index -= 1 !
goto L_V4START if row_index != 0


#
# Program end
#
L_FEND:
pop2x8b calleesaved_v14 , calleesaved_v15
pop2x8b calleesaved_v12 , calleesaved_v13
pop2x8b calleesaved_v10 , calleesaved_v11
pop2x8b calleesaved_v8 , calleesaved_v9

return
