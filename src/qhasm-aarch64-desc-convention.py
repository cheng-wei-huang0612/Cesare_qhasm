#!/usr/bin/python3



stackalign = True


#
# registers
#

#AArch64 has 31 x 64-bit general purpose Arm registers 
# and 1 special register having different names, depending on the context in which it is used. 
# These registers can be viewed as either 31 x 64-bit registers (X0-X30) 
# or as 31 x 32-bit registers (W0-W30).

# x31 (SP): Stack pointer or a zero register, depending on context.
# x30 (LR): Procedure link register, used to return from subroutines.
# x29 (FP): Frame pointer. (callee-saved)


print( ':name:int32:w0:w1:w2:w3:w4:w5:w6:w7:w8:w9:w10:w11:w12:w13:w14:w15:w16:w17:w18:w19:w20:w21:w22:w23:w24:w25:w26:w27:w28:w29:' )
#print( ':name:int32:w0:w1:w2:w3:w4:w5:w6:w7:w8:w9:w10:w11:w12:w13:w14:w15:w16:w17:w19:w20:w21:w22:w23:w24:w25:w26:w27:w28:w29:' )
print( 'new r:>r=int32:' )
print( 'int32 r:var/r=int32:' )

print( ':name:int64:x0:x1:x2:x3:x4:x5:x6:x7:x8:x9:x10:x11:x12:x13:x14:x15:x16:x17:x18:x19:x20:x21:x22:x23:x24:x25:x26:x27:x28:x29:' )
#print( ':name:int64:x0:x1:x2:x3:x4:x5:x6:x7:x8:x9:x10:x11:x12:x13:x14:x15:x16:x17:x19:x20:x21:x22:x23:x24:x25:x26:x27:x28:x29:' )
print( 'new r:>r=int64:' )
print( 'int64 r:var/r=int64:' )

print( ':name:reg64:r0:r1:r2:r3:r4:r5:r6:r7:r8:r9:r10:r11:r12:r13:r14:r15:r16:r17:r18:r19:r20:r21:r22:r23:r24:r25:r26:r27:r28:r29:' )
print( 'new r:>r=reg64:' )
print( 'reg64 r:var/r=reg64:' )


#AArch64 has 32 x 128-bit NEON registers (V0-V31). 
# These registers can also be viewed as 32-bit Sn registers or 64-bit Dn registers.

#print( ':name:reg128:q0:q1:q2:q3:q4:q5:q6:q7:q8:q9:q10:q11:q12:q13:q14:q15:q16:q17:q18:q19:q20:q21:q22:q23:q24:q25:q26:q27:q28:q29:q30:q31:' )
print( ':name:reg128:v0:v1:v2:v3:v4:v5:v6:v7:v8:v9:v10:v11:v12:v13:v14:v15:v16:v17:v18:v19:v20:v21:v22:v23:v24:v25:v26:v27:v28:v29:v30:v31:' )
print( 'new r:>r=reg128:' )
print( 'free r:<r=reg128:' )
print( 'int128 r:var/r=reg128:' )
print( 'reg128 r:var/r=reg128:' )
print( 'fp128 r:var/r=reg128:' )



for i in range(0,29):
  print( 'assign x%d to r:<r=int64#%d:' % (i,i+1) )

for i in range(0,31):
  print( 'assign v%d to r:<r=reg128#%d:' % (i,i+1) )



# Don't know what this is
# print( ":".join([
# 'startcode',
# 'asm/.fpu neon',
# 'asm/.text',
# ]) )




# The 64-bit ARM (AArch64) calling convention allocates the 31 general-purpose registers as:[2]

# x31 (SP): Stack pointer or a zero register, depending on context.
# x30 (LR): Procedure link register, used to return from subroutines.
# x29 (FP): Frame pointer.
# x19 to x29: Callee-saved.
# x18 (PR): Platform register. Used for some operating-system-specific special purpose, or an additional caller-saved register.
# x16 (IP0) and x17 (IP1): Intra-Procedure-call scratch registers.
# x9 to x15: Local variables, caller saved.
# x8 (XR): Indirect return value address.
# x0 to x7: Argument values passed to and results returned from a subroutine.
# All registers starting with x have a corresponding 32-bit register prefixed with w. 
# Thus, a 32-bit x0 is called w0.

# Similarly, the 32 floating-point registers are allocated as:[3]

# v0 to v7: Argument values passed to and results returned from a subroutine.
# v8 to v15: callee-saved, but only the bottom 64 bits need to be preserved.
# v16 to v31: Local variables, caller saved.


print( ':caller:int64:19:20:21:22:23:24:25:26:27:28:29:30:' )
print( ':caller:reg128:9:10:11:12:13:14:15:16:' )

print( 'input r:input/r:' )
print( 'output r:output/r:' )
print( 'caller r:caller/r:' )


# for i in range(0,8):
#   print( 'aarch64pcs_x%d input_x%d:>input_x%d=int64#%d:asm/_aarch64pcs_input_x%d!colon:'%(i,i,i,i+1,i) )

# for i in range(18,30):
#   print( 'aarch64pcs_x%d calleesaved_x%d:>calleesaved_x%d=int64#%d:asm/_aarch64pcs_calleesaved_x%d!colon:'%(i,i,i,i+1,i) )

# for i in range(0,8):
#   print( 'aarch64pcs_v%d input_v%d:>input_v%d=reg128#%d:asm/_aarch64pcs_input_v%d!colon:'%(i,i,i,i+1,i) )

# for i in range(8,16):
#   print( 'aarch64pcs_v%d calleesaved_v%d:>calleesaved_v%d=reg128#%d:asm/_aarch64pcs_calleesaved_v%d!colon:'%(i,i,i,i+1,i) )



print( ":".join([
'enter f',
'enter/f',
'asm/.align 4',
'asm/.global _#f',
'asm/.global #f',
'asm/_#f!colon',
'asm/#f!colon',
#'>input_x0=int64#1',
#'>input_x1=int64#2',
#'asm/sub sp,sp,$!frame',
'',
]) )


