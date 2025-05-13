
# qhasm: int64 input_x0

# qhasm: int64 input_x1

# qhasm: int64 input_x2

# qhasm: int64 input_x3

# qhasm: int64 input_x4

# qhasm: int64 input_x5

# qhasm: int64 input_x6

# qhasm: int64 input_x7

# qhasm: int64 output_x0

# qhasm: int64 calleesaved_x18

# qhasm: int64 calleesaved_x19

# qhasm: int64 calleesaved_x20

# qhasm: int64 calleesaved_x21

# qhasm: int64 calleesaved_x22

# qhasm: int64 calleesaved_x23

# qhasm: int64 calleesaved_x24

# qhasm: int64 calleesaved_x25

# qhasm: int64 calleesaved_x26

# qhasm: int64 calleesaved_x27

# qhasm: int64 calleesaved_x28

# qhasm: int64 calleesaved_x29

# qhasm: reg128 input_v0

# qhasm: reg128 input_v1

# qhasm: reg128 input_v2

# qhasm: reg128 input_v3

# qhasm: reg128 input_v4

# qhasm: reg128 input_v5

# qhasm: reg128 input_v6

# qhasm: reg128 input_v7

# qhasm: reg128 output_v0

# qhasm: reg128 calleesaved_v8

# qhasm: reg128 calleesaved_v9

# qhasm: reg128 calleesaved_v10

# qhasm: reg128 calleesaved_v11

# qhasm: reg128 calleesaved_v12

# qhasm: reg128 calleesaved_v13

# qhasm: reg128 calleesaved_v14

# qhasm: reg128 calleesaved_v15

# qhasm: enter muladd_demo
.align 4
.global _muladd_demo
.global muladd_demo
_muladd_demo:
muladd_demo:

# qhasm: reg128 a

# qhasm: reg128 b

# qhasm: reg128 c

# qhasm: reg128 r

# qhasm: assign v0 to a

# qhasm: assign v1 to b

# qhasm: assign v2 to c

# qhasm: assign v0 to r

# qhasm: 4x r = a * b
# asm 1: mul >r=reg128#4.4s,<a=reg128#1.4s,<b=reg128#2.4s
# asm 2: mul >r=v3.4s,<a=v0.4s,<b=v1.4s
mul v3.4s,v0.4s,v1.4s

# qhasm: 4x r += c
# asm 1: add <r=reg128#4.4s, <r=reg128#4.4s, <c=reg128#3.4s
# asm 2: add <r=v3.4s, <r=v3.4s, <c=v2.4s
add v3.4s, v3.4s, v2.4s

# qhasm: 4x a += b
# asm 1: add <a=reg128#1.4s, <a=reg128#1.4s, <b=reg128#2.4s
# asm 2: add <a=v0.4s, <a=v0.4s, <b=v1.4s
add v0.4s, v0.4s, v1.4s

# qhasm: return
ret
