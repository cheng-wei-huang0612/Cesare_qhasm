#!/usr/bin/python3

###############################################################################
## Scalar Arithmetic
###############################################################################

# FABD <V>d, <V>n, <V>m
# Floating-point absolute difference (scalar). Subtracts <V>m from <V>n, and
# places the absolute value of the result in <V>d. Where <V>is S or D.

# ADD Dd, Dn, Dm
# Add (scalar).
print("1/2 r = t + s:>r=int128:<t=int128:<s=int128`:asm/add >r%bot,<t%bot,<s%bot:")

# SQADD <V>d, <V>n, <V>m
# Signed saturating add (scalar). Where <V> is B, H, S or D.

# UQADD <V>d, <V>n, <V>m
# Unsigned saturating add (scalar). Where <V> is B, H, S or D.

# SQDMULH <V>d, <V>n, <V>m
# Signed saturating doubling multiply high half (scalar). Where <V> is H or S.

# SQRDMULH <V>d, <V>n, <V>m
# Signed saturating rounding doubling multiply high half (scalar). Where <V> is H or S.

# UQRSHL <V>d, <V>n, <V>m
# Unsigned saturating rounding shift left (scalar). Where <V> is B, H, S or D.

# SQRSHL <V>d, <V>n, <V>m
# Signed saturating rounding shift left (scalar). Where <V> is B, H, S or D.

# UQSUB <V>d, <V>n, <V>m
# Unsigned saturating subtract (scalar). Where <V> is B, H, S or D.

# SQSUB <V>d, <V>n, <V>m
# Signed saturating subtract (scalar). Where <V> is B, H, S or D.

# UQSHL <V>d, <V>n, <V>m
# Unsigned saturating shift left (scalar). Where <V> is B, H, S or D.

# SQSHL <V>d, <V>n, <V>m
# Signed saturating shift left (scalar). Where <V> is B, H, S or D.
#
# URSHL Dd, Dn, Dm
# Unsigned rounding shift left (scalar).

# SRSHL Dd, Dn, Dm
# Signed rounding shift left (scalar).

# USHL Dd, Dn, Dm
# Unsigned shift left (scalar).
print("1/2 r = t unsigned<< s:>r=int128:<t=int128:<s=int128:asm/ushl >r%bot,<t%bot,<s%bot:")

# SSHL Dd, Dn, Dm
# Signed shift left (scalar).
print("1/2 r = t signed<< s:>r=int128:<t=int128:<s=int128:asm/sshl >r%bot,<t%bot,<s%bot:")

# SUB Dd, Dn, Dm
# Subtract (scalar).
print("1/2 r = t - s:>r=int128:<t=int128:<s=int128`:asm/sub >r%bot,<t%bot,<s%bot:")

# FMULX <V>d, <V>n, <V>m
# Floating-point multiply extended, like FMUL but 0 ± ∞ → ±2 (scalar).
# Where <V> is S or D.

# FRECPS <V>d, <V>n, <V>m
# Floating-point reciprocal step (scalar). Where <V>is S or D. The embedded
# multiply-accumulate is fused in AArch64 FRECPS, whilst in AArch32 VRECPS it
# remains chained.

# FRSQRTS <V>d, <V>n, <V>m
# Floating-point reciprocal square root step (scalar). Where <V>is S or D. The embedded multiply-
# accumulate is fused in AArch64 FRSQRTS, whilst in AArch32 VRSQRTS it remains chained.


###############################################################################
## Scalar Compare
###############################################################################

# CMEQ Dd, Dn, Dm
# Compare bitwise equal (scalar).
print("1/2 r = (t == s):>r=int128:<t=int128:<s=int128`:asm/cmeq >r%bot,<t%bot,<s%bot:")

# CMEQ Dd, Dn, #0
# Compare bitwise equal to zero (scalar).
print("1/2 r = (t == 0):>r=int128:<t=int128`:asm/cmeq >r%bot,<t%bot,#0:")

# CMHS Dd, Dn, Dm
# Compare unsigned higher or same (scalar).
print("1/2 r = (t unsigend>= s):>r=int128:<t=int128:<s=int128`:asm/cmhs >r%bot,<t%bot,<s%bot:")

# CMGE Dd, Dn, Dm
# Compare signed greater than or equal (scalar).
print("1/2 r = (t sigend>= s):>r=int128:<t=int128:<s=int128`:asm/cmge >r%bot,<t%bot,<s%bot:")

# CMGE Dd, Dn, #0
# Compare signed greater than or equal to zero (scalar).
print("1/2 r = (t >= 0):>r=int128:<t=int128`:asm/cmge >r%bot,<t%bot,#0:")

# CMHI Dd, Dn, Dm
# Compare unsigned higher (scalar).
print("1/2 r = (t unsigend> s):>r=int128:<t=int128:<s=int128`:asm/cmhi >r%bot,<t%bot,<s%bot:")

