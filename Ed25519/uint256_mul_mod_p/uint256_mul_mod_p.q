int64 pointer_A
int64 pointer_B
int64 pointer_R

input pointer_A
input pointer_B
input pointer_R

# 讀取 A, B 各 4 個 64-bit
int64 A0
int64 A1
int64 A2
int64 A3

int64 B0
int64 B1
int64 B2
int64 B3

# 最終乘積可達 512 bits，暫存於 R0..R7
int64 R0
int64 R1
int64 R2
int64 R3
int64 R4
int64 R5
int64 R6
int64 R7

int64 product_lo
int64 product_hi

enter uint256_mul_mod_p

# Load Data

A0 = mem64[pointer_A]
A1 = mem64[pointer_A + 8]
A2 = mem64[pointer_A + 16]
A3 = mem64[pointer_A + 24]

B0 = mem64[pointer_B]
B1 = mem64[pointer_B + 8]
B2 = mem64[pointer_B + 16]
B3 = mem64[pointer_B + 24]

R0 = 0
R1 = 0
R2 = 0
R3 = 0
R4 = 0
R5 = 0
R6 = 0
R7 = 0

# deal with A0 times B0

product_lo = A0 * B0 
product_hi = A0 * B0 (hi)

R0 = R0 + product_lo
R1 = R1 + product_hi
# At this point, there is no carry


# deal with A0 * B1 and A1 * B0, add from R1

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
# Since the value of R3 is at most 2, no carry should be brought to R4.


# deal with A0 * B2, A1 * B1 and A2 * B0, add from R2

product_lo = A0 * B2
product_hi = A0 * B2 (hi)

R2 = R2 + product_lo !
R3 = R3 + product_hi + carry !
R4 = R4 + carry !

product_lo = A1 * B1
product_hi = A1 * B1 (hi)

R2 = R2 + product_lo !
R3 = R3 + product_hi + carry !
R4 = R4 + carry !

product_lo = A2 * B0
product_hi = A2 * B0 (hi)

R2 = R2 + product_lo !
R3 = R3 + product_hi + carry !
R4 = R4 + carry !

# deal with A0 * B3, A1 * B2, A2 * B1, and A3 * B0 add from R3

product_lo = A0 * B3
product_hi = A0 * B3 (hi)

R3 = R3 + product_lo !
R4 = R4 + product_hi + carry !
R5 = R5 + carry !

product_lo = A1 * B2
product_hi = A1 * B2 (hi)

R3 = R3 + product_lo !
R4 = R4 + product_hi + carry !
R5 = R5 + carry !

product_lo = A2 * B1
product_hi = A2 * B1 (hi)

R3 = R3 + product_lo !
R4 = R4 + product_hi + carry !
R5 = R5 + carry !

product_lo = A3 * B0
product_hi = A3 * B0 (hi)

R3 = R3 + product_lo !
R4 = R4 + product_hi + carry !
R5 = R5 + carry !



# deal with A1 * B3, A2 * B2, and A3 * B1 add from R4

product_lo = A1 * B3
product_hi = A1 * B3 (hi)

R4 = R4 + product_lo !
R5 = R5 + product_hi + carry !
R6 = R6 + carry !

product_lo = A2 * B2
product_hi = A2 * B2 (hi)

R4 = R4 + product_lo !
R5 = R5 + product_hi + carry !
R6 = R6 + carry !

product_lo = A3 * B1
product_hi = A3 * B1 (hi)

R4 = R4 + product_lo !
R5 = R5 + product_hi + carry !
R6 = R6 + carry !



# deal with A2 * B3, and A3 * B2 add from R5


product_lo = A2 * B3
product_hi = A2 * B3 (hi)

R5 = R5 + product_lo !
R6 = R6 + product_hi + carry !
R7 = R7 + carry !

product_lo = A3 * B2
product_hi = A3 * B2 (hi)

R5 = R5 + product_lo !
R6 = R6 + product_hi + carry !
R7 = R7 + carry !



# deal with A3 * B3 add from R6

product_lo = A3 * B3
product_hi = A3 * B3 (hi)

R6 = R6 + product_lo !
R7 = R7 + product_hi + carry !
# R8 = R8 + carry !


# Reduction Modulo 25519





mem64[pointer_R] = R0
mem64[pointer_R +  8] = R1
mem64[pointer_R + 16] = R2
mem64[pointer_R + 24] = R3
mem64[pointer_R + 32] = R4
mem64[pointer_R + 40] = R5
mem64[pointer_R + 48] = R6
mem64[pointer_R + 56] = R7




return