# print( ":".join([
# 'enternostack f',
# 'enter/f',
# 'asm/.align 4',
# 'asm/.global _#f',
# 'asm/.global #f',
# 'asm/.type _#f STT_FUNC',
# 'asm/.type #f STT_FUNC',
# 'asm/_#f!colon',
# 'asm/#f!colon',
# '',
# ]) )



print( ":".join([
'return',
'nofallthrough',
'asm/ret',
'leave',
'',
]) )



# print( ":".join([
# 'return r',
# 'nofallthrough',
# #'asm/add sp,sp,$!frame',
# '<r=int64',
# 'asm/mov x0,<r',
# 'asm/ret',
# 'leave',
# '',
# ]) )


# print( ":".join([
# 'returnq r',
# 'nofallthrough',
# #'asm/add sp,sp,$!frame',
# '<r=reg128',
# 'asm/mov v0, <r',
# 'asm/ret',
# 'leave',
# '',
# ]) )



# print( ":".join([
# 'qpopreturn',
# 'nofallthrough',
# #  [ $stackalign ] && echo 
# 'asm/mov sp,r12',
# #  [ $stackalign ] || echo 'asm/add sp,sp,$!frame'
# 'asm/vpop {q4,q5,q6,q7}',
# 'asm/bx lr',
# '<caller_r4=int32#5',
# '<caller_r5=int32#6',
# '<caller_r6=int32#7',
# '<caller_r7=int32#8',
# '<caller_r8=int32#9',
# '<caller_r9=int32#10',
# '<caller_r10=int32#11',
# '<caller_r11=int32#12',
# #  [ $stackalign ] && echo 
# '<caller_r12=int32#13',
# '<caller_r14=int32#14',
# 'leave',
# ]) )


# print( ":".join([
# 'qpopreturn r',
# 'nofallthrough',
# #  [ $stackalign ] && echo 
# 'asm/mov sp,r12',
# #  [ $stackalign ] || echo 'asm/add sp,sp,$!frame'
# 'asm/vpop {q4,q5,q6,q7}',
# 'asm/bx lr',
# '<r=int32#1',
# '<caller_r4=int32#5',
# '<caller_r5=int32#6',
# '<caller_r6=int32#7',
# '<caller_r7=int32#8',
# '<caller_r8=int32#9',
# '<caller_r9=int32#10',
# '<caller_r10=int32#11',
# '<caller_r11=int32#12',
# #  [ $stackalign ] && echo 
# '<caller_r12=int32#13',
# '<caller_r14=int32#14',
# 'leave',
# ]) )





#print( ':flag:=:' )
#print( ':flag:signed<:' )
#print( ':flag:signed>:' )
#print( ':flag:unsigned<:' )
#print( ':flag:unsigned>:' )
print( ':flag:negative:' )
print( ':flag:carry:' )
print( ':flag:overflow:' )
print( ':flag:zero:' )



print( 'cycles(r):>r=int32:asm/mrc p15, 0, >r, c9, c13, 0:' )
print( 'f#:#f:label/f:asm/._#f!colon:' )

#
# goto 
#

print( 'goto f:#f:nofallthrough:jump/f:asm/b ._#f:' )

print( 'goto f if r == 0:#f:jump/f:<r=int64:asm/cbz  <r , ._#f:' )
print( 'goto f if r != 0:#f:jump/f:<r=int64:asm/cbnz <r , ._#f:' )
print( 'goto f if r == 0:#f:jump/f:<r=int32:asm/cbz  <r , ._#f:' )
print( 'goto f if r != 0:#f:jump/f:<r=int32:asm/cbnz <r , ._#f:' )

print( 'goto f if r[n/64] == 0:#f:jump/f:<r=int64:#n:asm/tbz  <r  , $#n , ._#f:' )
print( 'goto f if r[n/64] != 0:#f:jump/f:<r=int64:#n:asm/tbnz <r , $#n , ._#f:' )
print( 'goto f if r[n/32] == 0:#f:jump/f:<r=int32:#n:asm/tbz  <r  , $#n , ._#f:' )
print( 'goto f if r[n/32] != 0:#f:jump/f:<r=int32:#n:asm/tbnz <r , $#n , ._#f:' )


#
# branch with flags
#
# meaning                         cmp     A, B            sign            flags
# ------------------------------- ------- --------------- --------------- -------------------
# equal                           eq      A == B          -               Z == 1
# not equal                       ne      A != B          -               Z == 0
# -------------------------------
print( 'goto f if =:#f:jump/f:<?zero:asm/b.eq ._#f:' )
print( 'goto f if ==:#f:jump/f:<?zero:asm/b.eq ._#f:' )
print( 'goto f if !=:#f:jump/f:<?zero:asm/b.ne ._#f:' )

# carry set                       cs,hs   A >= B          unsigned        C == 1
# carry clear                     cc,lo   A < B           unsigned        C == 0
# higher                          hi      A > B           unsigned        C == 1 && Z == 0
# lower or same                   ls      A <= B          unsigned        !(C == 1 && Z == 0)
# -------------------------------
print( 'goto f if carry:#f:jump/f:<?carry:asm/b.cs ._#f:' )
print( 'goto f if !carry:#f:jump/f:<?carry:asm/b.cc ._#f:' )
print( 'goto f if unsigned>=:#f:jump/f:<?carry:asm/b.hs ._#f:' )
print( 'goto f if !unsigned<:#f:jump/f:<?carry:asm/b.hs ._#f:' )
print( 'goto f if unsigned<:#f:jump/f:<?carry:asm/b.lo ._#f:' )
print( 'goto f if unsigned>:#f:jump/f:<?carry:<?zero:asm/b.hi ._#f:' )
print( 'goto f if !unsigned>:#f:jump/f:<?carry:<?zero:asm/b.ls ._#f:' )
print( 'goto f if unsigned<=:#f:jump/f:<?carry:<?zero:asm/b.ls ._#f:' )

