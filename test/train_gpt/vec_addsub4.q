enter muladd_demo

reg128 a
reg128 b
reg128 c
reg128 r

# assume: a = input_v0, b = input_v1, c = input_v2
assign v0 to a
assign v1 to b
assign v2 to c
# return in v0
assign v0 to r

# r = a * b + c
4x r = a * b
4x r += c
4x a += b

return

