int64 pointer_A
int64 pointer_B
int64 pointer_R

input pointer_A
input pointer_B
input pointer_R

# 讀取 A, B 各 4 個 64-bit
int64 A0
int64 A1


int64 B0
int64 B1


# 最終乘積可達 512 bits，暫存於 R0..R7
int64 R0
int64 R1
int64 R2
int64 R3


int64 product_lo
int64 product_hi

enter uint128_mul

# Load Data

A0 = mem64[pointer_A]
A1 = mem64[pointer_A + 8]


B0 = mem64[pointer_B]
B1 = mem64[pointer_B + 8]


R0 = 0
R1 = 0
R2 = 0
R3 = 0


product_lo = A0 * B0
product_hi = A0 * B0 (hi)

R0 = R0 + product_lo !
R1 = R1 + product_hi + carry !
R2 = R2 + carry !




product_lo = A0 * B1
product_hi = A0 * B1 (hi)

R1 = R1 + product_lo !
R2 = R2 + product_hi + carry !
R3 = R3 + carry !




product_lo = A1 * B0
product_hi = A1 * B0 (hi)

R1 = R1 + product_lo !
R2 = R2 + product_hi + carry !
R3 = R3 + carry !



product_lo = A1 * B1
product_hi = A1 * B1 (hi)

R2 = R2 + product_lo !
R3 = R3 + product_hi + carry !
# R4 = R4 + carry !




mem64[pointer_R] = R0
mem64[pointer_R +  8] = R1
mem64[pointer_R + 16] = R2
mem64[pointer_R + 24] = R3








return