# greater than or equal           ge      A >= B          signed          N == V
# less than                       lt      A < B           signed          N != V
# greater than                    gt      A > B           signed          Z == 0 && N == V
# less than or equal              le      A <= B          signed          !(Z == 0 && N == V)
# -------------------------------
print( 'goto f if signed<:#f:jump/f:<?negative:<?overflow:asm/b.lt ._#f:' )
print( 'goto f if <:#f:jump/f:<?negative:<?overflow:asm/b.lt ._#f:' )
print( 'goto f if !signed<:#f:jump/f:<?negative:<?overflow:asm/b.ge ._#f:' )
print( 'goto f if signed>=:#f:jump/f:<?negative:<?overflow:asm/b.ge ._#f:' )
print( 'goto f if >=:#f:jump/f:<?negative:<?overflow:asm/b.ge ._#f:' )

print( 'goto f if signed>:#f:jump/f:<?negative:<?overflow:<?zero:asm/b.gt ._#f:' )
print( 'goto f if >:#f:jump/f:<?negative:<?overflow:<?zero:asm/b.gt ._#f:' )
print( 'goto f if !signed>:#f:jump/f:<?negative:<?overflow:<?zero:asm/b.le ._#f:' )
print( 'goto f if signed<=:#f:jump/f:<?negative:<?overflow:<?zero:asm/b.le ._#f:' )

# minus, negative                 mi      A < B           -               N == 1
# plus or zero                    pl      A >= B          -               N == 0
# -------------------------------
print( 'goto f if negative:#f:jump/f:<?negative:asm/b.mi ._#f:' )
print( 'goto f if !negative:#f:jump/f:<?negative:asm/b.pl ._#f:' )

# overflow set                    vs      -               -               V == 1
# overflow clear                  vc      -               -               V == 0









print( 'constant s#:#s:asm/.p2align 4:asm/#s!colon:' )
print( 'const32 n:#n:asm/.word #n:' )
print( 'const128 n m o p:#n:#m:#o:#p:asm/.word #n,#m,#o,#p:' )

print( ':stackalign:32:' )
print( ':stackname:[sp,#:]:' )
#if stackalign : print( ':stackargname:[r12,#:]:' )
#if stackalign : print( ':rightbytes:0:' )

# XXX have to upgrade stackargusescaller to handle r12
# [ $stackalign ] || echo ':stackargname:[sp,#:]:'
# [ $stackalign ] || echo ':rightbytes:!frame+0:'

print( ':stackbytes:stack64:8:' )
print( 'stack64 r:var/r=stack64:' )
print( 'new r:>r=stack64:' )

print( ':stackbytes:stack32:4:' )
print( 'stack32 r:var/r=stack32:' )
print( 'new r:>r=stack32:' )

print( ':stackbytes:stack128:16:' )
print( 'stack128 r:var/r=stack128:' )
print( 'new r:>r=stack128:' )

print( ':stackbytes:stack256:32:' )
print( 'stack256 r:var/r=stack256:' )
print( 'new r:>r=stack256:' )

print( ':stackbytes:stack512:64:' )
print( 'stack512 r:var/r=stack512:' )
print( 'new r:>r=stack512:' )

print( ':stackbytes:stack1024:128:' )
print( 'stack1024 r:var/r=stack1024:' )
print( 'new r:>r=stack1024:' )

print( ':stackbytes:stack1600:200:' )
print( 'stack1600 r:var/r=stack1600:' )
print( 'new r:>r=stack1600:' )

print( ':stackbytes:stack3072:384:' )
print( 'stack3072 r:var/r=stack3072:' )
print( 'new r:>r=stack3072:' )

print( ':stackpriority:stack64:' )




#
#
# Instructions
# Perhaps better to use another scripts
#
#

#
#  64-bit instructions
#

# n can be 16 bits
print( 'r = n:>r=int64:#n:asm/mov >r, $#n:' )
print( 'r[0/4] = n:inplace>r=int64:<r=int64:#n:asm/movk <r, $#n:' )
print( 'r[1/4] = n:inplace>r=int64:<r=int64:#n:asm/movk <r, $#n,LSL $16:' )
print( 'r[2/4] = n:inplace>r=int64:<r=int64:#n:asm/movk <r, $#n,LSL $32:' )
print( 'r[3/4] = n:inplace>r=int64:<r=int64:#n:asm/movk <r, $#n,LSL $48:' )


print( 'r = t:>r=int64:<t=int64:asm/mov >r,<t:' )
print( 'r ^= t:>r=int64:<r=int64:<t=int64:asm/eor >r,<r,<t:' )
print( 'r &= t:>r=int64:<r=int64:<t=int64:asm/and >r, <r, <t:' )
print( 'r &= ~t:>r=int64:<r=int64:<t=int64:asm/bic >r,<r,<t:' )
print( 'r |= t:>r=int64:<r=int64:<t=int64:asm/orr >r,<r,<t:' )
print( 'r |= ~t:>r=int64:<r=int64:<t=int64:asm/orn >r,<r,<t:' )

# Cesare says
print("r = t & s:>r=int64:<t=int64:<s=int64:asm/and  >r, <t, <s:")
print("r = t & n:>r=int64:<t=int64:#n:asm/and >r, <t, $#n:")

print("r = t & s:>r=int32:<t=int32:<s=int32:asm/and  >r, <t, <s:")
print("r = t & n:>r=int32:<t=int32:#n:asm/and >r, <t, $#n:")

print( 'r = t ^ s:>r=int64:<t=int64:<s=int64:asm/eor >r,<t,<s:' )
print( 'r = t ^ n:>r=int64:<t=int64:#n:asm/eor >r,<t,$#n:' )

print( 'r = t | s:>r=int64:<t=int64:<s=int64:asm/orr >r, <t, <s: ')

# Seems does not work
print( 'r = |t|:>r=int64:<t=int64:asm/abs >r, <t' )