# CMGT Dd, Dn, Dm
# Compare signed greater than (scalar).
print("1/2 r = (t sigend> s):>r=int128:<t=int128:<s=int128`:asm/cmgt >r%bot,<t%bot,<s%bot:")

# CMGT Dd, Dn, #0
# Compare signed greater than zero (scalar).
print("1/2 r = (t > 0):>r=int128:<t=int128`:asm/cmgt >r%bot,<t%bot,#0:")

# CMLE Dd, Dn, #0
# Compare signed less than or equal to zero (scalar).
print("1/2 r = (t <= 0):>r=int128:<t=int128`:asm/cmle >r%bot,<t%bot,#0:")

# CMLT Dd, Dn, #0
# Compare signed less than zero (scalar).
print("1/2 r = (t < 0):>r=int128:<t=int128`:asm/cmlt >r%bot,<t%bot,#0:")

# CMTST Dd, Dn, Dm
# Compare bitwise test bits (scalar).
print("1/2 r = (t && s) > 0:>r=int128:<t=int128:<s=int128`:asm/cmtst >r%bot,<t%bot,<s%bot:")

# FCMEQ <V>d, <V>n, <V>m
# Floating-point compare mask equal (scalar). Where <V>is S or D.

# FCMEQ <V>d, <V>n, #0
# Floating-point compare mask equal to zero (scalar). Where <V>is S or D.

# FCMGE <V>d, <V>n, <V>m
# Floating-point compare mask greater than or equal (scalar). Where <V>is S or D.

# FCMGE <V>d, <V>n, #0
# Floating-point compare mask greater than or equal to zero (scalar). Where <V>is S or D.

# FCMGT <V>d, <V>n, <V>m
# Floating-point compare mask greater than (scalar). Where <V>is S or D.

# FCMGT <V>d, <V>n, #0
# Floating-point compare mask greater than zero (scalar). Where <V>is S or D.

# FCMLE <V>d, <V>n, #0
# Floating-point compare mask less than or equal to zero (scalar). Where <V>is S or D.

# FCMLT <V>d, <V>n, #0
# Floating-point compare mask less than zero (scalar). Where <V>is S or D.

# FACGE <V>d, <V>n, <V>m
# Floating-point absolute compare mask greater than or equal (scalar). Where <V>is S or D.

# FACGT <V>d, <V>n, <V>m
# Floating-point absolute compare mask greater than (scalar). Where <V>is S or D.


###############################################################################
## Scalar Widening/Narrowing Arithmetic
###############################################################################

# SQDMLAL <Vd>d, <Vs>n, <Vs>m
# Signed saturating doubling multiply-add long (scalar). Where the <Vd>/<Vs> is S/H or D/S.

# SQDMLSL <Vd>d, <Vs>n, <Vs>m
# Signed saturating doubling multiply-subtract long (scalar). Where the <Vd>/<Vs> is S/H or D/S.

# SQDMULL <Vd>d, <Vs>n, <Vs>m
# Signed saturating doubling multiply long (scalar). Where the <Vd>/<Vs> is S/H or D/S.


###############################################################################
## Scalar Unary Arithmetic
###############################################################################

# ABS Dd, Dn
# Absolute value (scalar).
print("1/2 r = abs(t):>r=int128:<t=int128`:asm/abs >r%bot,<t%bot:")

# SQABS <V>d, <V>n
# Signed saturating absolute value (scalar). Where <V> is B, H, S or D.

# NEG Dd, Dn
# Negate (scalar).
print("1/2 r = -t:>r=int128:<t=int128`:asm/neg >r%bot,<t%bot:")

# SQNEG <V>d, <V>n
# Signed saturating negate (scalar). Where <V> is B, H, S or D.

# SUQADD <V>d, <V>n
# Signed saturating accumulate of unsigned value (scalar). Where <V> is B, H, S or D.

# USQADD <V>d, <V>n
# Unsigned saturating accumulate of signed value Where <V> is B, H, S or D.

# SQXTUN <Vd>d, <Vs>n
# Signed saturating extract unsigned narrow (scalar). Where <Vd>/<Vs> is B/H, H/S or S/D.

# UQXTN <Vd>d, <Vs>n
# Unsigned saturating extract narrow (scalar). Where <Vd>/<Vs> is B/H, H/S or S/D.

# SQXTN <Vd>d, <Vs>n
# Signed saturating extract narrow (scalar). Where <Vd>/<Vs> is B/H, H/S or S/D.

# FCVTXN Sd, Dn
# Floating-point convert precision narrow, converting double-precision to
# single-precision with inexact result rounding to odd (scalar). Rounding to
# odd, or Von Neumann's rounding, is only suitable for further narrowing to
# half-precision giving correct rounding of the half-precision result.

