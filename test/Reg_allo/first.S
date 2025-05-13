
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

# qhasm: constant my_constants:
.p2align 4
my_constants:

# qhasm: const32 1
.word 1

# qhasm: enter start
.align 4
.global _start
.global start
_start:
start:

# qhasm: reg128 vec_F0_F1_G0_G1

# qhasm: assign v0 to vec_F0_F1_G0_G1

# qhasm: reg128 vec_F2_F3_G2_G3

# qhasm: assign v1 to vec_F2_F3_G2_G3

# qhasm: reg128 vec_F4_F5_G4_G5

# qhasm: assign v2 to vec_F4_F5_G4_G5

# qhasm: reg128 vec_F6_F7_G6_G7

# qhasm: assign v3 to vec_F6_F7_G6_G7

# qhasm: reg128 vec_F8_F9_G8_G9

# qhasm: assign v4 to vec_F8_F9_G8_G9

# qhasm: reg128 vec_V0_V1_S0_S1

# qhasm: assign v5 to vec_V0_V1_S0_S1

# qhasm: reg128 vec_V2_V3_S2_S3

# qhasm: assign v6 to vec_V2_V3_S2_S3

# qhasm: reg128 vec_V4_V5_S4_S5

# qhasm: assign v7 to vec_V4_V5_S4_S5

# qhasm: reg128 vec_V6_V7_S6_S7

# qhasm: assign v8 to vec_V6_V7_S6_S7

# qhasm: reg128 vec_V8_V9_S8_S9

# qhasm: assign v9 to vec_V8_V9_S8_S9

# qhasm: reg128 vec_uu0_rr0_vv0_ss0

# qhasm: assign v10 to vec_uu0_rr0_vv0_ss0

# qhasm: reg128 vec_uu1_rr1_vv1_ss1

# qhasm: assign v11 to vec_uu1_rr1_vv1_ss1

# qhasm: reg128 vec_uuhat_rrhat_vvhat_sshat

# qhasm: assign v12 to vec_uuhat_rrhat_vvhat_sshat

# qhasm: reg128 vec_uuV0_uuV1_rrV0_rrV1

# qhasm: assign v13 to vec_uuV0_uuV1_rrV0_rrV1

# qhasm: reg128 vec_uuV2_uuV3_rrV2_rrV3

# qhasm: assign v14 to vec_uuV2_uuV3_rrV2_rrV3

# qhasm: reg128 vec_uuV4_uuV5_rrV4_rrV5

# qhasm: assign v15 to vec_uuV4_uuV5_rrV4_rrV5

# qhasm: reg128 vec_uuV6_uuV7_rrV6_rrV7

# qhasm: assign v16 to vec_uuV6_uuV7_rrV6_rrV7

# qhasm: reg128 vec_uuV8_uuV9_rrV8_rrV9

# qhasm: assign v17 to vec_uuV8_uuV9_rrV8_rrV9

# qhasm: reg128 vec_uuV10_uuV11_rrV10_rrV11

# qhasm: assign v18 to vec_uuV10_uuV11_rrV10_rrV11

# qhasm: reg128 vec_vvS0_vvS1_ssS0_ssS1

# qhasm: reg128 vec_vvS2_vvS3_ssS2_ssS3

# qhasm: reg128 vec_vvS4_vvS5_ssS4_ssS5

# qhasm: reg128 vec_vvS6_vvS7_ssS6_ssS7

# qhasm: reg128 vec_vvS8_vvS9_ssS8_ssS9

# qhasm: reg128 vec_vvS10_vvS11_ssS10_ssS11

# qhasm: reg128 vec_2x_2p30a2p31 

# qhasm: reg128 vec_2x_2p62a2p63 

# qhasm: reg128 vec_2x_2p30m1 

# qhasm: 2x vec_F2_F3_G2_G3 = 0
# asm 1: movi <vec_F2_F3_G2_G3=reg128#2.2d, #0
# asm 2: movi <vec_F2_F3_G2_G3=v1.2d, #0
movi v1.2d, #0

# qhasm: 2x vec_uuV0_uuV1_rrV0_rrV1 = 0
# asm 1: movi <vec_uuV0_uuV1_rrV0_rrV1=reg128#14.2d, #0
# asm 2: movi <vec_uuV0_uuV1_rrV0_rrV1=v13.2d, #0
movi v13.2d, #0

# qhasm: 2x vec_uuV0_uuV1_rrV0_rrV1 = vec_uu0_rr0_vv0_ss0[0] unsigned* vec_V0_V1_S0_S1[0/4]
# asm 1: umull >vec_uuV0_uuV1_rrV0_rrV1=reg128#14.2d, <vec_uu0_rr0_vv0_ss0=reg128#11.2s, <vec_V0_V1_S0_S1=reg128#6.s[0]
# asm 2: umull >vec_uuV0_uuV1_rrV0_rrV1=v13.2d, <vec_uu0_rr0_vv0_ss0=v10.2s, <vec_V0_V1_S0_S1=v5.s[0]
umull v13.2d, v10.2s, v5.s[0]

# qhasm: free vec_F0_F1_G0_G1

# qhasm: free vec_F2_F3_G2_G3

# qhasm: free vec_F4_F5_G4_G5

# qhasm: free vec_F6_F7_G6_G7

# qhasm: free vec_F8_F9_G8_G9

# qhasm: free vec_V0_V1_S0_S1

# qhasm: free vec_V2_V3_S2_S3

# qhasm: free vec_V4_V5_S4_S5

# qhasm: free vec_V6_V7_S6_S7

# qhasm: free vec_V8_V9_S8_S9

# qhasm: free vec_uu0_rr0_vv0_ss0

# qhasm: free vec_uu1_rr1_vv1_ss1

# qhasm: free vec_uuhat_rrhat_vvhat_sshat

# qhasm: return
ret
