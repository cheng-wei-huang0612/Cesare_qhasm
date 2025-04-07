#!/usr/bin/python3


#
# move
#

print( 'r = t:>r=reg128:<t=reg128:asm/mov >r.16b,<t.16b:' )

# vget_lane_xxx, a particular neon lane to GP
for n,u in [(2,'d')]:
  print( 's = r[n/%d]:>s=int64:<r=reg128:#n:asm/umov >s,<r.%s[#n]' % (n,u) )

for n,u in [(4,'s')]:
  print( 's = r[n/%d]:>s=int32:<r=reg128:#n:asm/umov >s,<r.%s[#n]' % (n,u) )
  print( 's = r[n/%d]:>s=int64:<r=reg128:#n:asm/smov >s,<r.%s[#n]' % (n,u) )
  print( 's unsigned= r[n/%d]:>s=int64:<r=reg128:#n:asm/umov >s%%bot,<r.%s[#n]' % (n,u) )

for n,u in [(16,'b'),(8,'h')]:
  print( 's = r[n/%d]:>s=int32:<r=reg128:#n:asm/smov >s,<r.%s[#n]' % (n,u) )
  print( 's unsigned= r[n/%d]:>s=int32:<r=reg128:#n:asm/umov >s,<r.%s[#n]' % (n,u) )
  print( 's = r[n/%d]:>s=int64:<r=reg128:#n:asm/smov >s,<r.%s[#n]' % (n,u) )
  print( 's unsigned= r[n/%d]:>s=int64:<r=reg128:#n:asm/umov >s%%bot,<r.%s[#n]' % (n,u) )






# vsetq_u64, GP to a particular neon lane
for n,u in [(2,'d')]:
  print( 'r[n/%d] = s:inplace>r=reg128:<r=reg128:#n:<s=int64:asm/ins <r.%s[#n],<s' % (n,u) )
for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  print( 'r[n/%d] = s:inplace>r=reg128:<r=reg128:#n:<s=int32:asm/ins <r.%s[#n],<s' % (n,u) )
  print( 'r[n/%d] = s:inplace>r=reg128:<r=reg128:#n:<s=int64:asm/ins <r.%s[#n],<s%%bot' % (n,u) )


# GP to neon
for n,u in [(2,'d')]:
  print( '%dx r = s:inplace>r=reg128:<r=reg128:<s=int64:asm/dup <r.%d%s,<s'% (n,n,u) )
for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  print( '%dx r = s:inplace>r=reg128:<r=reg128:<s=int32:asm/dup <r.%d%s,<s'% (n,n,u) )
  print( '%dx r = s:inplace>r=reg128:<r=reg128:<s=int64:asm/dup <r.%d%s,<s%%bot'% (n,n,u) )


# Cesare: Immediate value to neon(every lane)

print( ' 2x r = n:>r=reg128:#n:asm/movi >r.2d, $#n:')






# neon lane to neon
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  regmod = '%d%s' % (n,u)
  print( '%dx r = s[n]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/dup <r.%s,<s.%s[#n]'% (n,regmod,u) )
  print( '%dx r = s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/dup <r.%s,<s.%s[#n]'% (n,n,regmod,u) )

# widening
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r = t[0]:>r=reg128:<t=reg128:asm/sshll >r.%d%s,<t.%d%s,0'% (n,n,u,n,us) )
  print( '%dx r = t[1]:>r=reg128:<t=reg128:asm/sshll2 >r.%d%s,<t.%d%s,0'% (n,n,u,ns,us) )
  print( '%dx r unsigned= t[0]:>r=reg128:<t=reg128:asm/ushll >r.%d%s,<t.%d%s,0'% (n,n,u,n,us) )
  print( '%dx r unsigned= t[1]:>r=reg128:<t=reg128:asm/ushll2 >r.%d%s,<t.%d%s,0'% (n,n,u,ns,us) )




#
# Comparison
#
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = f'{n}{u}'
  print( f'{n}x r = t == s:>r=reg128:<t=reg128:<s=reg128       :asm/cmeq >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t == 0:>r=reg128:<t=reg128                 :asm/cmeq >r.{nu},<t.{nu},$0' )
  
  print( f'{n}x r = t >= s:>r=reg128:<t=reg128:<s=reg128       :asm/cmge >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t >= 0:>r=reg128:<t=reg128                 :asm/cmge >r.{nu},<t.{nu},$0' )
  print( f'{n}x r = t <= s:>r=reg128:<t=reg128:<s=reg128       :asm/cmge >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = 0 <= t:>r=reg128:<t=reg128                 :asm/cmge >r.{nu},<t.{nu},$0' )

  print( f'{n}x r = t > s:>r=reg128:<t=reg128:<s=reg128        :asm/cmgt >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t > 0:>r=reg128:<t=reg128                 :asm/cmgt >r.{nu},<t.{nu},$0' )
  print( f'{n}x r = t < s:>r=reg128:<t=reg128:<s=reg128        :asm/cmgt >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = 0 < t:>r=reg128:<t=reg128                 :asm/cmgt >r.{nu},<t.{nu},$0' )
  
  print( f'{n}x r = t unsigned> s:>r=reg128:<t=reg128:<s=reg128:asm/cmhi >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t unsigned< s:>r=reg128:<t=reg128:<s=reg128:asm/cmhi >r.{nu},<s.{nu},<t.{nu}' )

  print( f'{n}x r = t unsigned>= s:>r=reg128:<t=reg128:<s=reg128:asm/cmhs >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t unsigned<= s:>r=reg128:<t=reg128:<s=reg128:asm/cmhs >r.{nu},<s.{nu},<t.{nu}' )

  print( f'{n}x r = t <= 0:>r=reg128:<t=reg128                 :asm/cmle >r.{nu},<t.{nu},$0' )
  print( f'{n}x r = 0 >= t:>r=reg128:<t=reg128                 :asm/cmle >r.{nu},<t.{nu},$0' )
  print( f'{n}x r = t < 0:>r=reg128:<t=reg128                 :asm/cmlt >r.{nu},<t.{nu},$0' )
  print( f'{n}x r = 0 > t:>r=reg128:<t=reg128                 :asm/cmlt >r.{nu},<t.{nu},$0' )


#
# logic
#

# instruction: not (mvn)
print( 'r = ~s:>r=reg128:<s=reg128:asm/not  >r.16b,<s.16b:' )

# instruction: mvni


# instruction: eor 
print( 'r ^= t:inplace>r=reg128:<r=reg128:<t=reg128:asm/eor <r.16b,<r.16b,<t.16b:' )
print( 'r = s ^ t:>r=reg128:<s=reg128:<t=reg128:asm/eor >r.16b,<s.16b,<t.16b:' )

# instruction: eor3
# You should check if the machine support this eor3 instruction (FEAT-SHA3)
print( 'r = s ^ t ^ u:>r=reg128:<s=reg128:<t=reg128:<u=reg128:asm/eor3 >r.16b,<s.16b,<t.16b,<u.16b:' )

# instruction: and
print( 'r &= t:inplace>r=reg128:<r=reg128:<t=reg128:asm/and <r.16b,<r.16b,<t.16b:' )
print( 'r = s & t:>r=reg128:<s=reg128:<t=reg128:asm/and >r.16b,<s.16b,<t.16b:' )

# instruction: bic
print( 'r &= ~t:inplace>r=reg128:<r=reg128:<t=reg128:asm/bic <r.16b,<r.16b,<t.16b:' )
print( 'r = s & ~t:>r=reg128:<s=reg128:<t=reg128:asm/bic >r.16b,<s.16b,<t.16b:' )

# instruction: orr
print( 'r |= t:inplace>r=reg128:<r=reg128:<t=reg128:asm/orr <r.16b,<r.16b,<t.16b:' )
print( 'r = s | t:>r=reg128:<s=reg128:<t=reg128:asm/orr >r.16b,<s.16b,<t.16b:' )


# instruction: orr(vector, immediate)
# one should concern the format of immediate values

