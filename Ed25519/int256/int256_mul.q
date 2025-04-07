int64 pointer_A
int64 pointer_B

int64 pointer_R

input pointer_A
input pointer_B

input pointer_R


int64 A_lo
int64 A_hi
int64 B_lo
int64 B_hi
int64 sign_A
int64 sign_B
int64 mask_A
int64 mask_B

int64 r0
int64 r1
int64 r2
int64 r3
int64 sign_R
int64 mask_R

int64 product_lo
int64 product_hi

enter int256_mul

A_0 = mem64[pointer_A]
A_1 = mem64[pointer_A + 8]
A_2 = mem64[pointer_A + 16]
A_3 = mem64[pointer_A + 24]

B_0 = mem64[pointer_B]
B_1 = mem64[pointer_B + 8]
B_2 = mem64[pointer_B + 16]
B_3 = mem64[pointer_B + 24]

sign_A = A_3 >> 63
sign_B = B_3 >> 63

# Take abs(A), branchless
mask_A = - sign_A
A_0 ^= mask_A
A_1 ^= mask_A
A_2 ^= mask_A
A_3 ^= mask_A

A_0 = A_0 + sign_A !
A_1 = A_1 + carry !
A_2 = A_2 + carry !
A_3 = A_3 + carry !

# Take abs(B), branchless
mask_B = - sign_B
B_0 ^= mask_B
B_1 ^= mask_B
B_2 ^= mask_B
B_3 ^= mask_B

B_0 = B_0 + sign_B !
B_1 = B_1 + carry !
B_2 = B_2 + carry !
B_3 = B_3 + carry !

sign_R = sign_A ^ sign_B



r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0

# p0 = A_lo * B_lo
product_lo = A_lo * B_lo
product_hi = A_lo * B_lo (hi)

r0 = r0 + product_lo !
r1 = r1 + product_hi + carry !


# p1 = A_lo * B_hi
product_lo = A_lo * B_hi
product_hi = A_lo * B_hi (hi)



r1 = r1 + product_lo !
r2 = r2 + product_hi + carry !
r3 = r3 + carry !




# p2 = A_hi * B_lo
product_lo = A_hi * B_lo
product_hi = A_hi * B_lo (hi)

r1 = r1 + product_lo !
r2 = r2 + product_hi + carry !
r3 = r3 + carry !






# p3 = A_hi * B_hi
product_lo = A_hi * B_hi
product_hi = A_hi * B_hi (hi)

r2 = r2 + product_lo !
r3 = r3 + product_hi + carry !





mask_R = - sign_R
r0 ^= mask_R
r1 ^= mask_R
r2 ^= mask_R
r3 ^= mask_R

r0 = r0 + sign_R!
r1 = r1 + carry !
r2 = r2 + carry !
r3 = r3 + carry !

mem64[pointer_R] = r0
mem64[pointer_R + 8] = r1
mem64[pointer_R + 16] = r2
mem64[pointer_R + 24] = r3

return