print( 'r = s:>r=int64:<s=stack64:asm/ldr >r, <s:' )
print( 's = r:<r=int64:>s=stack64:asm/str <r, >s:' )
print( 'r = mem64[&s]:>r=int64:<s=stack64:asm/ldr >r, <s:' )
print( 'r = mem64[&s+8]:>r=int64:<s=stack64:asm/ldr >r, !shift8<s:' )
print( 'mem64[&s] = r:inplace>s=stack64:<r=int64:<s=stack64:asm/str <r, <s:' )
print( 'mem64[&s+8] = r:inplace>s=stack64:<r=int64:<s=stack64:asm/str <r, !shift8<s:' )

# Cesare says
## Load a 64-bit value from memory
print( 'r = mem64[s+n]:>r=int64:<s=int64:#n:asm/ldr >r, [<s, $#n]:')
print( 'r = mem64[s]:>r=int64:<s=int64:asm/ldr >r, [<s]:')
## Store a 64-bit value to memory
print('mem64[s+n] = r:<s=int64:#n:<r=int64:asm/str <r, [<s, $#n]:')
print('mem64[s] = r:<s=int64:<r=int64:asm/str <r, [<s]:')


# LDP for 2x64bit numbers
print( 'r, s = mem128[t]:>r=int64:>s=int64:<t=int64:asm/ldp >r, >s, [<t]' )
print( 'r, s = mem128[t+n]:>r=int64:>s=int64:<t=int64:#n:asm/ldp >r, >s, [<t, $#n]' )

# LDP for 2x32bit numbers
print( 'r, s = mem64[t]:>r=int32:>s=int32:<t=int64:asm/ldp >r, >s, [<t]' )
print( 'r, s = mem64[t+n]:>r=int32:>s=int32:<t=int64:#n:asm/ldp >r, >s, [<t, $#n]' )



print( 'r = t + n:>r=int64:<t=int64:#n:asm/add >r,<t,$#n:' )
print( 'r = t + s:>r=int64:<t=int64:<s=int64:asm/add >r,<t,<s:' )
print( 'r += n:inplace>r=int64:<r=int64:#n:asm/add <r,<r,$#n:' )
print( 'r += s:inplace>r=int64:<r=int64:<s=int64:asm/add <r,<r,<s:' )
print( 'r = t + s << n:>r=int64:<t=int64:<s=int64:#n:asm/add >r,<t,<s,LSL $#n:' )
print( 'r = t + s >> n:>r=int64:<t=int64:<s=int64:#n:asm/add >r,<t,<s,ASR $#n:' )
print( 'r = t + s unsigned>> n:>r=int64:<t=int64:<s=int64:#n:asm/add >r,<t,<s,LSR $#n:' )

print( 'r = t - n:>r=int64:<t=int64:#n:asm/sub >r,<t,$#n:' )
print( 'r = t - s:>r=int64:<t=int64:<s=int64:asm/sub >r,<t,<s:' )
print( 'r -= n:inplace>r=int64:<r=int64:#n:asm/sub <r,<r,$#n:' )
print( 'r -= s:inplace>r=int64:<r=int64:<s=int64:asm/sub <r,<r,<s:' )
print( 'r = t - s << n:>r=int64:<t=int64:<s=int64:#n:asm/sub >r,<t,<s,LSL $#n:' )
print( 'r = t - s >> n:>r=int64:<t=int64:<s=int64:#n:asm/sub >r,<t,<s,ASR $#n:' )
print( 'r = t - s unsigned>> n:>r=int64:<t=int64:<s=int64:#n:asm/sub >r,<t,<s,LSR $#n:' )

# Cesare says
print( 'r = -s:>r=int64:<s=int64:asm/neg >r,<s' )


# Cesare says
# 64-bit multiplication
print( 'r = t * s:>r=int64:<t=int64:<s=int64:asm/mul >r,<t,<s' )
print( 'r = t * s (hi):>r=int64:<t=int64:<s=int64:asm/umulh >r, <t, <s' )
print( 'r = t unsigned* s (hi):>r=int64:<t=int64:<s=int64:asm/umulh >r, <t, <s' )
print( 'r = t signed* s (hi):>r=int64:<t=int64:<s=int64:asm/smulh >r, <t, <s' )

print( 'r = t * s + u:>r=int64:<t=int64:<s=int64:<u=int64:asm/madd >r, <t, <s, <u' )
print( 'r = u + t * s:>r=int64:<t=int64:<s=int64:<u=int64:asm/madd >r, <t, <s, <u' )






#
# XXX: don't know how to make qhasm work correctly with flags
#
# print( 'r = t + n !:>r=int64:<t=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,$#n:' )
# print( 'r += n !:inplace>r=int64:<r=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds <r,<r,$#n:' )
# print( 'r = t + s !:>r=int64:<t=int64:<s=int64:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s:' )
# print( 'r = t + s << n !:>r=int64:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s,LSL $#n:' )
# print( 'r = t + s >> n !:>r=int64:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s,ASR $#n:' )
# print( 'r = t + s unsigned>> n !:>r=int64:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s,LSR $#n:' )

# print( 'r = t - n !:>r=int64:<t=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,$#n:' )
# print( 'r -= n !:inplace>r=int64:<r=int64:>?negative:>?carry:>?overflow:>?zero:#n:asm/subs <r,<r,$#n:' )
# print( 'r = t - s !:>r=int64:<t=int64:<s=int64:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s:' )
# print( 'r = t - s << n !:>r=int64:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s,LSL $#n:' )
# print( 'r = t - s >> n !:>r=int64:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s,ASR $#n:' )
# print( 'r = t - s unsigned>> n !:>r=int64:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s,LSR $#n:' )

# print( 't - n !:<t=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,$#n:' )
# print( 't - s !:<t=int64:<s=int64:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s:' )
# print( 't - s << n !:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSL $#n:' )
# print( 't - s >> n !:><t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,ASR $#n:' )
# print( 't - s unsigned>> n !:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSR $#n:' )

# print( 't - n:<t=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,$#n:' )
# print( 't - s:<t=int64:<s=int64:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s:' )
# print( 't - s << n:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSL $#n:' )
# print( 't - s >> n:><t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,ASR $#n:' )
# print( 't - s unsigned>> n:<t=int64:<s=int64:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSR $#n:' )



