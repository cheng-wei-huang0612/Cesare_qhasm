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

enter int128_mul_sch

A_lo = mem64[pointer_A]
A_hi = mem64[pointer_A + 8]
B_lo = mem64[pointer_B]
B_hi = mem64[pointer_B + 8]

sign_A = A_hi >> 63
sign_B = B_hi >> 63

# Take abs(A), branchless
mask_A = - sign_A
A_lo ^= mask_A
A_hi ^= mask_A
A_lo = A_lo + sign_A!
A_hi = A_hi + carry !


# Take abs(B), branchless
mask_B = - sign_B
B_lo ^= mask_B
B_hi ^= mask_B
B_lo = B_lo + sign_B!
B_hi = B_hi + carry !

sign_R = sign_A ^ sign_B




r0 = 0
r1 = 0
r2 = 0
r3 = 0

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