# FRECPE <V>d, <V>n
# Floating-point reciprocal estimate (scalar). Where <V> is S or D.

# FRECPX <V>d, <V>n
# Floating-point reciprocal exponent (scalar). Where <V> is S or D.

# FRSQRTE <V>d, <V>n
# Floating-point reciprocal square root estimate (scalar). Where <V> is S or D.


###############################################################################
## Scalar-by-element Arithmetic
###############################################################################

# FMLA <V>d, <V>n, Vm.<Ts>[index]
# Floating-point fused multiply-add (scalar, by element). Where <V>/<Ts> is S/S or D/D.

# FMLS <V>d, <V>n, Vm.<Ts>[index]
# Floating-point fused multiply-subtract (scalar, by element). Where <V>/<Ts> is S/S or D/D.

# FMUL <V>d, <V>n, Vm.<Ts>[index]
# Floating-point multiply (scalar, by element). Where <V>/<Ts> is S/S or D/D.

# FMULX <V>d, <V>n, Vm.<Ts>[index]
# Floating-point multiply extended (scalar, by element): like FMUL but 0 ± ∞ →
# ±2. Where <V>/<Ts> is S/S, or D/D.

# SQDMLAL <Va>d, <Vb>n, Vm.<Ts>[index]
# Signed saturating doubling multiply-add long (scalar, by element). Where
# <Va>/<Vb>/<Ts> is S/H/H or D/S/S. If <Ts> is H, then Vm must be in the range
# V0-V15.

# SQDMLSL <Va>d, <Vb>n, Vm.<Ts>[index]
# Signed saturating doubling multiply-subtract long (scalar, by element). Where
# <Va>/<Vb>/<Ts> is S/H/H or D/S/S. If <Ts> is H, then Vm must be in the range
# V0-V15.

# SQDMULL <Va>d, <Vb>n, Vm.<Ts>[index]
# Signed saturating doubling multiply long (scalar, by element). Where
# <Va>/<Vb>/<Ts> is S/H/H or D/S/S.  If <Ts> is H, then Vm must be in the range
# V0-V15.

# SQDMULH <V>d, <V>n, Vm.<Ts>[index]
# Signed saturating doubling multiply returning high half (scalar, by element).
# Where <V>/<Ts> is H/H or S/S. If <Ts> is H, then Vm must be in the range
# V0-V15.

# SQRDMULH <V>d, <V>n, Vm.<Ts>[index]
# Signed saturating rounding doubling multiply returning high half (scalar, by
# element). Where <V>/<Ts> is H/H or S/S. If <Ts> is H, then Vm must be in the
# range V0-V15.


###############################################################################
## Scalar Shift (immediate)
###############################################################################

# USHR Dd, Dn, #shift
# Unsigned shift right (scalar). Where shift is in the range 1 to 64.
print("1/2 r = t unsigned>> n:>r=int128:<t=int128:#n:asm/ushr >r%bot,<t%bot,$#n:")

# SSHR Dd, Dn, #shift
# Signed shift right (scalar). Where shift is in the range 1 to 64.
print("1/2 r = t signed>> n:>r=int128:<t=int128:#n:asm/sshr >r%bot,<t%bot,$#n:")

# URSHR Dd, Dn, #shift
# Unsigned rounding shift right (scalar). Where shift is in the range 1 to 64.

# SRSHR Dd, Dn, #shift
# Signed rounding shift right (scalar). Where shift is in the range 1 to 64.

# USRA Dd, Dn, #shift
# Unsigned shift right and accumulate (scalar). Where shift is in the range 1 to 64.

# SSRA Dd, Dn, #shift
# Signed shift right and accumulate (scalar). Where shift is in the range 1 to 64.

# URSRA Dd, Dn, #shift
# Unsigned rounding shift right and accumulate (scalar). Where shift is in the range 1 to 64.

# SRSRA Dd, Dn, #shift
# Signed rounding shift right and accumulate (scalar). Where shift is in the range 1 to 64.

# SRI Dd, Dn, #shift
# Shift right and insert (scalar). Where shift is in the range 1 to 64.

# UQSHRN <Vd>d, <Vs>n, #shift
# Unsigned saturating shift right narrow (scalar). Where <Vd>/<Vs> is B/H, H/S,
# or S/D; and shift is in the range 1 to elsize(<Vd>).

# SQSHRN <Vd>d, <Vs>n, #shift
# Signed saturating shift right narrow (scalar). Where <Vd>/<Vs> is B/H, H/S,
# or S/D; and shift is in the range 1 to elsize(<Vd>).

# UQRSHRN <Vd>d, <Vs>n, #shift
# Unsigned saturating rounding shift right narrow (scalar). Where <Vd>/<Vs> is
# B/H, H/S, or S/D; and shift is in the range 1 to elsize(<Vd>).