print( 'r = t + n !:>r=int64:<t=int64:#n:asm/adds >r,<t,$#n:' )
print( 'r += n !:inplace>r=int64:<r=int64:#n:asm/adds <r,<r,$#n:' )
# Cesare says
print( 'r += s !:inplace>r=int64:<r=int64:<s=int64:asm/adds <r, <r, <s:' )
#
print( 'r = t + s !:>r=int64:<t=int64:<s=int64:asm/adds >r,<t,<s:' )
print( 'r = t + s << n !:>r=int64:<t=int64:<s=int64:#n:asm/adds >r,<t,<s,LSL $#n:' )
print( 'r = t + s >> n !:>r=int64:<t=int64:<s=int64:#n:asm/adds >r,<t,<s,ASR $#n:' )
print( 'r = t + s unsigned>> n !:>r=int64:<t=int64:<s=int64:#n:asm/adds >r,<t,<s,LSR $#n:' )

# Cesare says

print( 'r = t + s + carry :>r=int64:<t=int64:<s=int64:asm/adc >r,<t,<s:' )
print( 'r = t + s + carry !:>r=int64:<t=int64:<s=int64:asm/adcs >r,<t,<s:' )
print( 'r = t + carry !:>r=int64:<t=int64:asm/adcs >r,<t, xzr:' )
print( 'r += carry !:>r=int64:asm/adcs >r,<r, xzr:' )
print( 'clear carry!:>r=int64:<t=int64:asm/adcs xzr, xzr, xzr:' )





print( 'r = t - n !:>r=int64:<t=int64:#n:asm/subs >r,<t,$#n:' )
print( 'r -= n !:inplace>r=int64:<r=int64:#n:asm/subs <r,<r,$#n:' )
print( 'r = t - s !:>r=int64:<t=int64:<s=int64:asm/subs >r,<t,<s:' )
print( 'r = t - s << n !:>r=int64:<t=int64:<s=int64:#n:asm/subs >r,<t,<s,LSL $#n:' )
print( 'r = t - s >> n !:>r=int64:<t=int64:<s=int64:#n:asm/subs >r,<t,<s,ASR $#n:' )
print( 'r = t - s unsigned>> n !:>r=int64:<t=int64:<s=int64:#n:asm/subs >r,<t,<s,LSR $#n:' )

# Cesare says
print( 'r = t - n - borrow!:>r=int64:<t=int64:#n:asm/sbcs >r,<t,$#n:' )
print( 'r -= n  - borrow!:inplace>r=int64:<r=int64:#n:asm/sbcs <r,<r,$#n:' )
print( 'r = t - s  - borrow!:>r=int64:<t=int64:<s=int64:asm/sbcs >r,<t,<s:' )
print( 'r = t - s << n - borrow!:>r=int64:<t=int64:<s=int64:#n:asm/sbcs >r,<t,<s,LSL $#n:' )
print( 'r = t - s >> n - borrow!:>r=int64:<t=int64:<s=int64:#n:asm/sbcs >r,<t,<s,ASR $#n:' )
print( 'r = t - borrow!:>r=int64:<t=int64:asm/sbcs >r,<t,xzr:' )



print( 't - n !:<t=int64:#n:asm/cmp <t,$#n:' )
print( 't - s !:<t=int64:<s=int64:asm/cmp <t,<s:' )
print( 't - s << n !:<t=int64:<s=int64:#n:asm/cmp <t,<s,LSL $#n:' )
print( 't - s >> n !:><t=int64:<s=int64:#n:asm/cmp <t,<s,ASR $#n:' )
print( 't - s unsigned>> n !:<t=int64:<s=int64:#n:asm/cmp <t,<s,LSR $#n:' )

print( 't - n:<t=int64:#n:asm/cmp <t,$#n:' )
print( 't - s:<t=int64:<s=int64:asm/cmp <t,<s:' )
print( 't - s << n:<t=int64:<s=int64:#n:asm/cmp <t,<s,LSL $#n:' )
print( 't - s >> n:><t=int64:<s=int64:#n:asm/cmp <t,<s,ASR $#n:' )
print( 't - s unsigned>> n:<t=int64:<s=int64:#n:asm/cmp <t,<s,LSR $#n:' )



#
#  32-bit instructions
#

print( 'r = n:>r=int32:#n:asm/mov >r, $#n:' )
print( 'r = s:>r=int32:<s=int32:asm/mov >r, <s:' )

print( 'r = s:>r=int32:<s=stack32:asm/ldr >r,<s:' )
print( 's = r:<r=int32:>s=stack32:asm/str <r, >s:' )
print( 'r = mem32[&s]:>r=int32:<s=stack64:asm/ldr >r,<s:' )
print( 'r = mem32[&s+4]:>r=int32:<s=stack64:asm/ldr >r,!shift4<s:' )
print( 'mem32[&s] = r:inplace>s=stack64:<r=int32:<s=stack64:asm/str <r, <s:' )
print( 'mem32[&s+4] = r:inplace>s=stack64:<r=int32:<s=stack64:asm/str <r, !shift4<s:' )

print( 'r += n:inplace>r=int32:<r=int32:#n:asm/add <r,<r,$#n:' )
print( 'r = t + n:>r=int32:<t=int32:#n:asm/add >r,<t,$#n:' )
print( 'r = t + s:>r=int32:<t=int32:<s=int32:asm/add >r,<t,<s:' )
print( 'r += s:inplace>r=int32:<r=int32:<s=int32:asm/add <r,<r,<s:' )
print( 'r = t + s << n:>r=int32:<t=int32:<s=int32:#n:asm/add >r,<t,<s,LSL $#n:' )

# This is broken
print( 'r += s << n:inplace>r=int32:<r=int32:<s=int32:#n:asm/add >r,<r,<s,LSL $#n:' )

print( 'r = t + s >> n:>r=int32:<t=int32:<s=int32:#n:asm/add >r,<t,<s,ASR $#n:' )
print( 'r = t + s unsigned>> n:>r=int32:<t=int32:<s=int32:#n:asm/add >r,<t,<s,LSR $#n:' )