print( '8x r |= n:inplace>r=reg128:<r=reg128:#n:asm/orr <r.8h, $#n:')
print( '8x r |= (n<<8):inplace>r=reg128:<r=reg128:#n:asm/orr <r.8h, $#n, LSL $8:')

print( '4x r |= n:inplace>r=reg128:<r=reg128:#n:asm/orr <r.4s, $#n:')
print( '4x r |= (n<<8):inplace>r=reg128:<r=reg128:#n:asm/orr <r.4s, $#n, LSL $8:')
print( '4x r |= (n<<16):inplace>r=reg128:<r=reg128:#n:asm/orr <r.4s, $#n, LSL $16:')
print( '4x r |= (n<<24):inplace>r=reg128:<r=reg128:#n:asm/orr <r.4s, $#n, LSL $24:')



# instruction: orn
print( 'r |= ~t:inplace>r=reg128:<r=reg128:<t=reg128:asm/orn <r.16b,<r.16b,<t.16b:' )
print( 'r = s | ~t:>r=reg128:<s=reg128:<t=reg128:asm/orn >r.16b,<s.16b,<t.16b:' )


print( 's = (s & t) | (~s & u):inplace>s=reg128:<s=reg128:<t=reg128:<u=reg128:asm/bsl <s.16b,<t.16b,<u.16b:' )
print( 'u = (s & t) | (~s & u):inplace>u=reg128:<s=reg128:<t=reg128:<u=reg128:asm/bit <u.16b,<t.16b,<s.16b:' )
print( 't = (s & t) | (~s & u):inplace>t=reg128:<s=reg128:<t=reg128:<u=reg128:asm/bif <t.16b,<u.16b,<s.16b:' )



# Exclusive OR and Rotate : XAR

# Rotate and Exclusive OR : RAX1


# print( '4x r &= n:inplace>r=reg128:<r=reg128:#n:asm/vand.i32 <r,$#n:' )
# print( '4x r |= n:inplace>r=reg128:<r=reg128:#n:asm/vorr.i32 <r,$#n:' )




#
# arithmetic
#

# Instruction: addv

print( '16x r = reduce+ s:>r=reg128:<s=reg128:asm/addv >r%bregname,<s.16b' )
print( '8x  r = reduce+ s:>r=reg128:<s=reg128:asm/addv >r%hregname,<s.8h' )
print( '4x  r = reduce+ s:>r=reg128:<s=reg128:asm/addv >r%sregname,<s.4s' )
print( '8x  r = reduce+ s[0/2]:>r=reg128:<s=reg128:asm/addv >r%bregname,<s.8b' )
print( '4x  r = reduce+ s[0/2]:>r=reg128:<s=reg128:asm/addv >r%hregname,<s.4h' )


for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r <<= s:>r=reg128:<r=reg128:<s=reg128:asm/sshl >r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t << s:>r=reg128:<t=reg128:<s=reg128:asm/sshl >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r unsigned<<= s:>r=reg128:<r=reg128:<s=reg128:asm/ushl >r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t unsigned<< s:>r=reg128:<t=reg128:<s=reg128:asm/ushl >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r <<= n:>r=reg128:<r=reg128:#n:asm/shl >r.{nu},<r.{nu},$#n' )
  print( f'{n}x r = t << n:>r=reg128:<t=reg128:#n:asm/shl >r.{nu},<t.{nu},$#n' )
  print( f'{n}x r unsigned<<= n:>r=reg128:<r=reg128:#n:asm/shl >r.{nu},<r.{nu},$#n' )
  print( f'{n}x r = t unsigned<< n:>r=reg128:<t=reg128:#n:asm/shl >r.{nu},<t.{nu},$#n' )
  print( f'{n}x r >>= n:>r=reg128:<r=reg128:#n:asm/sshr >r.{nu},<r.{nu},$#n' )
  print( f'{n}x r = t >> n:>r=reg128:<t=reg128:#n:asm/sshr >r.{nu},<t.{nu},$#n' )
  print( f'{n}x r unsigned>>= n:>r=reg128:<r=reg128:#n:asm/ushr >r.{nu},<r.{nu},$#n' )
  print( f'{n}x r = t unsigned>> n:>r=reg128:<t=reg128:#n:asm/ushr >r.{nu},<t.{nu},$#n' )

# shift right and accumulate
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r += t >> n:inplace>r=reg128:<r=reg128:<t=reg128:#n:asm/ssra <r.{nu},<t.{nu},$#n' )
  print( f'{n}x r unsigned+= t >> n:inplace>r=reg128:<r=reg128:<t=reg128:#n:asm/usra <r.{nu},<t.{nu},$#n' )


# shift and insert
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r <-= t >> n:inplace>r=reg128:<r=reg128:<t=reg128:#n:asm/sri <r.{nu},<t.{nu},$#n' )
  print( f'{n}x r <-= t << n:inplace>r=reg128:<r=reg128:<t=reg128:#n:asm/sli <r.{nu},<t.{nu},$#n' )

# widening
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r = t[0] << n:>r=reg128:<t=reg128:#n:asm/sshll >r.%d%s,<t.%d%s,#n'% (n,n,u,n,us) )
  print( '%dx r = t[1] << n:>r=reg128:<t=reg128:#n:asm/sshll2 >r.%d%s,<t.%d%s,#n'% (n,n,u,ns,us) )
  print( '%dx r = t[0] unsigned<< n:>r=reg128:<t=reg128:#n:asm/ushll >r.%d%s,<t.%d%s,#n'% (n,n,u,n,us) )
  print( '%dx r = t[1] unsigned<< n:>r=reg128:<t=reg128:#n:asm/ushll2 >r.%d%s,<t.%d%s,#n'% (n,n,u,ns,us) )

for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r += s:inplace>r=reg128:<r=reg128:<s=reg128:asm/add <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t + s:>r=reg128:<t=reg128:<s=reg128:asm/add >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r -= s:inplace>r=reg128:<r=reg128:<s=reg128:asm/sub <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t - s:>r=reg128:<t=reg128:<s=reg128:asm/sub >r.{nu},<t.{nu},<s.{nu}' )




