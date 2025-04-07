int64 pointer_A
int64 pointer_B
int64 pointer_R

input pointer_A
input pointer_B
input pointer_R

# 讀取 A, B 各 4 個 64-bit
int64 A0

int64 B0



# 最終乘積可達 512 bits，暫存於 R0..R7
int64 R0
int64 R1



int64 product_lo
int64 product_hi

enter uint64_mul

# Load Data

A0 = mem64[pointer_A]



B0 = mem64[pointer_B]



R0 = 0
R1 = 0



product_lo = A0 * B0
product_hi = A0 * B0 (hi)

R0 = R0 + product_lo !
R1 = R1 + product_hi + carry !
# R2 = R2 + carry !






mem64[pointer_R] = R0
mem64[pointer_R +  8] = R1









return