print( 'r = t - n:>r=int32:<t=int32:#n:asm/sub >r,<t,$#n:' )
print( 'r -= n:inplace>r=int32:<r=int32:#n:asm/sub <r,<r,$#n:' )
print( 'r = t - s:>r=int32:<t=int32:<s=int32:asm/sub >r,<t,<s:' )
print( 'r -= s:inplace>r=int32:<r=int32:<s=int32:asm/sub <r,<r,<s:' )
print( 'r = t - s << n:>r=int32:<t=int32:<s=int32:#n:asm/sub >r,<t,<s,LSL $#n:' )
print( 'r = t - s >> n:>r=int32:<t=int32:<s=int32:#n:asm/sub >r,<t,<s,ASR $#n:' )
print( 'r = t - s unsigned>> n:>r=int32:<t=int32:<s=int32:#n:asm/sub >r,<t,<s,LSR $#n:' )


# Cesare says: 32-bit multiplication 

print("r = t * s:>r=int32:<t=int32:<s=int32:asm/mul >r,<t,<s")
print("r = t * s:>r=int64:<t=int32:<s=int32:asm/umull >r,<t,<s")
#print("r = t * s (hi):>r=int32l:<t=int32:<s=int32:asm/umulh >r,<t,<s")

print( 'r = mem32[s]:>r=int32:<s=int64:asm/ldr >r, [<s]:' )
print( 'r = mem32[s+4]:>r=int32:<s=int64:asm/ldr >r, [<s, 4]:' )
print( 'r = mem32[s+n]:>r=int32:<s=int64:#n:asm/ldr >r, [<s, $#n]:' )

print( 'r = mem32[s]:>r=int64:<s=int64:asm/ldr >r%wregname, [<s]:' )
print( 'r = mem32[s+4]:>r=int64:<s=int64:asm/ldr >r%wregname, [<s, 4]:' )
print( 'r = mem32[s+n]:>r=int64:<s=int64:#n:asm/ldr >r%wregname, [<s, $#n]:' )

print('mem32[s+n] = r:<s=int64:#n:<r=int32:asm/str <r, [<s, $#n]:')
print('mem32[s] = r:<s=int64:<r=int32:asm/str <r, [<s]:')

# store the 32bits value of a int64 into memory
print('mem32[s] = r:<s=int64:<r=int64:asm/str <r%wregname, [<s]:')
print('mem32[s+n] = r:<s=int64:<r=int64:#n:asm/str <r%wregname, [<s, $#n]:')


#
# XXX: don't know how to make qhasm work correctly with flags
#
# print( 'r = t + n !:>r=int32:<t=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,$#n:' )
# print( 'r += n !:inplace>r=int32:<r=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds <r,<r,$#n:' )
# print( 'r = t + s !:>r=int32:<t=int32:<s=int32:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s:' )
# print( 'r = t + s << n !:>r=int32:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s,LSL $#n:' )
# print( 'r = t + s >> n !:>r=int32:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s,ASR $#n:' )
# print( 'r = t + s unsigned>> n !:>r=int32:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/adds >r,<t,<s,LSR $#n:' )

# print( 'r = t - n !:>r=int32:<t=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,$#n:' )
# print( 'r -= n !:inplace>r=int32:<r=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs <r,<r,$#n:' )
# print( 'r = t - s !:>r=int32:<t=int32:<s=int32:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s:' )
# print( 'r = t - s << n !:>r=int32:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s,LSL $#n:' )
# print( 'r = t - s >> n !:>r=int32:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s,ASR $#n:' )
# print( 'r = t - s unsigned>> n !:>r=int32:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/subs >r,<t,<s,LSR $#n:' )

# print( 't - n !:<t=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,$#n:' )
# print( 't - s !:<t=int32:<s=int32:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s:' )
# print( 't - s << n !:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSL $#n:' )
# print( 't - s >> n !:><t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,ASR $#n:' )
# print( 't - s unsigned>> n !:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSR $#n:' )

# print( 't - n:<t=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,$#n:' )
# print( 't - s:<t=int32:<s=int32:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s:' )
# print( 't - s << n:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSL $#n:' )
# print( 't - s >> n:><t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,ASR $#n:' )
# print( 't - s unsigned>> n:<t=int32:<s=int32:#n:>?negative:>?carry:>?overflow:>?zero:asm/cmp <t,<s,LSR $#n:' )


print( 'r = t + n !:>r=int32:<t=int32:#n:asm/adds >r,<t,$#n:' )
print( 'r += n !:inplace>r=int32:<r=int32:#n:asm/adds <r,<r,$#n:' )
print( 'r = t + s !:>r=int32:<t=int32:<s=int32:asm/adds >r,<t,<s:' )
print( 'r = t + s << n !:>r=int32:<t=int32:<s=int32:#n:asm/adds >r,<t,<s,LSL $#n:' )
print( 'r += s << n !:inplace>r=int32:<r=int32:<s=int32:#n:asm/adds >r,<r,<s,LSL $#n:' )
print( 'r = t + s >> n !:>r=int32:<t=int32:<s=int32:#n:asm/adds >r,<t,<s,ASR $#n:' )
print( 'r = t + s unsigned>> n !:>r=int32:<t=int32:<s=int32:#n:asm/adds >r,<t,<s,LSR $#n:' )

print( 'r = t - n !:>r=int32:<t=int32:#n:asm/subs >r,<t,$#n:' )
print( 'r -= n !:inplace>r=int32:<r=int32:#n:asm/subs <r,<r,$#n:' )
print( 'r = t - s !:>r=int32:<t=int32:<s=int32:asm/subs >r,<t,<s:' )
print( 'r = t - s << n !:>r=int32:<t=int32:<s=int32:#n:asm/subs >r,<t,<s,LSL $#n:' )
print( 'r = t - s >> n !:>r=int32:<t=int32:<s=int32:#n:asm/subs >r,<t,<s,ASR $#n:' )
print( 'r = t - s unsigned>> n !:>r=int32:<t=int32:<s=int32:#n:asm/subs >r,<t,<s,LSR $#n:' )

