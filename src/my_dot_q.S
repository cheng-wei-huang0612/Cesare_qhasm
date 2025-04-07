
# qhasm: int32 a

# qhasm: int32 b

# qhasm: int32 r

# qhasm: enter main
.text
.p2align 5
.globl _main
.globl main
_main:
main:
mov %esp,%eax
and $31,%eax
add $0,%eax
sub %eax,%esp

# qhasm: a = 5
# asm 1: mov  $5,>a=int32#1
# asm 2: mov  $5,>a=%eax
mov  $5,%eax

# qhasm: b = 3
# asm 1: mov  $3,>b=int32#2
# asm 2: mov  $3,>b=%ecx
mov  $3,%ecx

# qhasm: r = 0
# asm 1: mov  $0,>r=int32#3
# asm 2: mov  $0,>r=%edx
mov  $0,%edx

# qhasm: r = a + b
# asm 1: lea  (<a=int32#1,<b=int32#2),>r=int32#2
# asm 2: lea  (<a=%eax,<b=%ecx),>r=%ecx
lea  (%eax,%ecx),%ecx

# qhasm: r ^= a
# asm 1: xorl <a=int32#1,<r=int32#2
# asm 2: xorl <a=%eax,<r=%ecx
xorl %eax,%ecx

# qhasm: leave
add %eax,%esp
ret
