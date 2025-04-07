int64 pointer_A
int64 pointer_B
int64 pointer_R

input pointer_A
input pointer_B
input pointer_R


int64 A
int64 B
int64 sign_A
int64 sign_B
int64 mask_A
int64 mask_B

int64 R0
int64 R1
int64 sign_R
int64 mask_R

int64 product_lo
int64 product_hi

enter int64_times_int64

A = mem64[pointer_A]

B = mem64[pointer_B]


sign_A = A  >> 63
sign_B = B >> 63

# Take abs(A), branchless
mask_A = - sign_A
A ^= mask_A
A = A + sign_A


# Take abs(B), branchless
mask_B = - sign_B
B ^= mask_B
B = B + sign_B 

sign_R = sign_A ^ sign_B

R0 = 0
R1 = 0

R0 = A * B
R1 = A * B (hi)


mask_R = - sign_R
R0 ^= mask_R
R1 ^= mask_R


R0 = R0 + sign_R!
R1 = R1 + carry !


mem64[pointer_R] = R0
mem64[pointer_R + 8] = R1


return