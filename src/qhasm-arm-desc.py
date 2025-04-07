#!/usr/bin/python3

import re
import sys


CONDS = [["=","eq"], ["!=","ne"], ["unsigned<","lo"],
         ["!unsigned<","hs"], ["unsigned>","hi"], ["!unsigned>","ls"],
         ["signed<","lt"], ["!signed<","ge"], ["signed>","gt"],
         ["!signed>","le"], ["negative","mi"], ["!negative","pl"],
         ["carry","cs"], ["!carry","cc"]
         #, ["overflow","vs"], ["!overflow","vc"]
]

SS = ["","s"]

SOPS=[["n","$#n","#n",""], ["s","<s","<s=int32",""], 
      ["(s >>> n)","<s,ROR $#n","<s=int32:#n",">?carry:"],
      ["(s >>> u)","<s,ROR <u","<s=int32:<u=int32",">?carry:"],
      ["(s << n)","<s,LSL $#n","<s=int32:#n",">?carry:"],
      ["(s << u)","<s,LSL <u","<s=int32:<u=int32",">?carry:"], 
      ["(s signed>> n)","<s,ASR $#n","<s=int32:#n",">?carry:"],
      ["(s signed>> u)","<s,ASR <u","<s=int32:<u=int32:#n",">?carry:"],
      ["(s unsigned>> n)","<s,LSR $#n","<s=int32:#n",">?carry:"],
      ["(s unsigned>> u)","<s,LSR <u","<s=int32:<u=int32",">?carry:"],
      ["(s carry >>> 1)","<s,RRX","<s=int32",">?carry:"]]

MOVS = [["= ","mov"],["= ~","mvn"]]

AOCS = [["+","adc"], ["-","sbc"]]
AOPS = [["+","add"], ["-","sub"]]
LOPS = [["^","eor"], ["&","and"], ["|","orr"]]
ALOS = [["+","add"], ["-","sub"], ["^","eor"], ["&","and"], ["|","orr"]]

TSTS=[["^","teq",">?negative:>?="], ["&","tst",">?negative:>?="],
      ["-","cmp",#"?negative:>?=:>?carry:>?overflow"
       ">?=:>?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?carry"         
      ],
      ["+","cmn",#"?negative:>?=:>?carry:>?overflow"
       ">?=:>?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?carry"
      ]]

print("goto f:#f:nofallthrough:jump/f:asm/b ._#f:")

for i in CONDS :
    QCOND = i[0]
    ACOND = i[1]
    QFLAG = re.sub(r'!',"",QCOND) 
    print("goto f if %s:#f:jump/f:<?%s:asm/b%s ._#f:" % (QCOND,QFLAG,ACOND))

# NOP
print("nop:asm/nop:")

# IMMEDIATE LOADS
print("r = n:>r=int32:#n:asm/ldr >r,=#n:")
print("r = -n:>r=int32:#n:asm/ldr >r,=-#n:")
       
for i in CONDS :
    QCOND = i[0]
    ACOND = i[1]
    QFLAG = re.sub(r'!',"",QCOND) 
    print("r = n if %s:inplace>r=int32:<r=int32:#n:<?%s:asm/ldr%s <r,=#n:" % (QCOND,QFLAG,ACOND))
    print("r = -n if %s:inplace>r=int32:<r=int32:#n:<?%s:asm/ldr%s <r,=-#n:" % (QCOND,QFLAG,ACOND))


# REV, RBIT
print("r = s[3]s[2]s[1]s[0]:>r=int32:<s=int32:asm/rev >r,<s:")
print("r = rev s:>r=int32:<s=int32:asm/rbit >r,<s:")

# rotates and shifts 
OF=">?carry:>?=:>?negative";
print("r >>>= n !:>r=int32:<r=int32:#n:asm/rors >r,<r,$#n:%s:" % OF) 
print("r >>>= u !:>r=int32:<r=int32:<u=int32:asm/rors >r,<r,<u:%s:" % OF) 
print("r <<= n !:>r=int32:<r=int32:#n:asm/lsls >r,<r,$#n:%s:" % OF) 
print("r <<= u !:>r=int32:<r=int32:<u=int32:asm/lsls >r,<r,<u:%s:" % OF) 
print("r signed>>= n !:>r=int32:<r=int32:#n:asm/asrs >r,<r,$#n:%s:" % OF) 
print("r signed>>= u !:>r=int32:<r=int32:<u=int32:asm/asrs >r,<r,<u:%s:" % OF) 
print("r unsigned>>= n !:>r=int32:<r=int32:#n:asm/lsrs >r,<r,$#n:%s:" % OF) 
print("r unsigned>>= u !:>r=int32:<r=int32:<u=int32:asm/lsrs >r,<r,<u:%s:" % OF) 
print("r carry >>>= 1 !:>r=int32:<r=int32:asm/rrxs >r,<r:%s:<?carry:" % OF)