# SQRSHRN <Vd>d, <Vs>n, #shift
# Signed saturating rounding shift right narrow (scalar). Where <Vd>/<Vs> is
# B/H, H/S, or S/D; and shift is in the range 1 to elsize(<Vd>).

# SQSHRUN <Vd>d, <Vs>n, #shift
# Signed saturating shift right unsigned narrow (scalar). Where <Vd>/<Vs> is
# B/H, H/S, or S/D; and shift is in the range 1 to elsize(<Vd>).

# SQRSHRUN <Vd>d, <Vs>n, #shift
# Signed saturating rounding shift right unsigned narrow (scalar). Where
# <Vd>/<Vs> is B/H, H/S, or S/D; and shift is in the range 1 to elsize(<Vd>).

# SHL Dd, Dn, #shift
# Shift left (scalar). Where shift is in the range 0 to 63.
print("1/2 r = t << n:>r=int128:<t=int128:#n:asm/slr >r%bot,<t%bot,$#n:")

# UQSHL <V>d, <V>n, #shift
# Unsigned saturating shift left (scalar). Where <V> is B, H, S, or D; and
# shift is in the range 0 to elsize(<V>)-1.

# SQSHL <V>d, <V>n, #shift
# Signed saturating shift left (scalar). Where <V> is B, H, S, or D; and shift
# is in the range 0 to elsize(<V>)- 1.

# SQSHLU <V>d, <V>n, #shift
# Signed saturating shift left unsigned (scalar). Where <V> is B, H, S, or D;
# and shift is in the range 0 to elsize(<V>)-1.

# SLI Dd, Dn, #shift
# Shift left and insert (scalar). Where shift is in the range 0 to 63.


###############################################################################
## Scalar Floating Point / Integer Convert
###############################################################################

# FCVT<r>S <V>d, <V>n
# Floating-point convert to signed integer of same size (scalar). Where <V> is
# S or D. The syntax term <r> selects the rounding mode: N (nearest, ties to
# even); A (nearest, ties to away), P (towards +Inf); M (towards –Inf), Z
# (towards zero).

# FCVTZS <V>d, <V>n, #fbits
# Floating-point convert to signed fixed-point of same size (scalar) with
# rounding towards zero. Where <V> is S or D. The number of fractional bits is
# represented by fbits in the range 1 to elsize(<V>).

# FCVT<r>U <V>d, <V>n
# Floating-point convert to unsigned integer of same size (scalar). Where <V>
# is S or D. The syntax term <r> selects the rounding mode: N (nearest, ties to
# even); A (nearest, ties to away), P (towards +Inf); M (towards –Inf), Z
# (towards zero).

# FCVTZU <V>d, <V>n, #fbits
# Floating-point convert to unsigned fixed-point of same size (scalar) with
# rounding towards zero. Where <V> is S or D. The number of fractional bits is
# represented by fbits in the range 1 to elsize(<V>).

# SCVTF <V>d, <V>n
# Signed integer convert to floating-point of same size using FPCR rounding
# mode (scalar). Where <V> is S or D.

# SCVTF <V>d, <V>n, #fbits
# Signed fixed-point convert to floating-point of same size using FPCR rounding
# mode (scalar). Where <V> is S or D. The number of fractional bits is
# represented by fbits in the range 1 to elsize(<V>).

# UCVTF <V>d, <V>n
# Unsigned integer convert to floating-point of same size using FPCR rounding
# mode (scalar). Where <V> is S or D.

# UCVTF <V>d, <V>n, #fbits
# Unsigned fixed-point convert to floating-point of same size using FPCR
# rounding mode (scalar). Where <V> is S or D. The number of fractional bits is
# represented by fbits in the range 1 to elsize(<V>).


###############################################################################
## Scalar Pairwise Reduce
###############################################################################

# ADDP Dd, Vn.2D
# Add pairwise (scalar).
print("1/2 r = t[0] + t[1]:>r=int128:<t=int128`:asm/addp >r%bot,<t:")

# FADDP <V>d, Vn.<T>
# Floating-point add pairwise (scalar). Where <V>/<T> is S/2S or D/2D.

# FMAXP <V>d, Vn.<T>
# Floating-point maximum pairwise (scalar). Where <V>/<T> is S/2S or D/2D.

# FMAXNMP <V>d, Vn.<T>
# Floating-point maximum number pairwise (scalar). Where <V>/<T> is S/2S or D/2D.

# FMINP <V>d, Vn.<T>
# Floating-point minimum pairwise (scalar). Where <V>/<T> is S/2S or D/2D.

# FMINNMP <V>d, Vn.<T>
# Floating-point minimum number pairwise (scalar). Where <V>/<T> is S/2S or D/2D.

