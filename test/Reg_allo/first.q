

constant my_constants:
const32 1


enter start

reg128 vec_F0_F1_G0_G1
assign v0 to vec_F0_F1_G0_G1
reg128 vec_F2_F3_G2_G3
assign v1 to vec_F2_F3_G2_G3
reg128 vec_F4_F5_G4_G5
assign v2 to vec_F4_F5_G4_G5
reg128 vec_F6_F7_G6_G7
assign v3 to vec_F6_F7_G6_G7
reg128 vec_F8_F9_G8_G9
assign v4 to vec_F8_F9_G8_G9
# The F9, G9 are always 0, we put them here for easy program writing

reg128 vec_V0_V1_S0_S1
assign v5 to vec_V0_V1_S0_S1
reg128 vec_V2_V3_S2_S3
assign v6 to vec_V2_V3_S2_S3
reg128 vec_V4_V5_S4_S5
assign v7 to vec_V4_V5_S4_S5
reg128 vec_V6_V7_S6_S7
assign v8 to vec_V6_V7_S6_S7
reg128 vec_V8_V9_S8_S9
assign v9 to vec_V8_V9_S8_S9
# The V9, S9 are always 0, we put them here for easy program writing

reg128 vec_uu0_rr0_vv0_ss0
assign v10 to vec_uu0_rr0_vv0_ss0
reg128 vec_uu1_rr1_vv1_ss1
assign v11 to vec_uu1_rr1_vv1_ss1
reg128 vec_uuhat_rrhat_vvhat_sshat
assign v12 to vec_uuhat_rrhat_vvhat_sshat

#---
#v13 ~ v28 are available
#---





# In the current computation, we temporarily allocate

reg128 vec_uuV0_uuV1_rrV0_rrV1
assign v13 to vec_uuV0_uuV1_rrV0_rrV1
reg128 vec_uuV2_uuV3_rrV2_rrV3
assign v14 to vec_uuV2_uuV3_rrV2_rrV3
reg128 vec_uuV4_uuV5_rrV4_rrV5
assign v15 to vec_uuV4_uuV5_rrV4_rrV5
reg128 vec_uuV6_uuV7_rrV6_rrV7
assign v16 to vec_uuV6_uuV7_rrV6_rrV7
reg128 vec_uuV8_uuV9_rrV8_rrV9
assign v17 to vec_uuV8_uuV9_rrV8_rrV9
reg128 vec_uuV10_uuV11_rrV10_rrV11
assign v18 to vec_uuV10_uuV11_rrV10_rrV11
reg128 vec_vvS0_vvS1_ssS0_ssS1
reg128 vec_vvS2_vvS3_ssS2_ssS3
reg128 vec_vvS4_vvS5_ssS4_ssS5
reg128 vec_vvS6_vvS7_ssS6_ssS7
reg128 vec_vvS8_vvS9_ssS8_ssS9
reg128 vec_vvS10_vvS11_ssS10_ssS11


reg128 vec_2x_2p30a2p31 #(Carry position 1) 
reg128 vec_2x_2p62a2p63 #(Carry position 2)
reg128 vec_2x_2p30m1 #(This is a constant used in update_{FG, VS} )

2x vec_F2_F3_G2_G3 = 0
2x vec_uuV0_uuV1_rrV0_rrV1 = 0
2x vec_uuV0_uuV1_rrV0_rrV1 = vec_uu0_rr0_vv0_ss0[0] unsigned* vec_V0_V1_S0_S1[0/4]

free vec_F0_F1_G0_G1
free vec_F2_F3_G2_G3
free vec_F4_F5_G4_G5
free vec_F6_F7_G6_G7
free vec_F8_F9_G8_G9

free vec_V0_V1_S0_S1
free vec_V2_V3_S2_S3
free vec_V4_V5_S4_S5
free vec_V6_V7_S6_S7
free vec_V8_V9_S8_S9

free vec_uu0_rr0_vv0_ss0
free vec_uu1_rr1_vv1_ss1
free vec_uuhat_rrhat_vvhat_sshat
return