print( 't - n !:<t=int32:#n:asm/cmp <t,$#n:' )
print( 't - s !:<t=int32:<s=int32:asm/cmp <t,<s:' )
print( 't - s << n !:<t=int32:<s=int32:#n:asm/cmp <t,<s,LSL $#n:' )
print( 't - s >> n !:><t=int32:<s=int32:#n:asm/cmp <t,<s,ASR $#n:' )
print( 't - s unsigned>> n !:<t=int32:<s=int32:#n:asm/cmp <t,<s,LSR $#n:' )

print( 't - n:<t=int32:#n:asm/cmp <t,$#n:' )
print( 't - s:<t=int32:<s=int32:asm/cmp <t,<s:' )
print( 't - s << n:<t=int32:<s=int32:#n:asm/cmp <t,<s,LSL $#n:' )
print( 't - s >> n:><t=int32:<s=int32:#n:asm/cmp <t,<s,ASR $#n:' )
print( 't - s unsigned>> n:<t=int32:<s=int32:#n:asm/cmp <t,<s,LSR $#n:' )

# Cesare says:
print("r = t unsigned>> n:>r=int32:<t=int32:#n:asm/lsr >r, <t, $#n")
print("r = t signed>> n:>r=int32:<t=int32:#n:asm/asr >r, <t, $#n")
print("r = t unsigned>> n:>r=int64:<t=int64:#n:asm/lsr >r, <t, $#n")
print("r = t signed>> n:>r=int64:<t=int64:#n:asm/asr >r, <t, $#n")
print("r = t (unsigned)>> n:>r=int32:<t=int32:#n:asm/lsr >r, <t, $#n")
print("r = t (signed)>> n:>r=int32:<t=int32:#n:asm/asr >r, <t, $#n")
print("r = t (unsigned)>> n:>r=int64:<t=int64:#n:asm/lsr >r, <t, $#n")
print("r = t (signed)>> n:>r=int64:<t=int64:#n:asm/asr >r, <t, $#n")
#print("r = t << n:>r=int32:<t=int32:#n:asm/lsl  <t,$#n")
print("r = t << n:>r=int64:<t=int64:#n:asm/lsl >r, <t, $#n")
# --



#
# 128-bit mem <-> reg
#

print( 'r = mem128[s]:>r=reg128:<s=int64:asm/ldr >r%qregname,[<s]:' )
print( 'r = mem128[s],s+=n:>r=reg128:<s=int64:>s=int64:#n:asm/ldr >r%qregname,[<s],$#n:' )
print( 'r = mem128[s+n]:>r=reg128:<s=int64:#n:asm/ldr >r%qregname,[<s,$#n]:' )
print( 'r = mem128[s+=n]:>r=reg128:<s=int64:>s=int64:#n:asm/ldr >r%qregname,[<s, $#n]!:' )
print( 'r = mem128[s-=n]:>r=reg128:<s=int64:>s=int64:#n:asm/ldr >r%qregname,[<s, $-#n]!:' )

#print( 'r = mem128[s]:>r=reg128:<s=int64:asm/ld1.16b {>r},[<s]:' )


# print( 'r = mem128[s]:>r=reg128:<s=int32:asm/vld1.8 {>r%bot->r%top},[<s]:' )
# print( 'r = mem128[s];s+=16:>r=reg128:<s=int32:asm/vld1.8 {>r%bot->r%top},[<s]!:' )
# print( 'r = mem128[s];s+=t:>r=reg128:<s=int32:<t=int32:asm/vld1.8 {>r%bot->r%top},[<s],<t:' )
# print( 'mem128[s] aligned= r:<r=reg128:<s=int32:asm/vst1.8 {<r%bot-<r%top},[<s,!colon 128]' )
# print( 'mem128[s] aligned= r;s+=16:<r=reg128:<s=int32:asm/vst1.8 {<r%bot-<r%top},[<s,!colon 128]!' )
# print( 'r aligned= mem128[s]:>r=reg128:<s=int32:asm/vld1.8 {>r%bot->r%top},[<s,!colon 128]' )
# print( 'r aligned= mem128[s];s+=16:>r=reg128:<s=int32:asm/vld1.8 {>r%bot->r%top},[<s,!colon 128]!:' )


print( 'mem128[s] = r:<s=int64:<r=reg128:asm/str <r%qregname, [<s]:' )
print( 'mem128[s] = r , s+=n:<s=int64:>s=int64:<r=reg128:#n:asm/str <r%qregname, [<s], $#n:' )
print( 'mem128[s+n] = r:<s=int64:#n:<r=reg128:asm/str <r%qregname, [<s, $#n]:' )
print( 'mem128[s+=n] = r:<r=reg128:<s=int64:>s=int64:#n:asm/str <r%qregname, [<s, $#n]!:' )
print( 'mem128[s-=n] = r:<r=reg128:<s=int64:>s=int64:#n:asm/str <r%qregname, [<s, $-#n]!:' )


print( 'mem8[s] = r , s+=n:<s=int64:>s=int64:<r=reg128:#n:asm/str <r%bregname, [<s], $#n:' )
print( 'mem16[s] = r , s+=n:<s=int64:>s=int64:<r=reg128:#n:asm/str <r%hregname, [<s], $#n:' )
print( 'mem32[s] = r , s+=n:<s=int64:>s=int64:<r=reg128:#n:asm/str <r%sregname, [<s], $#n:' )
print( 'mem64[s] = r , s+=n:<s=int64:>s=int64:<r=reg128:#n:asm/str <r%dregname, [<s], $#n:' )


#print( 'mem128[s] = r:<r=reg128:<s=int64:asm/st1.16b {<r},[<s]:' )
#
# This is hard to implement. The r and t registers must be sequential
#
print( 'mem256[s] = r[0/2] t[0/2] r[1/2] t[1/2]:<r=reg128:<t=reg128:<s=int64:asm/st2 {<r.2d,<t.2d},[<s]:' )
print( 'mem256[s] = r[0/2] t[0/2] r[1/2] t[1/2], s+=32:<r=reg128:<t=reg128:<s=int64:asm/st2 {<r.2d,<t.2d},[<s],32:' )


