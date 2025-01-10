#!/usr/bin/python3


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

#
# The last part of description file and the start of the useer code.
#

print( ':' )

for i in range(0,8):
  print( 'int64 input_x%d'%(i) )

print( 'int64 output_x0' )

for i in range(18,30):
  print( 'int64 calleesaved_x%d'%(i) )

for i in range(0,8):
  print( 'reg128 input_v%d'%(i) )

print( 'reg128 output_v0' )

for i in range(8,16):
  print( 'reg128 calleesaved_v%d'%(i) )

