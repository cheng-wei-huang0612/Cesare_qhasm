int64 pointer_A
int64 pointer_B

int64 pointer_R

input pointer_A
input pointer_B

input pointer_R


int64 A
int64 B0
int64 B1
int64 B2
int64 B3
int64 sign_A
int64 sign_B
int64 mask_A
int64 mask_B

int64 r0
int64 r1
int64 r2
int64 r3
int64 r4
int64 sign_R
int64 mask_R

int64 product_lo
int64 product_hi

enter int64_times_int256

A = mem64[pointer_A]

B0 = mem64[pointer_B]
B1 = mem64[pointer_B + 8]
B2 = mem64[pointer_B + 16]
B3 = mem64[pointer_B + 24]


sign_A = A  >> 63
sign_B = B3 >> 63

# Take abs(A), branchless
mask_A = - sign_A
A ^= mask_A
A = A + sign_A


# Take abs(B), branchless
mask_B = - sign_B
B0 ^= mask_B
B1 ^= mask_B
B2 ^= mask_B
B3 ^= mask_B
B0 = B0 + sign_B !
B1 = B1 + carry !
B2 = B2 + carry !
B3 = B3 + carry !

sign_R = sign_A ^ sign_B

r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0

# A * B0
product_lo = A * B0
product_hi = A * B0 (hi)

r0 = r0 + product_lo !
r1 = r1 + product_hi + carry !


# A * B1
product_lo = A * B1
product_hi = A * B1 (hi)

r1 = r1 + product_lo !
r2 = r2 + product_hi + carry !

# A * B2
product_lo = A * B2
product_hi = A * B2 (hi)

r2 = r2 + product_lo !
r3 = r3 + product_hi + carry !

# A * B3
product_lo = A * B3
product_hi = A * B3 (hi)

r3 = r3 + product_lo !
r4 = r4 + product_hi + carry !






mask_R = - sign_R
r0 ^= mask_R
r1 ^= mask_R
r2 ^= mask_R
r3 ^= mask_R
r4 ^= mask_R

r0 = r0 + sign_R!
r1 = r1 + carry !
r2 = r2 + carry !
r3 = r3 + carry !
r4 = r4 + carry !

mem64[pointer_R] = r0
mem64[pointer_R + 8] = r1
mem64[pointer_R + 16] = r2
mem64[pointer_R + 24] = r3
mem64[pointer_R + 32] = r4

return