print("r = s >>> n !:>r=int32:<s=int32:#n:asm/rors >r,<s,$#n:%s:" % OF) 
print("r = s >>> u !:>r=int32:<s=int32:<u=int32:asm/rors >r,<s,<u:%s:" % OF) 
print("r = s << n !:>r=int32:<s=int32:#n:asm/lsls >r,<s,$#n:%s:" % OF) 
print("r = s << u !:>r=int32:<s=int32:<u=int32:asm/lsls >r,<s,<u:%s:" % OF) 
print("r = s signed>> n !:>r=int32:<s=int32:#n:asm/asrs >r,<s,$#n:%s:" % OF) 
print("r = s signed>> u !:>r=int32:<s=int32:<u=int32:asm/asrs >r,<s,<u:%s:" % OF) 
print("r = s unsigned>> n !:>r=int32:<s=int32:#n:asm/lsrs >r,<s,$#n:%s:" % OF) 
print("r = s unsigned>> u !:>r=int32:<s=int32:<u=int32:asm/lsrs >r,<s,<u:%s:" % OF) 
print("r = s carry >>> 1 !:>r=int32:<s=int32:asm/rrxs >r,<s:%s:<?carry:" % OF)

print("r >>>= n:>r=int32:<r=int32:#n:asm/ror >r,<r,$#n:") 
print("r >>>= u:>r=int32:<r=int32:<u=int32:asm/ror >r,<r,<u:") 
print("r <<= n:>r=int32:<r=int32:#n:asm/lsl >r,<r,$#n:") 
print("r <<= u:>r=int32:<r=int32:<u=int32:asm/lsl >r,<r,<u:") 
print("r signed>>= n:>r=int32:<r=int32:#n:asm/asr >r,<r,$#n:") 
print("r signed>>= u:>r=int32:<r=int32:<u=int32:asm/asr >r,<r,<u:") 
print("r unsigned>>= n:>r=int32:<r=int32:#n:asm/lsr >r,<r,$#n:") 
print("r unsigned>>= u:>r=int32:<r=int32:<u=int32:asm/lsr >r,<r,<u:") 
print("r carry >>>= 1:>r=int32:<r=int32:asm/rrx >r,<r:<?carry:>?carry:")

print("r = s >>> n:>r=int32:<s=int32:#n:asm/ror >r,<s,$#n:") 
print("r = s >>> u:>r=int32:<s=int32:<u=int32:asm/ror >r,<s,<u:") 
print("r = s << n:>r=int32:<s=int32:#n:asm/lsl >r,<s,$#n:") 
print("r = s << u:>r=int32:<s=int32:<u=int32:asm/lsl >r,<s,<u:") 
print("r = s signed>> n:>r=int32:<s=int32:#n:asm/asr >r,<s,$#n:") 
print("r = s signed>> u:>r=int32:<s=int32:<u=int32:asm/asr >r,<s,<u:") 
print("r = s unsigned>> n:>r=int32:<s=int32:#n:asm/lsr >r,<s,$#n:") 
print("r = s unsigned>> u:>r=int32:<s=int32:<u=int32:asm/lsr >r,<s,<u:")  
print("r = s carry >>> 1:>r=int32:<s=int32:asm/rrxs >r,<s:<?carry:>?carry:")

# NEG
print("r = -s:>r=int32:<s=int32:asm/neg >r,<s:")

