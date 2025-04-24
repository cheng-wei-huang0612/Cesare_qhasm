

int64 pointer_delta
int64 pointer_fuv
int64 pointer_grs

input pointer_delta
input pointer_fuv
input pointer_grs

int64 delta
int64 fuv
int64 grs


int64 g0_and_1
int64 cond
int64 delta_tmp
int64 c_mask
int64 n_mask

int64 fuv_new
int64 grs_new
int64 tmp
int64 neg_fuv

int64 neg_delta
int64 delta_swapper



enter divstep

delta = mem64[pointer_delta]
fuv = mem64[pointer_fuv]
grs = mem64[pointer_grs]


g0_and_1 = grs & 1

delta - 0!
c_mask = g0_and_1 if signed> else 0 
c_mask = -c_mask!

neg_fuv = -fuv
neg_delta = -delta


fuv_new = grs if negative else fuv


return 
