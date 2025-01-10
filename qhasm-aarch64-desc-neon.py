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
  print( f'{n}x r = t == 0:>r=reg128:<t=reg128                 :asm/cmeq >r.{nu},<t.{nu},0' )
  print( f'{n}x r = t >= s:>r=reg128:<t=reg128:<s=reg128       :asm/cmge >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t unsigned>= s:>r=reg128:<t=reg128:<s=reg128:asm/cmhs >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t > s:>r=reg128:<t=reg128:<s=reg128        :asm/cmgt >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t unsigned> s:>r=reg128:<t=reg128:<s=reg128:asm/cmhi >r.{nu},<t.{nu},<s.{nu}' )
  print( f'{n}x r = t <= s:>r=reg128:<t=reg128:<s=reg128       :asm/cmge >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = t unsigned<= s:>r=reg128:<t=reg128:<s=reg128:asm/cmhs >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = t < s:>r=reg128:<t=reg128:<s=reg128        :asm/cmgt >r.{nu},<s.{nu},<t.{nu}' )
  print( f'{n}x r = t unsigned< s:>r=reg128:<t=reg128:<s=reg128:asm/cmhi >r.{nu},<s.{nu},<t.{nu}' )



#
# logic
#
print( 'r = ~s:>r=reg128:<s=reg128:asm/mvn  >r.16b,<s.16b:' )

print( 'r ^= t:>r=reg128:<r=reg128:<t=reg128:asm/eor >r.16b,<r.16b,<t.16b:' )
print( 'r &= t:>r=reg128:<r=reg128:<t=reg128:asm/and >r.16b,<r.16b,<t.16b:' )
print( 'r &= ~t:>r=reg128:<r=reg128:<t=reg128:asm/bic >r.16b,<r.16b,<t.16b:' )
print( 'r |= t:>r=reg128:<r=reg128:<t=reg128:asm/orr >r.16b,<r.16b,<t.16b:' )
print( 'r |= ~t:>r=reg128:<r=reg128:<t=reg128:asm/orn >r.16b,<r.16b,<t.16b:' )

print( 'r = s ^ t:>r=reg128:<s=reg128:<t=reg128:asm/eor >r.16b,<s.16b,<t.16b:' )
print( 'r = s & t:>r=reg128:<s=reg128:<t=reg128:asm/and >r.16b,<s.16b,<t.16b:' )
print( 'r = s & ~t:>r=reg128:<s=reg128:<t=reg128:asm/bic >r.16b,<s.16b,<t.16b:' )
print( 'r = s | t:>r=reg128:<s=reg128:<t=reg128:asm/orr >r.16b,<s.16b,<t.16b:' )
print( 'r = s | ~t:>r=reg128:<s=reg128:<t=reg128:asm/orn >r.16b,<s.16b,<t.16b:' )

print( 's = (s & t) | (~s & u):inplace>s=reg128:<s=reg128:<t=reg128:<u=reg128:asm/bsl <s.16b,<t.16b,<u.16b:' )
# print( 'u = (s & t) | (~s & u):inplace>u=reg128:<s=reg128:<t=reg128:<u=reg128:asm/vbit <u,<t,<s:' )
# print( 't = (s & t) | (~s & u):inplace>t=reg128:<s=reg128:<t=reg128:<u=reg128:asm/vbif <t,<u,<s:' )

# Bit Clear and Exclusive OR : BCAX

# Exclusive OR and Rotate : XAR

# Rotate and Exclusive OR : RAX1


# print( '4x r &= n:inplace>r=reg128:<r=reg128:#n:asm/vand.i32 <r,$#n:' )
# print( '4x r |= n:inplace>r=reg128:<r=reg128:#n:asm/vorr.i32 <r,$#n:' )




#
# arithmetic
#

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



for n,u in [(16,'b')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r poly*= s:inplace>r=reg128:<r=reg128:<s=reg128:asm/pmul <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t poly* s:>r=reg128:<t=reg128:<s=reg128:asm/pmul >r.{nu},<t.{nu},<s.{nu}' )


for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r *= s:inplace>r=reg128:<r=reg128:<s=reg128:asm/mul <r.{nu},<r.{nu},<s.{nu}' )
  print( f'{n}x r = t * s:>r=reg128:<t=reg128:<s=reg128:asm/mul >r.{nu},<t.{nu},<s.{nu}' )

for n,u in [(8,'h'),(4,'s')]:
  print( '%dx r *= s[n]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( '%dx r = t * s[n]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( '%dx r += t * s[n]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( 'r *= s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( 'r = t * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )
  print( 'r += t * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,u,n,u,u) )


for n,u in [(16,'b'),(8,'h'),(4,'s')]:
  nu = '%d%s'%(n,u)
  print( f'{n}x r += s * t:inplace>r=reg128:<r=reg128:<s=reg128:<t=reg128:asm/mla <r.{nu},<s.{nu},<t.{nu}' )
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


#
# mul scalar
#
for n,u in [(8,'h'),(4,'s')]:
   print( '%dx r = t * s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r *= s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r = t unsigned* s[n/%d]:>r=reg128:<t=reg128:<s=reg128:#n:asm/mul >r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r unsigned*= s[n/%d]:inplace>r=reg128:<r=reg128:<s=reg128:#n:asm/mul <r.%d%s,<r.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r += t * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r += t unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mla <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r -= t * s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mls <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )
   print( '%dx r -= t unsigned* s[n/%d]:inplace>r=reg128:<r=reg128:<t=reg128:<s=reg128:#n:asm/mls <r.%d%s,<t.%d%s,<s.%s[#n]'% (n,n,n,u,n,u,u) )

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


print( '16x r = popcnt s:>r=reg128:<s=reg128:asm/cnt >r.16b,<s.16b' )


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