# MOV and MVN
for MOV in MOVS :
    QMOV=MOV[0]
    AMOV=MOV[1]
    OF=">?negative:?>="
    for SOP in SOPS :
        QSOP=SOP[0]
        ASOP=SOP[1]
        QOPR=SOP[2]
        QOF= SOP[3]
  
        print("r %s%s:>r=int32:<s=int32:%s:asm/%s >r,%s:" % (QMOV,QSOP,QOPR,AMOV,ASOP))
        print("r %s%s !:>r=int32:<s=int32:%s:%s:asm/%ss >r,%s:%s" % (QMOV,QSOP,QOPR,OF,AMOV,ASOP,QOF))
        for i in CONDS :
            QCOND= i[0]
            ACOND= i[1]
            QFLAG= re.sub(r'!',"",QCOND) 

            print("r %s%s if %s:inplace>r=int32:<r=int32:<s=int32:<?%s:%s:asm/%s%s <r,%s:" % (QMOV,QSOP,QCOND,QFLAG,QOPR,AMOV,ACOND,ASOP))
            print("r %s%s if %s !:inplace>r=int32:<r=int32:<s=int32:<?%s:%s:%s:asm/%ss%s <r,%s:%s" % (QMOV,QSOP,QCOND,QFLAG,QOPR,OF,AMOV,ACOND,ASOP,QOF))

 

print("bigendian:asm/setend be:")
print("littleendian:asm/setend le:")

for OP in ALOS :
    QOP = OP[0]
    AOP = OP[1]
    if re.match(r"[+-]",QOP) :  OF=">?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?carry:>?="
    else : OF=">?negative:>?="

    #print $OP, $QOP, $AOP, $OF, "\n";
    for SOP in SOPS :
        QSOP=SOP[0]
        ASOP=SOP[1]
        QOPR=SOP[2]
        if re.match(r"[+-]",QOP) : QOF= ""
        else : QOF= SOP[3]
        print("r %s= %s:>r=int32:<r=int32:%s:asm/%s >r,<r,%s:" % (QOP,QSOP,QOPR,AOP,ASOP))
        print("r = t %s %s:>r=int32:<t=int32:%s:asm/%s >r,<t,%s:" % (QOP,QSOP,QOPR,AOP,ASOP))
        print("r %s= %s !:>r=int32:<r=int32:%s:asm/%ss >r,<r,%s:%s:%s" % (QOP,QSOP,QOPR,AOP,ASOP,OF,QOF))
        print("r = t %s %s !:>r=int32:<t=int32:%s:asm/%ss >r,<t,%s:%s:%s" % (QOP,QSOP,QOPR,AOP,ASOP,OF,QOF))    
        for i in CONDS :
            QCOND= i[0]
            ACOND= i[1]
            QFLAG= re.sub(r'!',"",QCOND) 
        
            print("r = t %s %s if %s:<r=int32:<t=int32:%s:<?%s:asm/%s%s <r,<t,%s:" % (QOP,QSOP,QCOND,QOPR,QFLAG,AOP,ACOND,ASOP))
            print("r %s= %s if %s:inplace>r=int32:<r=int32:%s:<?%s:asm/%s%s <r,<r,%s:" % (QOP,QSOP,QCOND,QOPR,QFLAG,AOP,ACOND,ASOP))    
            print("r = t %s %s if %s !:<r=int32:<t=int32:%s:<?%s:asm/%ss%s <r,<t,%s:%s:%s" % (QOP,QSOP,QCOND,QOPR,QFLAG,AOP,ACOND,ASOP,OF,QOF))
            print("r %s= %s if %s !:inplace>r=int32:<r=int32:%s:<?%s:asm/%ss%s <r,<r,%s:%s:%s" % (QOP,QSOP,QCOND,QOPR,QFLAG,AOP,ACOND,ASOP,OF,QOF))  


# BIC

for SOP in SOPS :
    QSOP=SOP[0]
    ASOP=SOP[1]
    QOPR=SOP[2]
    QOF= SOP[3]

    for S in SS :
        if (S!="") :
            OF=(">?negative:>?=:%s" % (QOF)); NF=" !"
        else :
            OF=""; NF=""
        
        print("r = t & ~%s%s:>r=int32:<t=int32:%s:asm/bic%s >r,<t,%s:%s" % (QSOP,NF,QOPR,S,ASOP,OF))
        print("r &= ~%s%s:>r=int32:<r=int32:%s:asm/bic%s >r,<r,%s:%s" % (QSOP,NF,QOPR,S,ASOP,OF))

        for i in CONDS :
            QCOND= i[0]
            ACOND= i[1]
            QFLAG= re.sub(r'!',"",QCOND) 
            print("r = t & ~%s if %s%s:inplace>r=int32:<r=int32:<t=int32:%s:<?%s:asm/bic%s%s <r,<t,%s:%s" % (QSOP,QCOND,NF,QOPR,QFLAG,S,ACOND,ASOP,OF))
            print("r &= ~%s if %s%s:inplace>r=int32:<r=int32:<r=int32:%s:<?%s:asm/bic%s%s <r,<r,%s:%s" % (QSOP,QCOND,NF,QOPR,QFLAG,S,ACOND,ASOP,OF))