print( 'push2x8b r , s:<r=reg128:<s=reg128:asm/stp <r%dregname,<s%dregname,[sp,$-16]!' )
print( 'pop2x8b  r , s:>r=reg128:>s=reg128:asm/ldp >r%dregname,>s%dregname,[sp],$16' )

print( 'push2xint64 r , s:<r=int64:<s=int64:asm/stp <r, <s, [sp, $-16]!' )
print( 'pop2xint64  r , s:>r=int64:>s=int64:asm/ldp >r, >s, [sp], $16' )
print( 'pushint64 r:<r=int64:asm/str <r, [sp, $-8]!' )
print( 'popint64  r:>r=int64:asm/ldr >r, [sp], $8' )



# print( 'mem128[s] = r:<r=reg128:<s=int32:asm/vst1.8 {<r%bot-<r%top},[<s]:' )
# print( 'mem128[s] = r;s+=16:<r=reg128:<s=int32:asm/vst1.8 {<r%bot-<r%top},[<s]!:' )
# print( 'r = mem64[s]r[1]:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%bot},[<s]:' )
# print( 'r = mem64[s]r[1];s+=8:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%bot},[<s]!:' )
# print( 'r = r[0]mem64[s]:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%top},[<s]:' )
# print( 'r = r[0]mem64[s];s+=8:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%top},[<s]!:' )
# print( 'r aligned= mem64[s]r[1]:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%bot},[<s,!colon 64]:' )
# print( 'r aligned= r[0]mem64[s]:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%top},[<s,!colon 64]:' )
# print( 'r aligned= mem64[s]r[1];s+=8:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%bot},[<s,!colon 64]!:' )
# print( 'r aligned= mem64[s]r[1];s+=t:<r=reg128:inplace>r=reg128:<s=int32:<t=int32:asm/vld1.8 {<r%bot},[<s,!colon 64],<t:' )
# print( 'r aligned= r[0]mem64[s];s+=8:<r=reg128:inplace>r=reg128:<s=int32:asm/vld1.8 {<r%top},[<s,!colon 64]!:' )
# print( 'r aligned= r[0]mem64[s];s+=t:<r=reg128:inplace>r=reg128:<s=int32:<t=int32:asm/vld1.8 {<r%top},[<s,!colon 64],<t:' )
# print( 'mem64[s] = r[0]:<r=reg128:<s=int32:asm/vst1.8 <r%bot,[<s]:' )
# print( 'mem64[s] = r[0];s+=8:<r=reg128:<s=int32:asm/vst1.8 <r%bot,[<s]!:' )
# print( 'mem64[s] = r[1]:<r=reg128:<s=int32:asm/vst1.8 <r%top,[<s]:' )
# print( 'mem64[s] = r[1];s+=8:<r=reg128:<s=int32:asm/vst1.8 <r%top,[<s]!:' )
# print( 'mem64[s] aligned= r[0]:<r=reg128:<s=int32:asm/vst1.8 <r%bot,[<s,!colon 64]:' )
# print( 'mem64[s] aligned= r[0];s+=8:<r=reg128:<s=int32:asm/vst1.8 <r%bot,[<s,!colon 64]!:' )
# print( 'mem64[s] aligned= r[1]:<r=reg128:<s=int32:asm/vst1.8 <r%top,[<s,!colon 64]:' )
# print( 'mem64[s] aligned= r[1];s+=8:<r=reg128:<s=int32:asm/vst1.8 <r%top,[<s,!colon 64]!:' )

# print( 'r = s[0]r[1]:<r=reg128:inplace>r=reg128:<s=stack128:asm/vldr <r%bot,<s:' )
# print( 'r = r[0]s[1]:<r=reg128:inplace>r=reg128:<s=stack128:asm/vldr <r%top,!shift8<s:' )
# print( 's = r[0]s[1]:<r=reg128:<s=stack128:inplace>s=stack128:asm/vstr <r%bot,<s:' )
# print( 's = s[0]r[1]:<r=reg128:<s=stack128:inplace>s=stack128:asm/vstr <r%top,!shift8<s:' )
# #print( 'r = s:>r=reg128:<s=stack128:asm/vld1.8 {>r%bot->r%top},<s' )
# print( 'r[0] = s:<r=reg128:inplace>r=reg128:<s=stack64:asm/vldr <r%bot,<s' )
# print( 'r[1] = s:<r=reg128:inplace>r=reg128:<s=stack64:asm/vldr <r%top,<s' )
# #print( 'r = s:>r=stack128:<s=reg128:asm/vst1.8 {<s%bot-<s%top},>r' )
# print( 'r = s[0]:>r=stack64:<s=reg128:asm/vstr <s%bot,>r:' )
# print( 'r = s[1]:>r=stack64:<s=reg128:asm/vstr <s%top,>r:' )

# 64-bit EXTR：
# effectively: view t | s as a 128bit(little-endian) number, shifting right {shift}
#              take the low 64 bits and store into r.
print("r = t , s >> n:>r=int64:<t=int64:<s=int64:#n:asm/extr >r,<t,<s, $#n:")

# 32-bit EXTR：
print("r = t , s >> n:>r=int32:<t=int32:<s=int32:#n:asm/extr >r,<t,<s, $#n:")


# 64-bit UBFX:
print("r = t & ((1 << n) - 1):>r=int64:<t=int64:#n:asm/ubfx >r, <t, $0, $#n:")
print("r = (t >> m) & ((1 << n) - 1):>r=int64:<t=int64:#m:#n:asm/ubfx >r, <t, $#m, $#n:")


print( 'r = ~s:>r=int64:<s=int64:asm/mvn >r, <s:')
print( 'r = ~s:>r=int32:<s=int32:asm/mvn >r, <s:')