# instruction: pmul
for n,u in [(16,'b')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r poly*= s:inplace>r=reg128:<r=reg128:<s=reg128:asm/pmul <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t poly* s:>r=reg128:<t=reg128:<s=reg128:asm/pmul >r.{nu},<t.{nu},<s.{nu}' )




for n,u in [(8,'h'),(4,'s')]:
  # mul (by element)
  print( '%dx r *= s[n]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( '%dx r = t * s[n]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( 'r *= s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( 'r = t * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( '%dx r = t * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
  print( '%dx r *= s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
  print( '%dx r = t unsigned* s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
  print( '%dx r unsigned*= s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )

  # mla (by element)
  print( '%dx r += t * s[n]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( 'r += t * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( '%dx r += t * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
  print( '%dx r += t unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )

  # mls (by element)
  print( '%dx r -= t * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mls <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
  print( '%dx r -= t unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mls <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )


for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  nu = '%d%s'%(n,u)

  # mul (vector)
  print( f'{n}x r *= s:inplace>r=reg128:<r=reg128:<s=reg128:asm/mul <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t * s:>r=reg128:<t=reg128:<s=reg128:asm/mul >r.{nu},<t.{nu},<s.{nu}' )

  # mla (vector)
  print( f'{n}x r += s * t:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/mla <r.{nu},<s.{nu},<t.{nu}' )

  # mls (vector)
  print( f'{n}x r -= s * t:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/mls <r.{nu},<s.{nu},<t.{nu}' )

# Widening
for n,us,ud in [(8,'b','h'),(4,'h','s'),(2,'s','d')]:
  print( '%dx r = t[0] + s[0]:>r=reg128:<t=reg128:<s=reg128:asm/saddl >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,us,n,us) )
  print( '%dx r += s[0]:>r=reg128:<r=reg128:<s=reg128:asm/saddw >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t + s[0]:>r=reg128:<t=reg128:<s=reg128:asm/saddw >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t[1] + s[1]:>r=reg128:<t=reg128:<s=reg128:asm/saddl2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n*2,us,n*2,us) )
  print( '%dx r += s[1]:>r=reg128:<r=reg128:<s=reg128:asm/saddw2 >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )
  print( '%dx r = t + s[1]:>r=reg128:<t=reg128:<s=reg128:asm/saddw2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )

  print( '%dx r = t[0] unsigned+ s[0]:>r=reg128:<t=reg128:<s=reg128:asm/uaddl >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,us,n,us) )
  print( '%dx r unsigned+= s[0]:>r=reg128:<r=reg128:<s=reg128:asm/uaddw >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t unsigned+ s[0]:>r=reg128:<t=reg128:<s=reg128:asm/uaddw >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t[1] unsigned+ s[1]:>r=reg128:<t=reg128:<s=reg128:asm/uaddl2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n*2,us,n*2,us) )
  print( '%dx r unsigned+= s[1]:>r=reg128:<r=reg128:<s=reg128:asm/uaddw2 >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )
  print( '%dx r = t unsigned+ s[1]:>r=reg128:<t=reg128:<s=reg128:asm/uaddw2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )

  print( '%dx r = t[0] - s[0]:>r=reg128:<t=reg128:<s=reg128:asm/ssubl >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,us,n,us) )
  print( '%dx r -= s[0]:>r=reg128:<r=reg128:<s=reg128:asm/ssubw >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t - s[0]:>r=reg128:<t=reg128:<s=reg128:asm/ssubw >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t[1] - s[1]:>r=reg128:<t=reg128:<s=reg128:asm/ssubl2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n*2,us,n*2,us) )
  print( '%dx r -= s[1]:>r=reg128:<r=reg128:<s=reg128:asm/ssubw2 >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )
  print( '%dx r = t - s[1]:>r=reg128:<t=reg128:<s=reg128:asm/ssubw2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )

  print( '%dx r = t[0] unsigned- s[0]:>r=reg128:<t=reg128:<s=reg128:asm/usubl >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,us,n,us) )
  print( '%dx r unsigned-= s[0]:>r=reg128:<r=reg128:<s=reg128:asm/usubw >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t unsigned- s[0]:>r=reg128:<t=reg128:<s=reg128:asm/usubw >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n,us) )
  print( '%dx r = t[1] unsigned- s[1]:>r=reg128:<t=reg128:<s=reg128:asm/usubl2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n*2,us,n*2,us) )
  print( '%dx r unsigned-= s[1]:>r=reg128:<r=reg128:<s=reg128:asm/usubw2 >r.%d%s,<r.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )
  print( '%dx r = t unsigned- s[1]:>r=reg128:<t=reg128:<s=reg128:asm/usubw2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,ud,n,ud,n*2,us) )

# instruction: pmull and pmull2
for n,u,ns,us in [(8,'h',16,'b'),(1,'q',2,'d')]:
  print( '%dx r = t[0] poly* s[0]:>r=reg128:<t=reg128:<s=reg128:asm/pmull >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r = t[1] poly* s[1]:>r=reg128:<t=reg128:<s=reg128:asm/pmull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,ns,us,ns,us) )
  if 1 == n :
    print( 'r = t[0] poly* s[0]:>r=reg128:<t=reg128:<s=reg128:asm/pmull >r.%d%s,<t.%d%s,<s.%d%s'% (n,u,n,us,n,us) )
    print( 'r = t[1] poly* s[1]:>r=reg128:<t=reg128:<s=reg128:asm/pmull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,u,ns,us,ns,us) )







#
# mul vector
#
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r = t[0] * s[0]:>r=reg128:<t=reg128:<s=reg128:asm/smull >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r = t[1] * s[1]:>r=reg128:<t=reg128:<s=reg128:asm/smull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,ns,us,ns,us) )
  print( '%dx r = t[0] unsigned* s[0]:>r=reg128:<t=reg128:<s=reg128:asm/umull >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r = t[1] unsigned* s[1]:>r=reg128:<t=reg128:<s=reg128:asm/umull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,ns,us,ns,us) )


for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r += s[0] * t[0]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlal <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r += s[1] * t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlal2 <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,ns,us,ns,us) )
  print( '%dx r unsigned+= s[0] unsigned* t[0]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/umlal <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r unsigned+= s[1] unsigned* t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/umlal2 <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,ns,us,ns,us) )

  print( '%dx r -= s[0] * t[0]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlsl <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r -= s[1] * t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlsl2 <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,ns,us,ns,us) )
  print( '%dx r unsigned-= s[0] unsigned* t[0]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/umlsl <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r unsigned-= s[1] unsigned* t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/umlsl2 <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,ns,us,ns,us) )




# widening
for n,u,ns,us in [(4,'s',8,'h'),(2,'d',4,'s')]:
   print( '%dx r = t[0] * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/smull >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r = t[0] unsigned* s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/umull >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r = t[1] * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/smull2 >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )
   print( '%dx r = t[1] unsigned* s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/umull2 >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )
   print( '%dx r += t[0] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlal <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r += t[0] unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/umlal <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r += t[1] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlal2 <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )
   print( '%dx r += t[1] unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/umlal2 <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )
   print( '%dx r -= t[0] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlsl <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r -= t[0] unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/umlsl <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r -= t[1] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlsl2 <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )
   print( '%dx r -= t[1] unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/umlsl2 <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )




#( echo vmull =
#) | while read insn accum
#do
#  echo "r[0,1] $accum s[0] unsigned* t[0];r[2,3] $accum s[1] unsigned* t[1]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 >r,<s%bot,<t%bot:"
#  echo "r[0,1] $accum s[0] unsigned* t[2];r[2,3] $accum s[1] unsigned* t[3]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 >r,<s%bot,<t%top:"
#  echo "r[0,1] $accum s[2] unsigned* t[0];r[2,3] $accum s[3] unsigned* t[1]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 >r,<s%top,<t%bot:"
#  echo "r[0,1] $accum s[2] unsigned* t[2];r[2,3] $accum s[3] unsigned* t[3]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 >r,<s%top,<t%top:"
#  echo "r[0,1] $accum s[0] signed* t[0];r[2,3] $accum s[1] signed* t[1]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 >r,<s%bot,<t%bot:"
#  echo "r[0,1] $accum s[0] signed* t[2];r[2,3] $accum s[1] signed* t[3]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 >r,<s%bot,<t%top:"
#  echo "r[0,1] $accum s[2] signed* t[0];r[2,3] $accum s[3] signed* t[1]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 >r,<s%top,<t%bot:"
#  echo "r[0,1] $accum s[2] signed* t[2];r[2,3] $accum s[3] signed* t[3]:>r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 >r,<s%top,<t%top:"
#done

#( echo vmlal +=
#) | while read insn accum
#do
#  echo "r[0,1] $accum s[0] unsigned* t[0];r[2,3] $accum s[1] unsigned* t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 <r,<s%bot,<t%bot:"
#  echo "r[0,1] $accum s[0] unsigned* t[2];r[2,3] $accum s[1] unsigned* t[3]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 <r,<s%bot,<t%top:"
#  echo "r[0,1] $accum s[2] unsigned* t[0];r[2,3] $accum s[3] unsigned* t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 <r,<s%top,<t%bot:"
#  echo "r[0,1] $accum s[2] unsigned* t[2];r[2,3] $accum s[3] unsigned* t[3]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.u32 <r,<s%top,<t%top:"
#  echo "r[0,1] $accum s[0] signed* t[0];r[2,3] $accum s[1] signed* t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 <r,<s%bot,<t%bot:"
#  echo "r[0,1] $accum s[0] signed* t[2];r[2,3] $accum s[1] signed* t[3]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 <r,<s%bot,<t%top:"
#  echo "r[0,1] $accum s[2] signed* t[0];r[2,3] $accum s[3] signed* t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 <r,<s%top,<t%bot:"
#  echo "r[0,1] $accum s[2] signed* t[2];r[2,3] $accum s[3] signed* t[3]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/$insn.s32 <r,<s%top,<t%top:"
#done

# print( "4x r = s * t:>r=reg128:<s=reg128:<t=reg128:asm/vmul.i32 >r,<s,<t:" )
# print( "r[0] = s[0] * t[0];r[1] = s[1] * t[1];r[2,3] = r[2,3]:>r=reg128:<s=reg128:<t=reg128:asm/vmul.i32 >r%bot,<s%bot,<t%bot:" )
# print( 'r[0,1] = r[0,1];r[2] = s[2] * t[2];r[3] = s[3] * t[3]:>r=reg128:<s=reg128:<t=reg128:asm/vmul.i32 >r%top,<s%top,<t%top:"' )


#
# TBL , TBX
#
print( '16x r = t[s]:>r=reg128:<t=reg128:<s=reg128:asm/tbx >r.16b,{<t.16b},<s.16b' )


#
# transpose
#

for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  nu = '%d%s'%(n,u)
  print( '{n}x r = s[0/{n}] t[0/{n}] s[2/{n}] t[2/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/trn1 >r.{nu},<s.{nu},<t.{nu}' )
  print( '{n}x r = s[1/{n}] t[1/{n}] s[3/{n}] t[3/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/trn2 >r.{nu},<s.{nu},<t.{nu}' )

for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r = s[0/{n}] t[0/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/trn1 >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = s[1/{n}] t[1/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/trn2 >r.{nu},<s.{nu},<t.{nu}' )


#
# zip
#

for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r = s[0/{n}] t[0/{n}] s[1/{n}] t[1/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/zip1 >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = s[{n//2}/{n}] t[{n//2}/{n}] s[{1+n//2}/{n}] t[{1+n//2}/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/zip2 >r.{nu},<s.{nu},<t.{nu}' )

for n,u in [(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r zip= s[0/{n}] t[0/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/zip1 >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r zip= s[1/{n}] t[1/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/zip2 >r.{nu},<s.{nu},<t.{nu}' )


#
# un-zip
#

for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r = s[0/{n}] s[2/{n}] t[0/{n}] t[2/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/uzp1 >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = s[1/{n}] s[3/{n}] t[1/{n}] t[3/{n}]:>r=reg128:<s=reg128:<t=reg128:asm/uzp2 >r.{nu},<s.{nu},<t.{nu}' )


# instruction: cnt
print( '16x r = popcnt s:>r=reg128:<s=reg128:asm/cnt >r.16b,<s.16b' )
print( '16x r = ones(s):>r=reg128:<s=reg128:asm/cnt >r.16b,<s.16b' )
print( '8x r = popcnt s[0/2]:>r=reg128:<s=reg128:asm/cnt >r.8b,<s.8b' )
print( '8x r = ones(s[0/2]):>r=reg128:<s=reg128:asm/cnt >r.8b,<s.8b' )






# print( 'r = r[0,1]s[0,1]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vext.32 <r%top,<s%bot,<s%bot,$0:' )
# print( 'r = r[0,1]s[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vext.32 <r%top,<s%top,<s%top,$0:' )
# print( 'r = s[0,1]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vext.32 <r%bot,<s%bot,<s%bot,$0:' )
# print( 'r = s[2,3]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vext.32 <r%bot,<s%top,<s%bot,$0:' )
# print( 'r = r[0,1]s[1]t[0]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%top,<s%bot,<t%bot,$1:' )
# print( 'r = r[0,1]s[1]t[2]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%top,<s%bot,<t%top,$1:' )
# print( 'r = r[0,1]s[3]t[0]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%top,<s%top,<t%bot,$1:' )
# print( 'r = r[0,1]s[3]t[2]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%top,<s%top,<t%top,$1:' )
# print( 'r = s[1]t[0]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%bot,<s%bot,<t%bot,$1:' )
# print( 'r = s[3]t[0]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%bot,<s%top,<t%bot,$1:' )
# print( 'r = s[1]t[2]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%bot,<s%bot,<t%top,$1:' )
# print( 'r = s[1,2,3]t[0]:>r=reg128:<s=reg128:<t=reg128:asm/vext.32 >r,<s,<t,$1:' )
# print( 'r = r[1]r[0]:<r=reg128:inplace>r=reg128:asm/vswp <r%bot,<r%top:' )
# print( 'r = r[1,0]:<r=reg128:inplace>r=reg128:asm/vswp <r%bot,<r%top:' )
# print( 'r = r[2,3]r[0,1]:<r=reg128:inplace>r=reg128:asm/vswp <r%bot,<r%top:' )
# print( 'r s = r[0]s[0]r[1]s[1]:<r=reg128:inplace>r=reg128:<s=reg128:inplace>s=reg128:asm/vswp <s%bot,<r%top:' )
# print( 'r s = r[0]s[1]s[0]r[1]:<r=reg128:inplace>r=reg128:<s=reg128:inplace>s=reg128:asm/vswp <s%top,<r%top:' )
# print( 'r s = s[0]r[1]r[0]s[1]:<r=reg128:inplace>r=reg128:<s=reg128:inplace>s=reg128:asm/vswp <s%bot,<r%bot:' )
# print( 'r s = r[0]s[0]r[2]r[3]r[1]s[1]s[2]s[3]:<r=reg128:inplace>r=reg128:<s=reg128:inplace>s=reg128:asm/vtrn.32 <r%bot,<s%bot:' )
# print( 'r s = r[0]r[1]r[2]s[2]s[0]s[1]r[3]s[3]:<r=reg128:inplace>r=reg128:<s=reg128:inplace>s=reg128:asm/vtrn.32 <r%top,<s%top:' )
# print( 'r s = r[0]s[0]r[2]s[2]r[1]s[1]r[3]s[3]:<r=reg128:inplace>r=reg128:<s=reg128:inplace>s=reg128:asm/vtrn.32 <r,<s:' )
# print( 'r = r[0]r[2]r[1]r[3]:<r=reg128:inplace>r=reg128:asm/vtrn.32 <r%bot,<r%top:' )
# print( 'r = r[0,2,1,3]:<r=reg128:inplace>r=reg128:asm/vtrn.32 <r%bot,<r%top:' )
# print( 'r = r[0,4,2,6,1,5,3,7]:<r=reg128:inplace>r=reg128:asm/vtrn.16 <r%bot,<r%top:' )
# print( 'r = r[0,8,2,10,4,12,6,14,1,9,3,11,5,13,7,15]:<r=reg128:inplace>r=reg128:asm/vtrn.8 <r%bot,<r%top:' )
# print( 'r = s[2,3]t[0,1]:>r=reg128:<s=reg128:<t=reg128:asm/vext.32 >r,<s,<t,$2:' )
# print( 'r = s[3]t[0,1,2]:>r=reg128:<s=reg128:<t=reg128:asm/vext.32 >r,<s,<t,$3:' )
# print( 'r = s[3]t[0]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%bot,<s%top,<t%bot,$1:' )
# print( 'r = s[3]t[2]r[2,3]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vext.32 <r%bot,<s%top,<t%top,$1:' )
# print( 'r = r[0]s[0]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vmov <r%top,<s%bot:' )
# print( 'r = r[0]s[1]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vmov <r%top,<s%top:' )
# print( 'r = s[0]r[1]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vmov <r%bot,<s%bot:' )
# print( 'r = s[1]r[1]:<r=reg128:inplace>r=reg128:<s=reg128:asm/vmov <r%bot,<s%top:' )

# print( 'r = r[1]r[0]r[2,3]:<r=reg128:inplace>r=reg128:asm/vrev64.i32 <r%bot,<r%bot:' )
# print( 'r = r[0,1]r[3]r[2]:<r=reg128:inplace>r=reg128:asm/vrev64.i32 <r%top,<r%top:' )
# print( 's = r[1]r[0]r[3]r[2]:<r=reg128:>s=reg128:asm/vrev64.i32 >s,<r:' )
# print( 's = r[1]r[0]r[3]r[2]r[5]r[4]r[7]r[6]:<r=reg128:>s=reg128:asm/vrev32.i16 >s,<r:' )
# print( 's = r[1]r[0]r[3]r[2]r[5]r[4]r[7]r[6]r[9]r[8]r[11]r[10]r[13]r[12]r[15]r[14]:<r=reg128:>s=reg128:asm/vrev16.i8 >s,<r:' )
# print( 's = r[7,6,5,4,3,2,1,0,15,14,13,12,11,10,9,8]:<r=reg128:>s=reg128:asm/vrev64.i8 >s,<r:' )
# print( 's = r[3,2,1,0,7,6,5,4,11,10,9,8,15,14,13,12]:<r=reg128:>s=reg128:asm/vrev32.i8 >s,<r:' )

# print( 'r[0,1,2,3] s[0,1,2,3] = r[0,2]s[1,3] r[1,3]s[0,2]:inplace>r=reg128:inplace>s=reg128:<r=reg128:<s=reg128:asm/vuzp.i32 <r,<s:' )
# print( 'r[0,1,2,3] s[0,1,2,3] = r[0]s[0]r[1]s[1] r[2]s[2]r[3]s[3]:inplace>r=reg128:inplace>s=reg128:<r=reg128:<s=reg128:asm/vzip.i32 <r,<s:' )
# print( 'r[0,1,2,3]            = r[0]r[2]r[1]r[3]:inplace>r=reg128:<r=reg128:<s=reg128:asm/vzip.i32 <r%bot,<r%top:' )

# print( 'r = s[t[0,1,2,3,4,5,6,7]]r[8,9,10,11,12,13,14,15]:>r=reg128:<s=reg128:<t=reg128:asm/vtbl.8 >r%bot,{<s%bot},<t%bot:' )
# print( 'r = r[0,1,2,3,4,5,6,7] s[8+t[8,9,10,11,12,13,14,15]]:>r=reg128:<s=reg128:<t=reg128:asm/vtbl.8 >r%top,{<s%top},<t%top:' )

# Again: discuss syntax
# print( 'push r s t u:<r=reg128#5:<s=reg128#6:<t=reg128#7:<u=reg128#8:asm/vpush {<r,<s,<t,<u}:' )
# print( 'pop r s t u:>r=reg128#5:>s=reg128#6:>t=reg128#7:>u=reg128#8:asm/vpop {>r,>s,>t,>u}:' )

# Is it worth extending this section or should we just support 64-bit variables?
#print( 'r = r[0],s[1] + t[1]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vadd.i64 <r%top,<s%top,<t%top:' )
#print( 'r = r[0],s[1] + t[0]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vadd.i64 <r%top,<s%top,<t%bot:' )
#print( 'r = s[0] + t[0],r[1]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vadd.i64 <r%bot,<s%bot,<t%bot:' )
#print( 'r = r[0],s[1] signed>> n:<r=reg128:inplace>r=reg128:<s=reg128:#n:asm/vshr.s64 <r%top,<s%top,$#n:' )
#print( 'r = s[0] signed>> n,r[1]:<r=reg128:inplace>r=reg128:<s=reg128:#n:asm/vshr.s64 <r%bot,<s%bot,$#n:' )
#print( 'r = r[0],s[1] << n:<r=reg128:inplace>r=reg128:<s=reg128:#n:asm/vshl.i64 <r%top,<s%top,$#n:' )
#print( 'r = s[0] << n,r[1]:<r=reg128:inplace>r=reg128:<s=reg128:#n:asm/vshl.i64 <r%bot,<s%bot,$#n:' )
#print( 'r = s[0] + t[1],r[1]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vadd.i64 <r%bot,<s%bot,<t%top:' )
#print( 'r = r[0],s[1] - t[1]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vsub.i64 <r%top,<s%top,<t%top:' )
#print( 'r = s[0] - t[0],r[1]:<r=reg128:inplace>r=reg128:<s=reg128:<t=reg128:asm/vsub.i64 <r%bot,<s%bot,<t%bot:' )

#s = s[0],t[1] << 4

# Required for NEON poly1305, discuss and fix syntax!
#print( '2x r[0] <<= n:<r=reg128:>r=reg128:#n:asm/vshl.i32 >r%bot,<r%bot,$#n:' )
#print( '2x r[1] <<= n:<r=reg128:>r=reg128:#n:asm/vshl.i32 >r%top,<r%top,$#n:' )
#print( '2x r[0] unsigned>>= n:<r=reg128:>r=reg128:#n:asm/vshr.u32 >r%bot,<r%bot,$#n:' )
#print( '2x r[1] unsigned>>= n:<r=reg128:>r=reg128:#n:asm/vshr.u32 >r%top,<r%top,$#n:' )
#print( '2x s[0] = r[0] << n:<r=reg128:>s=reg128:#n:asm/vshl.i32 >s%bot,<r%bot,$#n:' )
#print( '2x s[1] = r[1] << n:<r=reg128:>s=reg128:#n:asm/vshl.i32 >s%top,<r%top,$#n:' )
#print( '2x s[0] = r[0] unsigned>> n:<r=reg128:>s=reg128:#n:asm/vshr.u32 >s%bot,<r%bot,$#n:' )
#print( '2x s[1] = r[1] unsigned>> n:<r=reg128:>s=reg128:#n:asm/vshr.u32 >s%top,<r%top,$#n:' )
#print( '2x s[1] = r[0] unsigned>> n:<r=reg128:>s=reg128:#n:asm/vshr.u32 >s%top,<r%bot,$#n:' )
#print( '2x s[0] = r[1] unsigned>> n:<r=reg128:>s=reg128:#n:asm/vshr.u32 >s%bot,<r%top,$#n:' )
#print( 'r[0] ^= t[0]:>r=reg128:<r=reg128:<t=reg128:asm/veor >r%bot,<r%bot,<t%bot:' )
#print( 'r[1] ^= t[0]:>r=reg128:<r=reg128:<t=reg128:asm/veor >r%top,<r%top,<t%bot:' )
#print( 'r[0] ^= t[1]:>r=reg128:<r=reg128:<t=reg128:asm/veor >r%bot,<r%bot,<t%top:' )
#print( 'r[1] ^= t[1]:>r=reg128:<r=reg128:<t=reg128:asm/veor >r%top,<r%top,<t%top:' )

#print( 's[0,1] = r[0]<<n; s[2,3] = r[1]<<n:>s=reg128:<r=reg128:#n:asm/vshll.u32 >s,<r%bot,$#n:' )
#print( 's[0,1] = r[2]<<n; s[2,3] = r[3]<<n:>s=reg128:<r=reg128:#n:asm/vshll.u32 >s,<r%top,$#n:' )

#print( 's[0] = r[0,1] unsigned>> n; s[1] = r[2,3] unsigned>> n:inplace>s=reg128:<s=reg128:<r=reg128:#n:asm/vshrn.u64 <s%bot,<r,$#n:' )
#print( 's[2] = r[0,1] unsigned>> n; s[3] = r[2,3] unsigned>> n:inplace>s=reg128:<s=reg128:<r=reg128:#n:asm/vshrn.u64 <s%top,<r,$#n:' )



# From here on, we list the commands in alphabetic order

# instruction: abs
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r = |s|:>r=reg128:<s=reg128:asm/abs >r.{nu}, <s.{nu}:')


# instruction: addhn

for n,u,dn,s,hu in [(8,'h',16,8,'b'),(4,'s',8,16,'h'),(2,'d',4,32,'s')]:
  nu = '%d%s'%(n,u)
  nhu = '%d%s'%(n,hu)
  dnhu = '%d%s'%(dn,hu)
  print( f'{n}x r[0] = (s + t) >> {s}:>r=reg128:<s=reg128:<t=reg128:asm/addhn >r.{nhu}, <s.{nu}, <t.{nu}:')
  print( f'{n}x r[1] = (s + t) >> {s}:>r=reg128:<s=reg128:<t=reg128:asm/addhn2 >r.{dnhu}, <s.{nu}, <t.{nu}:')

# instruction: addp(scalar)

print( 'r = s[0] + s[1]:>r=reg128:<s=reg128:asm/addp >r%dregname, <s.2d:')

# instruction: addp(vector)

print( '8x 8bits r = s[2i]+s[2i+1] t[2i]+t[2i+1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.8b, <s.8b, <t.8b:')
print( '16x 8bits r = s[2i]+s[2i+1] t[2i]+t[2i+1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.16b, <s.16b, <t.16b:')

print( '4x 16bits r = s[2i]+s[2i+1] t[2i]+t[2i+1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.4h, <s.4h, <t.4h:')
print( '8x 16bits r = s[2i]+s[2i+1] t[2i]+t[2i+1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.8h, <s.8h, <t.8h:')

print( '2x 32bits r = s[2i]+s[2i+1] t[2i]+t[2i+1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.2s, <s.2s, <t.2s:')
print( '4x 32bits r = s[2i]+s[2i+1] t[2i]+t[2i+1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.4s, <s.4s, <t.4s:')

print( '2x r = s[0]+s[1] t[0]+t[1]:>r=reg128:<s=reg128:<t=reg128:asm/addp >r.2d, <s.2d, <t.2d:')

# instruction: addv

print( '16x r = sum(s):>r=reg128:<s=reg128:asm/addv >r%bregname,<s.16b' )
print( '8x  r = sum(s):>r=reg128:<s=reg128:asm/addv >r%hregname,<s.8h' )
print( '4x  r = sum(s):>r=reg128:<s=reg128:asm/addv >r%sregname,<s.4s' )
print( '8x  r = sum(s[0/2]):>r=reg128:<s=reg128:asm/addv >r%bregname,<s.8b' )
print( '4x  r = sum(s[0/2]):>r=reg128:<s=reg128:asm/addv >r%hregname,<s.4h' )

# AES related: 
# instruction: aesd
print( 'r = aesd(s):>r=reg128:<s=reg128:asm/aesd >r.16b, <s.16b:')
# instruction: aese
print( 'r = aese(s):>r=reg128:<s=reg128:asm/aese >r.16b, <s.16b:')
# instruction: aesimc
print( 'r = aesimc(s):>r=reg128:<s=reg128:asm/aesimc >r.16b, <s.16b:')
# instruction: aesmc
print( 'r = aesmc(s):>r=reg128:<s=reg128:asm/aesmc >r.16b, <s.16b:')



# instruction: bcax
#  Bit Clear and Exclusive OR : BCAX

print( 'r = t ^ (s & ~u):>r=reg128:<t=reg128:<s=reg128:<u=reg128:asm/bcax >r.16b, <t.16b, <s.16b, <u.16b:')


# instruction: bic(vector, immediate)
# one should concern the format of immediate values

print( '8x r &= ~n:inplace>r=reg128:<r=reg128:#n:asm/bic <r.8h, $#n:')
print( '8x r &= ~(n<<8):inplace>r=reg128:<r=reg128:#n:asm/bic <r.8h, $#n, LSL $8:')

print( '4x r &= ~n:inplace>r=reg128:<r=reg128:#n:asm/bic <r.4s, $#n:')
print( '4x r &= ~(n<<8):inplace>r=reg128:<r=reg128:#n:asm/bic <r.4s, $#n, LSL $8:')
print( '4x r &= ~(n<<16):inplace>r=reg128:<r=reg128:#n:asm/bic <r.4s, $#n, LSL $16:')
print( '4x r &= ~(n<<24):inplace>r=reg128:<r=reg128:#n:asm/bic <r.4s, $#n, LSL $24:')


# instruction: cls count leading sign bits
print( '16x r = cls(s):>r=reg128:<s=reg128:asm/cls >r.16b, <s.16b:')
print( '8x r = cls(s[0/2]):>r=reg128:<s=reg128:asm/cls >r.8b, <s.8b:')
print( '8x r = cls(s):>r=reg128:<s=reg128:asm/cls >r.8h, <s.8h:')
print( '4x r = cls(s[0/2]):>r=reg128:<s=reg128:asm/cls >r.4h, <s.4h:')
print( '4x r = cls(s):>r=reg128:<s=reg128:asm/cls >r.4s, <s.4s:')
print( '4x r = cls(s[0/2]):>r=reg128:<s=reg128:asm/cls >r.2s, <s.2s:')


# instruction: clz count leading zero bits
print( '16x r = clz(s):>r=reg128:<s=reg128:asm/clz >r.16b, <s.16b:')
print( '8x r = clz(s[0/2]):>r=reg128:<s=reg128:asm/clz >r.8b, <s.8b:')
print( '8x r = clz(s):>r=reg128:<s=reg128:asm/clz >r.8h, <s.8h:')
print( '4x r = clz(s[0/2]):>r=reg128:<s=reg128:asm/clz >r.4h, <s.4h:')
print( '4x r = clz(s):>r=reg128:<s=reg128:asm/clz >r.4s, <s.4s:')
print( '4x r = clz(s[0/2]):>r=reg128:<s=reg128:asm/clz >r.2s, <s.2s:')




# instruction: ext
# Effectively, it view t s as a 32 byte string 
#              logical shift left for n bytes 
#              and then store the low 16 byte (128 bits) into r
print( 'r = t , s << n:>r=reg128:<t=reg128:<s=reg128:#n:asm/ext >r.16b, <t.16b, <s.16b, $#n:' )
print( 'r = t s << n:>r=reg128:<t=reg128:<s=reg128:#n:asm/ext >r.16b, <t.16b, <s.16b, $#n:' )



# instruction: neg
print( '16x r = -t:>r=reg128:<t=reg128:asm/neg >r.16b, <t.16b:')
print( '8x r = -t:>r=reg128:<t=reg128:asm/neg >r.8h, <t.8h:')
print( '4x r = -t:>r=reg128:<t=reg128:asm/neg >r.4s, <t.4s:')
print( '2x r = -t:>r=reg128:<t=reg128:asm/neg >r.2d, <t.2d:')


# instruction: pmul
for n,u in [(16,'b')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r poly*= s:inplace>r=reg128:<r=reg128:<s=reg128:asm/pmul <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t poly* s:>r=reg128:<t=reg128:<s=reg128:asm/pmul >r.{nu},<t.{nu},<s.{nu}' )

# instruction: pmull and pmull2
for n,u,ns,us in [(8,'h',16,'b'),(1,'q',2,'d')]:
  print( '%dx r = t[0] poly* s[0]:>r=reg128:<t=reg128:<s=reg128:asm/pmull >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r = t[1] poly* s[1]:>r=reg128:<t=reg128:<s=reg128:asm/pmull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,ns,us,ns,us) )
  if 1 == n :
    print( 'r = t[0] poly* s[0]:>r=reg128:<t=reg128:<s=reg128:asm/pmull >r.%d%s,<t.%d%s,<s.%d%s'% (n,u,n,us,n,us) )
    print( 'r = t[1] poly* s[1]:>r=reg128:<t=reg128:<s=reg128:asm/pmull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,u,ns,us,ns,us) )

# instruction: raddhn and raddhn2
for n,u,dn,s,hu in [(8,'h',16,8,'b'),(4,'s',8,16,'h'),(2,'d',4,32,'s')]:
  nu = '%d%s'%(n,u)
  nhu = '%d%s'%(n,hu)
  dnhu = '%d%s'%(dn,hu)
  print( f'{n}x r[0] = round(s + t) >> {s}:>r=reg128:<s=reg128:<t=reg128:asm/addhn >r.{nhu}, <s.{nu}, <t.{nu}:')
  print( f'{n}x r[1] = round(s + t) >> {s}:>r=reg128:<s=reg128:<t=reg128:asm/addhn2 >r.{dnhu}, <s.{nu}, <t.{nu}:')



# instruction: rbit
print( '16x r = brv(s):>r=reg128:<s=reg128:asm/rbit >r.16b, <s.16b:')


# instruction: rev16
print( '16x r = s[1]s[0] s[3]s[2]:>r=reg128:<s=reg128:asm/rev16 >r.16b, <s.16b:')

# instruction: rev32
print( '16x r = s[3]s[2]s[1]s[0]:>r=reg128:<s=reg128:asm/rev32 >r.16b, <s.16b:')
print( '8x r = s[1]s[0] s[3]s[2]:>r=reg128:<s=reg128:asm/rev32 >r.8h, <s.8h:')

# instruction: rev64
print( '16x r = s[7]s[6]s[5]s[4]s[3]s[2]s[1]s[0]:>r=reg128:<s=reg128:asm/rev64 >r.16b, <s.16b:')
print( '8x r = s[3]s[2]s[1]s[0]:>r=reg128:<s=reg128:asm/rev32 >r.16b, <s.16b:')
print( '4x r = s[1]s[0] s[3]s[2]:>r=reg128:<s=reg128:asm/rev32 >r.8h, <s.8h:')

# instruction: rshrn and rshrn2 (immediate)
for (n,dn,u,du) in [(8,16, 'b', 'h'), (4,8, 'h', 's'), (2,4, 's', 'd')]:
  print( f'{n}x r = round(s >> n):>r=reg128:<s=reg128:#n:asm/rshrn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[0/2] = round(s >> n):>r=reg128:<s=reg128:#n:asm/rshrn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[1/2] = round(s >> n):>r=reg128:<s=reg128:#n:asm/rshrn2 >r.{dn}{u}, <s.{n}{du}, $#n:')

  print( f'{n}x r = round(s / 2^n):>r=reg128:<s=reg128:#n:asm/rshrn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[0/2] = round(s / 2^n):>r=reg128:<s=reg128:#n:asm/rshrn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[1/2] = round(s / 2^n):>r=reg128:<s=reg128:#n:asm/rshrn2 >r.{dn}{u}, <s.{n}{du}, $#n:')

# instruction: rsubhn and rsubhn2 (immediate)
for (n,dn,u,du) in [(8,16, 'b', 'h'), (4,8, 'h', 's'), (2,4, 's', 'd')]:
  print( f'{n}x r = round((s - t) >> n):>r=reg128:<s=reg128:#n:asm/rsubhn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[0/2] = round((s - t) >> n):>r=reg128:<s=reg128:#n:asm/rsubhn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[1/2] = round((s - t) >> n):>r=reg128:<s=reg128:#n:asm/rsubhn2 >r.{dn}{u}, <s.{n}{du}, $#n:')

  print( f'{n}x r = round((s - t) / 2^n):>r=reg128:<s=reg128:#n:asm/rsubhn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[0/2] = round((s - t) / 2^n):>r=reg128:<s=reg128:#n:asm/rsubhn >r.{n}{u}, <s.{n}{du}, $#n:')
  print( f'{n}x r[1/2] = round((s - t) / 2^n):>r=reg128:<s=reg128:#n:asm/rsubhn2 >r.{dn}{u}, <s.{n}{du}, $#n:')

# instruction: saba
print( '16x r = r + |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/saba <r.16b, <s.16b, <t.16b:')
print( '8x r = r + |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/saba <r.8h, <s.8h, <t.8h:')
print( '4x r = r + |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/saba <r.4s, <s.4s, <t.4s:')
print( '16x r += |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/saba <r.16b, <s.16b, <t.16b:')
print( '8x r += |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/saba <r.8h, <s.8h, <t.8h:')
print( '4x r += |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/saba <r.4s, <s.4s, <t.4s:')

# instruction: sabal and sabal2
print( '8x r(double) = r(double) + |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal <r.8h, <s.8b, <t.8b:')
print( '8x r(double) = r(double) + |s[0/2] - t[0/2]|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal <r.8h, <s.8b, <t.8b:')
print( '8x r(double) = r(double) + |s[1/2] - t[1/2]|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal2 <r.8h, <s.16b, <t.16b:')
print( '4x r(double) = r(double) + |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal <r.4s, <s.4h, <t.4h:')
print( '4x r(double) = r(double) + |s[0/2] - t[0/2]|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal <r.4s, <s.4h, <t.4h:')
print( '4x r(double) = r(double) + |s[1/2] - t[1/2]|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal2 <r.4s, <s.8h, <t.8h:')
print( '2x r(double) = r(double) + |s - t|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal <r.2d, <s.2s, <t.2s:')
print( '2x r(double) = r(double) + |s[0/2] - t[0/2]|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal <r.2d, <s.2s, <t.2s:')
print( '2x r(double) = r(double) + |s[1/2] - t[1/2]|:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/sabal2 <r.2d, <s.4s, <t.4s:')

# instruction: sabd
print( '16x r = |s - t|:>r=reg128:<s=reg128:<t=reg128:asm/sabd >r.16b, <s.16b, <t.16b:')
print( '8x r = |s - t|:>r=reg128:<s=reg128:<t=reg128:asm/sabd >r.8h, <s.8h, <t.8h:')
print( '4x r = |s - t|:>r=reg128:<s=reg128:<t=reg128:asm/sabd >r.4s, <s.4s, <t.4s:')

# instruction: sabdl and sabdl2
print( '8x r(double) = |s - t|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl >r.8h, <s.8b, <t.8b:')
print( '8x r(double) = |s[0/2] - t[0/2]|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl >r.8h, <s.8b, <t.8b:')
print( '8x r(double) = |s[1/2] - t[1/2]|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl2 >r.8h, <s.16b, <t.16b:')
print( '4x r(double) = |s - t|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl >r.4s, <s.4h, <t.4h:')
print( '4x r(double) = |s[0/2] - t[0/2]|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl >r.4s, <s.4h, <t.4h:')
print( '4x r(double) = |s[1/2] - t[1/2]|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl2 >r.4s, <s.8h, <t.8h:')
print( '2x r(double) = |s - t|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl >r.2d, <s.2s, <t.2s:')
print( '2x r(double) = |s[0/2] - t[0/2]|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl >r.2d, <s.2s, <t.2s:')
print( '2x r(double) = |s[1/2] - t[1/2]|:>r=reg128:<s=reg128:<t=reg128:asm/sabdl2 >r.2d, <s.4s, <t.4s:')

# instruction: sadalp
print( '8x r(double) = r(double) + s[2i] - s[2i+1]:inplace>r=reg128:<r=reg128:<s=reg128:asm/sadalp <r.8h, <s.16b:')
print( '4x r(double) = r(double) + s[2i] - s[2i+1]:inplace>r=reg128:<r=reg128:<s=reg128:asm/sadalp <r.4s, <s.8h:')
print( '2x r(double) = r(double) + s[2i] - s[2i+1]:inplace>r=reg128:<r=reg128:<s=reg128:asm/sadalp <r.2d, <s.4s:')
print( '8x r(double) += s[2i] - s[2i+1]:inplace>r=reg128:<r=reg128:<s=reg128:asm/sadalp <r.8h, <s.16b:')
print( '4x r(double) += s[2i] - s[2i+1]:inplace>r=reg128:<r=reg128:<s=reg128:asm/sadalp <r.4s, <s.8h:')
print( '2x r(double) += s[2i] - s[2i+1]:inplace>r=reg128:<r=reg128:<s=reg128:asm/sadalp <r.2d, <s.4s:')

# instruction: smlal and smlal2 (by element)
for n,u,ns,us in [(4,'s',8,'h'),(2,'d',4,'s')]:
   print( '%dx r += t[0] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlal <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r += t[1] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlal2 <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )

# instruction: smlal and smlal2 (vector)
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r += s[0] * t[0]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlal <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r += s[1] * t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlal2 <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,ns,us,ns,us) )

# instruction: smlsl and smlsl2 (by element)
for n,u,ns,us in [(4,'s',8,'h'),(2,'d',4,'s')]:
   print( '%dx r -= t[0] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlsl <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r -= t[1] * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/smlsl2 <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )

# instruction: smlsl and smlsl2 (vector)
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r -= s[0] * t[0]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlsl <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r -= s[1] * t[1]:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/smlsl2 <r.%d%s,<s.%d%s,<t.%d%s'% (n,n,u,ns,us,ns,us) )

# instruction: smull and smull2 (by element)
for n,u,ns,us in [(4,'s',8,'h'),(2,'d',4,'s')]:
   print( '%dx r = t[0] * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/smull >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
   print( '%dx r = t[1] * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/smull2 >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )

# instruction: smull and smull2 (vector)
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r = t[0] * s[0]:>r=reg128:<t=reg128:<s=reg128:asm/smull >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r = t[1] * s[1]:>r=reg128:<t=reg128:<s=reg128:asm/smull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,ns,us,ns,us) )


# instruction: sqabs
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  print( f'{n}x r = |s| (saturated):>r=reg128:<s=reg128:asm/sqabs >r.{n}{u}, <s.{n}{u}:')

# instruction: sqadd
for n,u in [(16,'b'),(8,'h'),(4,'s'),(2,'d')]:
  print( f'{n}x r = s + t (saturated):>r=reg128:<s=reg128:asm/sqadd >r.{n}{u}, <s.{n}{u}, <t.{n}{u}:')


# instruction: sqdmlal and sqdmlal2 (by element)
print( '8x t = saturated(t + 2 * r[0/2] * s[n/8]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlal <t.4s,<r.4h,<s.h[#n]:' )
print( '8x t = saturated(t + 2 * r[1/2] * s[n/8]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlal2 <t.4s,<r.8h,<s.h[#n]:' )
print( '4x t = saturated(t + 2 * r[0/2] * s[n/4]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlal <t.2d,<r.2s,<s.s[#n]:' )
print( '4x t = saturated(t + 2 * r[1/2] * s[n/4]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlal2 <t.2d,<r.4s,<s.s[#n]:' )

# instruction: sqdmlal and sqdmlal2 (vector)
print( '8x t = saturated(t + 2 * r[0/2] * s[0/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlal <t.4s,<r.4h,<s.4h:' )
print( '8x t = saturated(t + 2 * r[1/2] * s[1/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlal2 <t.4s,<r.8h,<s.8h:' )
print( '4x t = saturated(t + 2 * r[0/2] * s[0/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlal <t.2d,<r.2s,<s.2s:' )
print( '4x t = saturated(t + 2 * r[1/2] * s[1/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlal2 <t.2d,<r.4s,<s.4s:' )

# instruction: sqdmlsl and sqdmlsl2 (by element)
print( '8x t = saturated(t - 2 * r[0/2] * s[n/8]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlsl <t.4s,<r.4h,<s.h[#n]:' )
print( '8x t = saturated(t - 2 * r[1/2] * s[n/8]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlsl2 <t.4s,<r.8h,<s.h[#n]:' )
print( '4x t = saturated(t - 2 * r[0/2] * s[n/4]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlsl <t.2d,<r.2s,<s.s[#n]:' )
print( '4x t = saturated(t - 2 * r[1/2] * s[n/4]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmlsl2 <t.2d,<r.4s,<s.s[#n]:' )

# instruction: sqdmlsl and sqdmlsl2 (vector)
print( '8x t = saturated(t - 2 * r[0/2] * s[0/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlsl <t.4s,<r.4h,<s.4h:' )
print( '8x t = saturated(t - 2 * r[1/2] * s[1/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlsl2 <t.4s,<r.8h,<s.8h:' )
print( '4x t = saturated(t - 2 * r[0/2] * s[0/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlsl <t.2d,<r.2s,<s.2s:' )
print( '4x t = saturated(t - 2 * r[1/2] * s[1/2]):inplace>t=reg128:<t=reg128:<r=reg128:<s=reg128:asm/sqdmlsl2 <t.2d,<r.4s,<s.4s:' )

# instruction: sqdmulh and sqdmulh2 (by element)
print( '8x t = signedsaturated((2 * r * s[n/8]) >> 16):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmulh >t.8h,<r.8h,<s.h[#n]:' )
print( '8x t = signedsaturated((r * s[n/8]) >> 15):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmulh >t.8h,<r.8h,<s.h[#n]:' )
print( '4x t = signedsaturated((2 * r * s[n/4]) >> 32):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmulh >t.4s,<r.4s,<s.s[#n]:' )
print( '4x t = signedsaturated((r * s[n/4]) >> 31):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmulh >t.4s,<r.4s,<s.s[#n]:' )


# instruction: sqdmulh and sqdmulh2 (vector)
print( '8x t = signedsaturated((2 * r * s) >> 16):>t=reg128:<r=reg128:<s=reg128:asm/sqdmulh >t.8h,<r.8h,<s.8h:' )
print( '8x t = signedsaturated((r * s) >> 15):>t=reg128:<r=reg128:<s=reg128:asm/sqdmulh >t.8h,<r.8h,<s.8h:' )
print( '4x t = signedsaturated((2 * r * s) >> 32):>t=reg128:<r=reg128:<s=reg128:asm/sqdmulh >t.4s,<r.4s,<s.4s:' )
print( '4x t = signedsaturated((r * s) >> 31):>t=reg128:<r=reg128:<s=reg128:asm/sqdmulh >t.4s,<r.4s,<s.4s:' )

# instruction: sqdmull and sqdmull2 (by element)
print( '8x t = saturated(2 * r[0/2] * s[n/8]):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmull <t.4s,<r.4h,<s.h[#n]:' )
print( '8x t = saturated(2 * r[1/2] * s[n/8]):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmull2 <t.4s,<r.8h,<s.h[#n]:' )
print( '4x t = saturated(2 * r[0/2] * s[n/4]):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmull <t.2d,<r.2s,<s.s[#n]:' )
print( '4x t = saturated(2 * r[1/2] * s[n/4]):>t=reg128:<r=reg128:<s=reg128:#n:asm/sqdmull2 <t.2d,<r.4s,<s.s[#n]:' )

# instruction: sqdmull and sqdmull2 (vector)
print( '8x t = saturated(2 * r[0/2] * s[0/2]):>t=reg128:<r=reg128:<s=reg128:asm/sqdmull <t.4s,<r.4h,<s.4h:' )
print( '8x t = saturated(2 * r[1/2] * s[1/2]):>t=reg128:<r=reg128:<s=reg128:asm/sqdmull2 <t.4s,<r.8h,<s.8h:' )
print( '4x t = saturated(2 * r[0/2] * s[0/2]):>t=reg128:<r=reg128:<s=reg128:asm/sqdmull <t.2d,<r.2s,<s.2s:' )
print( '4x t = saturated(2 * r[1/2] * s[1/2]):>t=reg128:<r=reg128:<s=reg128:asm/sqdmull2 <t.2d,<r.4s,<s.4s:' )


# instruction: sqrdmulh (by element)
print( '4x t = (r * s[n/4]) >> 31 round:>t=reg128:<r=reg128:<s=reg128:#n:asm/sqrdmulh >t.4s,<r.4s,<s.s[#n]:' )
print( '8x t = (r * s[n/8]) >> 15 round:>t=reg128:<r=reg128:<s=reg128:#n:asm/sqrdmulh >t.8h,<r.8h,<s.h[#n]:' )

# instruction: sqrdmulh (vector)
print( '4x t = (r * s) >> 31 round:>t=reg128:<r=reg128:<s=reg128:asm/sqrdmulh >t.4s,<r.4s,<s.4s:' )
print( '8x t = (r * s) >> 15 round:>t=reg128:<r=reg128:<s=reg128:asm/sqrdmulh >t.8h,<r.8h,<s.8h:' )
print( '2x t = (r * s) >> 31 round:>t=reg128:<r=reg128:<s=reg128:asm/sqrdmulh >t.2s,<r.2s,<s.2s:' )
print( '4x t = (r * s) >> 15 round:>t=reg128:<r=reg128:<s=reg128:asm/sqrdmulh >t.4h,<r.4h,<s.4h:' )

# instruction: umull and umull2 (by element)
for n,u,ns,us in [(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r = t[0] unsigned* s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/umull >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,n,us,us) )
  print( '%dx r = t[1] unsigned* s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/umull2 >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,ns,n,u,ns,us,us) )

# instruction: umull and umull2 (vector)
for n,u,ns,us in [(8,'h',16,'b'),(4,'s',8,'h'),(2,'d',4,'s')]:
  print( '%dx r = t[0] unsigned* s[0]:>r=reg128:<t=reg128:<s=reg128:asm/umull >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,n,us,n,us) )
  print( '%dx r = t[1] unsigned* s[1]:>r=reg128:<t=reg128:<s=reg128:asm/umull2 >r.%d%s,<t.%d%s,<s.%d%s'% (n,n,u,ns,us,ns,us) )

# umlal (vector)
print( '2x r += t * s:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:asm/umlal <r.2d,<t.2s,<s.2s' )