# RSB
for SOP in SOPS :
    QSOP=SOP[0]
    ASOP=SOP[1]
    QOPR=SOP[2]
    QOF= SOP[3]

    for S in SS :
        if (S!="") :
            OF=">?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?=:>?carry:"; NF=" !";
        else :
            OF=""; NF=""
        print("r = - t + %s%s:>r=int32:<t=int32:%s:asm/rsb%s >r,<t,%s:%s" %(QSOP,NF,QOPR,S,ASOP,OF))

        for i in CONDS :
            QCOND= i[0]
            ACOND= i[1]
            QFLAG= re.sub(r'!',"",QCOND) 
            
            print("r = - t + %s if %s%s:inplace>r=int32:<r=int32:<t=int32:%s:<?%s:asm/rsb%s%s <r,<t,%s:%s" % (QSOP,QCOND,NF,QOPR,QFLAG,S,ACOND,ASOP,OF)) 


for OP in AOCS :
    QOP = OP[0]
    for S in SS :
        if (S!="") :
            OF=">?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?=:>?carry:<?carry:"; NF=" !"
        else : OF="<?carry:"; NF=""
    
        AOP = OP[1] + S

        for SOP in SOPS :
            QSOP=SOP[0]
            ASOP=SOP[1]
            QOPR=SOP[2]
            QOF= SOP[3]

            print("r %s= %s %s carry%s:>r=int32:<r=int32:%s:asm/%s >r,<r,%s:%s" % (QOP,QSOP,QOP,NF,QOPR,AOP,ASOP,OF))
            print("r = t %s %s %s carry%s:>r=int32:<t=int32:%s:asm/%s >r,<t,%s:%s" % (QOP,QSOP,QOP,NF,QOPR,AOP,ASOP,OF))
            
            for i in CONDS :
                QCOND= i[0]
                ACOND= i[1]
                QFLAG= re.sub(r'!',"",QCOND) 
                print("r %s= %s %s carry if %s%s:inplace>r=int32:<r=int32:<r=int32:%s:asm/%s%s <r,<r,%s:<?%s:%s" % (QOP,QSOP,QOP,QCOND,NF,QOPR,AOP,ACOND,ASOP,QFLAG,OF))
                print("r = t %s %s %s carry if %s%s:inplace>r=int32:<r=int32:<t=int32:%s:asm/%s%s <r,<r,%s:<?%s:%s" % (QOP,QSOP,QOP,QCOND,NF,QOPR,AOP,ACOND,ASOP,QFLAG,OF))


for TST in TSTS :
    QTST = TST[0]
    ATST = TST[1]
    OF   = TST[2]
    
    for SOP in SOPS :
        QSOP=SOP[0]
        ASOP=SOP[1]
        QOPR=SOP[2]
        if re.match(r"[+-]",QTST) : QOF= ""
        else : QOF = SOP[3]

        print("r %s %s:<r=int32:%s:asm/%s <r,%s:%s:%s" % (QTST,QSOP,QOPR,ATST,ASOP,OF,QOF))

        for i in CONDS :
            QCOND= i[0]
            ACOND= i[1]
            QFLAG= re.sub(r'!',"",QCOND) 
            
            print("r %s %s if %s:<r=int32:%s:asm/%s%s <r,%s:<?%s:%s:%s" % (QTST,QSOP,QCOND,QOPR,ATST,ACOND,ASOP,QFLAG,OF,QOF))



# MUL MLA UMULL UMLAL SMULL SMLAL no flags version (clearly better) only
print("r *= s:inplace>r=int32:<r=int32:<s=int32:asm/mul >r,<s,<r:")
print("r = s * t:>r=int32:<s=int32:<t=int32:asm/mul >r,<s,<t:")
print("r = s * t + u:>r=int32:<s=int32:<t=int32:<u=int32:asm/mla >r,<s,<t,<u:")
print("r += s * t:inplace>r=int32:<r=int32:<s=int32:<t=int32:asm/mla >r,<s,<t,<r:")
print("unsigned r s = t * u:>r=int32:>s=int32:<t=int32:<u=int32:asm/umull >s,>r,<t,<u:")
print("unsigned r s += t * u:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umlal <s,<r,<t,<u:")
print("unsigned r s = t * u + r + s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umaal <s,<r,<t,<u:")
print("signed r s = t * u:>r=int32:>s=int32:<t=int32:<u=int32:asm/smull >s,>r,<t,<u:")
print("signed r s += t * u:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/smlal <s,<r,<t,<u:")
for i in CONDS :
    QCOND= i[0]
    ACOND= i[1]
    QFLAG= re.sub(r'!',"",QCOND) 
    
    print("r *= s if %s:inplace>r=int32:<r=int32:<r=int32:<s=int32:asm/mul%s <r,<s,<r:<%s:" % (QCOND,ACOND,QFLAG))
    print("r = s * t if %s:inplace>r=int32:<r=int32:<s=int32:<t=int32:asm/mul%s <r,<s,<t:<%s:" % (QCOND,ACOND,QFLAG))
    print("r = s * t + u if %s:inplace>r=int32:<r=int32:<s=int32:<t=int32:<u=int32:asm/mla%s <r,<s,<t,<u:<%s:" % (QCOND,ACOND,QFLAG))
    print("unsigned r s = t * u if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umull%s <s,<r,<t,<u:<%s:"% (QCOND,ACOND,QFLAG))
    print("unsigned r s += t * u if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umlal%s <s,<r,<t,<u:<%s:"% (QCOND,ACOND,QFLAG))
    print("unsigned r s = t * u + r + s if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umaal%s <s,<r,<t,<u:<%s:"% (QCOND,ACOND,QFLAG))
    print("signed r s = t * u if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/smull%s <s,<r,<t,<u:<%s:"% (QCOND,ACOND,QFLAG))
    print("signed r s += t * u if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/smlal%s <s,<r,<t,<u:<%s:"% (QCOND,ACOND,QFLAG)) 

LDTYPE = [["","","32"],["signed ","sb","8"],["unsigned ","b","8"],
	  ["signed ","sh","16"],["unsigned ","h","16"]]

for i in LDTYPE :
    LDSGN = i[0]
    LDSUF = i[1]
    LDLEN = i[2]

    print("r = %smem%s[s]:>r=int32:<s=int32:asm/ldr%s >r,[<s]:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s + n]:>r=int32:<s=int32:#n:asm/ldr%s >r,[<s,$#n]:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s - n]:>r=int32:<s=int32:#n:asm/ldr%s >r,[<s,$-#n]:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s]; s += n:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s >r,[<s],$#n:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s]; s -= n:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s >r,[<s],$-#n:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s += n]:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s >r,[<s,$#n]!:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s -= n]:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s >r,[<s,$-#n]!:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s + t]:>r=int32:<s=int32:<t=int32:asm/ldr%s >r,[<s,<t]:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s + (t << n)]:>r=int32:<s=int32:<t=int32:#n:asm/ldr%s >r,[<s,<t, LSL $#n]:" % (LDSGN,LDLEN,LDSUF))
    print("r = %smem%s[s + (t unsigned>> n)]:>r=int32:<s=int32:<t=int32:#n:asm/ldr%s >r,[<s,<t, LSR $#n]:" % (LDSGN,LDLEN,LDSUF))

    for i in CONDS :
        QCOND= i[0]
        ACOND= i[1]
        QFLAG= re.sub(r'!',"",QCOND) 

        print("r = %smem%s[s] if %s:inplace>r=int32:<r=int32:<s=int32:asm/ldr%s%s <r,[<s]:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s + n] if %s:inplace>r=int32:<r=int32:<s=int32:#n:asm/ldr%s%s <r,[<s,$#n]:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s - n] if %s:inplace>r=int32:<r=int32:<s=int32:#n:asm/ldr%s%s <r,[<s,$-#n]:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s]; s += n if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s%s <r,[<s],$#n:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s]; s -= n if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s%s <r,[<s],$-#n:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s += n] if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s%s <r,[<s,$#n]!:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s -= n] if %s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr%s%s <r,[<s,$-#n]!:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))
        print("r = %smem%s[s + (t << n)] if %s:inplace>r=int32:<r=int32:<s=int32:<t=int32:#n:asm/ldr%s%s <r,[<s,<t, LSL $#n]:<?%s:" % (LDSGN,LDLEN,QCOND,LDSUF,ACOND,QFLAG))

STTYPE = [["","32"],["b","8"],["h","16"]]

for i in STTYPE :
    STSUF = i[0]
    STLEN = i[1]
    
    print("mem%s[s] = r:<r=int32:<s=int32:asm/str%s <r,[<s]:" % (STLEN,STSUF))
    print("mem%s[s + n] = r:<r=int32:<s=int32:#n:asm/str%s <r,[<s,$#n]:" % (STLEN,STSUF))
    print("mem%s[s - n] = r:<r=int32:<s=int32:#n:asm/str%s <r,[<s,$-#n]:" % (STLEN,STSUF))
    print("mem%s[s] = r; s += n:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s <r,[<s],$#n:" % (STLEN,STSUF))
    print("mem%s[s] = r; s -= n:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s <r,[<s],$-#n:" % (STLEN,STSUF))
    print("mem%s[s += n] = r:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s <r,[<s,$#n]!:" % (STLEN,STSUF))
    print("mem%s[s -= n] = r:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s <r,[<s,$-#n]!:" % (STLEN,STSUF))
    print("mem%s[s + (t << n)] = r:<r=int32:<s=int32:<t=int32:#n:asm/str%s <r,[<s,<t, LSL $#n]:" % (STLEN,STSUF))

    for i in CONDS :
        QCOND= i[0]
        ACOND= i[1]
        QFLAG= re.sub(r'!',"",QCOND) 

        print("mem%s[s] = r if %s:<r=int32:<s=int32:asm/str%s%s <r,[<s]:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s + n] = r if %s:<r=int32:<s=int32:#n:asm/str%s%s <r,[<s,$#n]:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s - n] = r if %s:<r=int32:<s=int32:#n:asm/str%s%s <r,[<s,$-#n]:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s] = r; s += n if %s:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s%s <r,[<s],$#n:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s] = r; s -= n if %s:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s%s <r,[<s],$-#n:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s += n] = r if %s:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s%s <r,[<s,$#n]!:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s -= n] = r if %s:<r=int32:inplace>s=int32:<s=int32:#n:asm/str%s%s <r,[<s,$-#n]!:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))
        print("mem%s[s + (t << n)] = r if %s:<r=int32:<s=int32:<t=int32:#n:asm/str%s%s <r,[<s,<t, LSL $#n]:<?%s:" % (STLEN,QCOND,STSUF,ACOND,QFLAG))



print("assign r0 to r:<r=int32#1:")
print("assign r1 to r:<r=int32#2:")
print("assign r2 to r:<r=int32#3:")
print("assign r3 to r:<r=int32#4:")
print("assign r4 to r:<r=int32#5:")
print("assign r5 to r:<r=int32#6:")
print("assign r6 to r:<r=int32#7:")
print("assign r7 to r:<r=int32#8:")
print("assign r8 to r:<r=int32#9:")
print("assign r9 to r:<r=int32#10:")
print("assign r10 to r:<r=int32#11:")
print("assign r11 to r:<r=int32#12:")
print("assign r12 to r:<r=int32#13:")
print("assign r14 to r:<r=int32#14:")

print("r = s:>r=int32:<s=stack32:asm/ldr >r,<s:")
print("s = r:<r=int32:>s=stack32:asm/str <r,>s:")

for i in CONDS :
    QCOND= i[0]
    ACOND= i[1]
    QFLAG= re.sub(r'!',"",QCOND) 
    print("r = s if %s:inplace>r=int32:<r=int32:<s=stack32:<?%s:asm/ldr%s <r,<s:"% (QCOND,QFLAG,ACOND))
    print("s = r if %s:<r=int32:inplace>s=stack32:<s=stack32:<?%s:asm/ldr%s <r,<s:"% (QCOND,QFLAG,ACOND))


# BFI BFC SBFX UBFX

print("r = s signed n bits from pos m:>r=int32:<s=int32:#n:#m:asm/sbfx >r,<s,$#m,$#n:")
print("r = s unsigned n bits from pos m:>r=int32:<s=int32:#n:#m:asm/ubfx >r,<s,$#m,$#n:")
print("r = (s << (32 - m - n)) unsigned>> (32 - m):>r=int32:<s=int32:#n:#m:asm/sbfx >r,<s,$#m,$#n:")
print("r = (s << (32 - m - n)) unsigned>> (32 - m):>r=int32:<s=int32:#n:#m:asm/ubfx >r,<s,$#m,$#n:")
print("r insert right n bits in s from pos m:>r=int32:<s=int32:#n:#m:asm/bfi >r,<s,$#m,$#n:")

# this is armv7, where STRD and LDRD only works on an even-odd pair

PAIRS = [["r0 r1","1","2"], ["r2 r3","3","4"], ["r4 r5","5","6"],
         ["r6 r7","7","8"], ["r8 r9","9","10"], ["r10 r11","11","12"]]


for i in PAIRS :
    print("assign %s to r s;mem64[t + n] = r s:<r=int32#%s:<s=int32#%s:<t=int32:#n:asm/strd <r,[<t,$#n]:" % (i[0],i[1],i[2]))
    print("assign %s to r s;mem64[t] = r s;t += n:<r=int32#%s:<s=int32#%s:<t=int32:#n:asm/strd <r,[<t],$#n:" % (i[0],i[1],i[2]))    
    print("assign %s to r s;mem64[t + u] = r s:<r=int32#%s:<s=int32#%s:<t=int32:<u=int32:asm/strd <r,[<t,<u]:" % (i[0],i[1],i[2]))
    print("assign %s to r s;t = r s:<r=int32#%s:<s=int32#%s:>t=stack64:#n:asm/strd <r,>t:" % (i[0],i[1],i[2]))
    print("assign %s to r s;mem64[&t] = r s:<r=int32#%s:<s=int32#%s:>t=stack32:#n:asm/strd <r,>t:" % (i[0],i[1],i[2]))
    print("assign %s to r s = mem64[t + n]:>r=int32#%s:>s=int32#%s:<t=int32:#n:asm/ldrd >r,[<t,$#n]:" % (i[0],i[1],i[2]))
    print("assign %s to r s = mem64[t]; t += n:>r=int32#%s:>s=int32#%s:<t=int32:#n:asm/ldrd >r,[<t],$#n:" % (i[0],i[1],i[2]))
    print("assign %s to r s = mem64[t + u]:>r=int32#%s:>s=int32#%s:<t=int32:<u=int32:asm/ldrd >r,[<t,<u]:" % (i[0],i[1],i[2]))
    print("assign %s to r s = t:>r=int32#%s:>s=int32#%s:<t=stack64:#n:asm/ldrd >r,<t:" % (i[0],i[1],i[2]))    
    print("assign %s to r s = mem64[&t]:>r=int32#%s:>s=int32#%s:<t=stack32:#n:asm/ldrd >r,<t:" % (i[0],i[1],i[2]))    
    for j in CONDS :
        QCOND= j[0]
        ACOND= j[1]
        QFLAG= re.sub(r'!',"",QCOND) 

        print("assign %s to r s;mem64[t + n] = r s if %s:<r=int32#%s:<s=int32#%s:<t=int32:#n:<?%s:asm/strd%s <r,[<t,$#n]:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))
        print("assign %s to r s;mem64[t] = r s;t += n if %s:<r=int32#%s:<s=int32#%s:<t=int32:#n:<?%s:asm/strd%s <r,[<t],$#n:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))    
        print("assign %s to r s;mem64[t + u] = r s if %s:<r=int32#%s:<s=int32#%s:<t=int32:<u=int32:<?%s:asm/strd%s <r,[<t,<u]:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))
        print("assign %s to r s;t = r s if %s:<r=int32#%s:<s=int32#%s:>t=stack64:#n:<?%s:asm/strd%s <r,>t:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))
        print("assign %s to r s = mem64[t + n] if %s:>r=int32#%s:>s=int32#%s:<t=int32:#n:<?%s:asm/ldrd%s >r,[<t,$#n]:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))
        print("assign %s to r s = mem64[t]; t += n if %s:>r=int32#%s:>s=int32#%s:<t=int32:#n:<?%s:asm/ldrd%s >r,[<t],$#n:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))
        print("assign %s to r s = mem64[t + u] if %s:>r=int32#%s:>s=int32#%s:<t=int32:<u=int32:<?%s:asm/ldrd%s >r,[<t,<u]:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))
        print("assign %s to r s = t if %s:>r=int32#%s:>s=int32#%s:<t=stack64:#n:<?%s:asm/ldrd%s >r,<t:" % (i[0],QCOND,i[1],i[2],QFLAG,ACOND))    
    
    
for i in range(3,15) :
    for j in range(2,i) :
        for k in range(1,j) :
            print("r s t = mem96[a]:>r=int32#%s:>s=int32#%s:>t=int32#%s:<a=int32:asm/ldm <a,{>r,>s,>t}:" % (k,j,i))
            print("r s t = mem96[a];a+=12:>r=int32#%s:>s=int32#%s:>t=int32#%s:inplace>a=int32:<a=int32:asm/ldm <a!,{>r,>s,>t}:" % (k,j,i))
            print("mem96[a] = r s t:<r=int32#%s:<s=int32#%s:<t=int32#%s:<a=int32:asm/stm <a,{<r,<s,<t}:" % (k,j,i))
            print("mem96[a] = r s t;a+=12:<r=int32#%s:<s=int32#%s:<t=int32#%s:inplace>a=int32:<a=int32:asm/stm <a!,{<r,<s,<t}:" % (k,j,i))
            print("r s t = mem96[a-12]:>r=int32#%s:>s=int32#%s:>t=int32#%s:<a=int32:asm/ldmdb <a,{>r,>s,>t}:" % (k,j,i))
            print("r s t = mem96[a-=12]:>r=int32#%s:>s=int32#%s:>t=int32#%s:inplace>a=int32:<a=int32:asm/ldmdb <a!,{>r,>s,>t}:" % (k,j,i))
            print("mem96[a-12] = r s t:<r=int32#%s:<s=int32#%s:<t=int32#%s:<a=int32:asm/stmdb <a,{<r,<s,<t}:" % (k,j,i))
            print("mem96[a-=12] = r s t:<r=int32#%s:<s=int32#%s:<t=int32#%s:inplace>a=int32:<a=int32:asm/stmdb <a!,{<r,<s,<t}:" % (k,j,i))


for i in range(4,15) :
    for j in range(3,i) :
        for k in range(2,j) :
            for l in range(1,k) :
                print("r s t u = mem128[a]:>r=int32#%s:>s=int32#%s:>t=int32#%s:>u=int32#%s:<a=int32:asm/ldm <a,{>r,>s,>t,>u}:" % (l,k,j,i))
                print("r s t u = mem128[a];a+=16:>r=int32#%s:>s=int32#%s:>t=int32#%s:>u=int32#%s:inplace>a=int32:<a=int32:asm/ldm <a!,{>r,>s,>t,>u}:" % (l,k,j,i))
                print("mem128[a] = r s t u:<r=int32#%s:<s=int32#%s:<t=int32#%s:<u=int32#%s:<a=int32:asm/stm <a,{<r,<s,<t,<u}:" % (l,k,j,i))
                print("mem128[a] = r s t u;a+=16:<r=int32#%s:<s=int32#%s:<t=int32#%s:<u=int32#%s:inplace>a=int32:<a=int32:asm/stm <a!,{<r,<s,<t,<u}:" % (l,k,j,i))
                print("r s t u = mem128[a-16]:>r=int32#%s:>s=int32#%s:>t=int32#%s:>u=int32#%s:<a=int32:asm/ldmdb <a,{>r,>s,>t,>u}:" % (l,k,j,i))
                print("r s t u = mem128[a-=16]:>r=int32#%s:>s=int32#%s:>t=int32#%s:>u=int32#%s:inplace>a=int32:<a=int32:asm/ldmdb <a!,{>r,>s,>t,>u}:" % (l,k,j,i))
                print("mem128[a-16] = r s t u:<r=int32#%s:<s=int32#%s:<t=int32#%s:<u=int32#%s:<a=int32:asm/stmdb <a,{<r,<s,<t,<u}:" % (l,k,j,i))
                print("mem128[a-=16] = r s t u:<r=int32#%s:<s=int32#%s:<t=int32#%s:<u=int32#%s:inplace>a=int32:<a=int32:asm/stmdb <a!,{<r,<s,<t,<u}:" % (l,k,j,i))
