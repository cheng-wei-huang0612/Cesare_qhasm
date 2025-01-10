#!/usr/bin/perl

@CONDS = (["=","eq"], ["!=","ne"], ["unsigned<","lo"],
	  ["!unsigned<","hs"], ["unsigned>","hi"], ["!unsigned>","ls"],
	  ["signed<","lt"], ["!signed<","ge"], ["signed>","gt"],
	  ["!signed>","le"], ["negative","mi"], ["!negative","pl"],
	  ["carry","cs"], ["!carry","cc"] 
	  #, ["overflow","vs"], ["!overflow","vc"] 
    );

@SS = ("","s");

@SOPS=( ["n","\$#n","#n",""], ["s","<s","<s=int32",""], 
       ["(s >>> n)","<s,ROR \$#n","<s=int32:#n",">?carry:"],
       ["(s >>> u)","<s,ROR <u","<s=int32:<u=int32",">?carry:"],
       ["(s << n)","<s,LSL \$#n","<s=int32:#n",">?carry:"],
       ["(s << u)","<s,LSL <u","<s=int32:<u=int32",">?carry:"], 
       ["(s signed>> n)","<s,ASR \$#n","<s=int32:#n",">?carry:"],
       ["(s signed>> u)","<s,ASR <u","<s=int32:<u=int32:#n",">?carry:"],
       ["(s unsigned>> n)","<s,LSR \$#n","<s=int32:#n",">?carry:"],
       ["(s unsigned>> u)","<s,LSR <u","<s=int32:<u=int32",">?carry:"],
       ["(s carry >>> 1)","<s,RRX","<s=int32",">?carry:"]
    );
       
@MOVS = (["= ","mov"],["= ~","mvn"]);

@AOCS = (["+","adc"], ["-","sbc"]);
@AOPS = (["+","add"], ["-","sub"]);
@LOPS = (["^","eor"], ["&","and"], ["|","orr"]);
@ALOS = (["+","add"], ["-","sub"], ["^","eor"], ["&","and"], ["|","orr"]);

@TSTS=(["^","teq",">?negative:>?="], ["&","tst",">?negative:>?="],
      ["-","cmp",#"?negative:>?=:>?carry:>?overflow"
       ">?=:>?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?carry"         
      ],
       ["+","cmn",#"?negative:>?=:>?carry:>?overflow"
	">?=:>?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?carry"
       ]);


# BRANCHES
print "goto f:#f:nofallthrough:jump/f:asm/b ._#f:\n";

foreach $i (@CONDS) {
    $QCOND= $i->[0];
    $ACOND= $i->[1];
    ($QFLAG = $QCOND) =~ s/!//;
    print "goto f if $QCOND:#f:jump/f:<?$QFLAG:asm/b$ACOND ._#f:\n";
}


# NOP
print "nop:asm/nop:\n"; 

# IMMEDIATE LOADS
print "r = n:>r=int32:#n:asm/ldr >r,=#n:\n";
print "r = -n:>r=int32:#n:asm/ldr >r,=-#n:\n";
       
for $i (@CONDS) {
    $QCOND= $i->[0];
    $ACOND= $i->[1];
    ($QFLAG = $QCOND) =~ s/!//;
    print "r = n if $QCOND:inplace>r=int32:<r=int32:#n:<?$QFLAG:asm/ldr$ACOND <r,=#n:\n";
    print "r = -n if $QCOND:inplace>r=int32:<r=int32:#n:<?$QFLAG:asm/ldr$ACOND <r,=-#n:\n";
}

# REV, RBIT
print "r = s[3]s[2]s[1]s[0]:>r=int32:<s=int32:asm/rev >r,<s:\n";
print "r = rev s:>r=int32:<s=int32:asm/rbit >r,<s:\n";

# rotates and shifts 
$OF=">?carry:>?=:>?negative";
print "r >>>= n !:>r=int32:<r=int32:#n:asm/rors >r,<r,\$#n:$OF:\n"; 
print "r >>>= u !:>r=int32:<r=int32:<u=int32:asm/rors >r,<r,<u:$OF:\n"; 
print "r <<= n !:>r=int32:<r=int32:#n:asm/lsls >r,<r,\$#n:$OF:\n"; 
print "r <<= u !:>r=int32:<r=int32:<u=int32:asm/lsls >r,<r,<u:$OF:\n"; 
print "r signed>>= n !:>r=int32:<r=int32:#n:asm/asrs >r,<r,\$#n:$OF:\n"; 
print "r signed>>= u !:>r=int32:<r=int32:<u=int32:asm/asrs >r,<r,<u:$OF:\n"; 
print "r unsigned>>= n !:>r=int32:<r=int32:#n:asm/lsrs >r,<r,\$#n:$OF:\n"; 
print "r unsigned>>= u !:>r=int32:<r=int32:<u=int32:asm/lsrs >r,<r,<u:$OF:\n"; 
print "r carry >>>= 1 !:>r=int32:<r=int32:asm/rrxs >r,<r:$OF:<?carry:\n";

print "r = s >>> n !:>r=int32:<s=int32:#n:asm/rors >r,<s,\$#n:$OF:\n"; 
print "r = s >>> u !:>r=int32:<s=int32:<u=int32:asm/rors >r,<s,<u:$OF:\n"; 
print "r = s << n !:>r=int32:<s=int32:#n:asm/lsls >r,<s,\$#n:$OF:\n"; 
print "r = s << u !:>r=int32:<s=int32:<u=int32:asm/lsls >r,<s,<u:$OF:\n"; 
print "r = s signed>> n !:>r=int32:<s=int32:#n:asm/asrs >r,<s,\$#n:$OF:\n"; 
print "r = s signed>> u !:>r=int32:<s=int32:<u=int32:asm/asrs >r,<s,<u:$OF:\n"; 
print "r = s unsigned>> n !:>r=int32:<s=int32:#n:asm/lsrs >r,<s,\$#n:$OF:\n"; 
print "r = s unsigned>> u !:>r=int32:<s=int32:<u=int32:asm/lsrs >r,<s,<u:$OF:\n"; 
print "r = s carry >>> 1 !:>r=int32:<s=int32:asm/rrxs >r,<s:$OF:<?carry:\n";

print "r >>>= n:>r=int32:<r=int32:#n:asm/ror >r,<r,\$#n:\n"; 
print "r >>>= u:>r=int32:<r=int32:<u=int32:asm/ror >r,<r,<u:\n"; 
print "r <<= n:>r=int32:<r=int32:#n:asm/lsl >r,<r,\$#n:\n"; 
print "r <<= u:>r=int32:<r=int32:<u=int32:asm/lsl >r,<r,<u:\n"; 
print "r signed>>= n:>r=int32:<r=int32:#n:asm/asr >r,<r,\$#n:\n"; 
print "r signed>>= u:>r=int32:<r=int32:<u=int32:asm/asr >r,<r,<u:\n"; 
print "r unsigned>>= n:>r=int32:<r=int32:#n:asm/lsr >r,<r,\$#n:\n"; 
print "r unsigned>>= u:>r=int32:<r=int32:<u=int32:asm/lsr >r,<r,<u:\n"; 
print "r carry >>>= 1:>r=int32:<r=int32:asm/rrx >r,<r:<?carry:>?carry:\n";

print "r = s >>> n:>r=int32:<s=int32:#n:asm/ror >r,<s,\$#n:\n"; 
print "r = s >>> u:>r=int32:<s=int32:<u=int32:asm/ror >r,<s,<u:\n"; 
print "r = s << n:>r=int32:<s=int32:#n:asm/lsl >r,<s,\$#n:\n"; 
print "r = s << u:>r=int32:<s=int32:<u=int32:asm/lsl >r,<s,<u:\n"; 
print "r = s signed>> n:>r=int32:<s=int32:#n:asm/asr >r,<s,\$#n:\n"; 
print "r = s signed>> u:>r=int32:<s=int32:<u=int32:asm/asr >r,<s,<u:\n"; 
print "r = s unsigned>> n:>r=int32:<s=int32:#n:asm/lsr >r,<s,\$#n:\n"; 
print "r = s unsigned>> u:>r=int32:<s=int32:<u=int32:asm/lsr >r,<s,<u:\n";  
print "r = s carry >>> 1:>r=int32:<s=int32:asm/rrxs >r,<s:<?carry:>?carry:\n";

# NEG
print "r = -s:>r=int32:<s=int32:asm/neg >r,<s:\n";

# MOV and MVN
for $MOV (@MOVS) {
    $QMOV=$MOV->[0];
    $AMOV=$MOV->[1];
    $OF=">?negative:?>=";
    for my $SOP (@SOPS) {
	$QSOP=$SOP->[0];
	$ASOP=$SOP->[1];
	$QOPR=$SOP->[2];
	$QOF= $SOP->[3];
  
	print "r $QMOV$QSOP:>r=int32:<s=int32:$QOPR:asm/$AMOV >r,$ASOP:\n";
	print "r $QMOV$QSOP !:>r=int32:<s=int32:$QOPR:$OF:asm/${AMOV}s >r,$ASOP:$QOF\n";
	for $i (@CONDS) {
	    $QCOND= $i->[0];
	    $ACOND= $i->[1];
	    ($QFLAG = $QCOND) =~ s/!//;

	    print "r $QMOV$QSOP if $QCOND:inplace>r=int32:<r=int32:<s=int32:<?$QFLAG:$QOPR:asm/$AMOV$ACOND <r,$ASOP:\n";
	    print "r $QMOV$QSOP if $QCOND !:inplace>r=int32:<r=int32:<s=int32:<?$QFLAG:$QOPR:$OF:asm/${AMOV}s${ACOND} <r,$ASOP:$QOF\n";
	}
    }
}
 

print "bigendian:asm/setend be:\n";
print "littleendian:asm/setend le:\n";

for $OP (@ALOS) {
    $QOP = $OP->[0];
    $AOP = $OP->[1];
    if ($QOP =~ m/[+-]/) {
	$OF=">?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?carry:>?=";
    } else { $OF=">?negative:>?="; }

    #print $OP, $QOP, $AOP, $OF, "\n";
    for my $SOP (@SOPS) {
    	$QSOP=$SOP->[0];
    	$ASOP=$SOP->[1];
    	$QOPR=$SOP->[2];
    	if ($QOP =~ m/[+-]/) {
	    $QOF= "";
	} else {$QOF= $SOP->[3];}
    	print "r $QOP= $QSOP:>r=int32:<r=int32:$QOPR:asm/$AOP >r,<r,$ASOP:\n";
    	print "r = t $QOP $QSOP:>r=int32:<t=int32:$QOPR:asm/$AOP >r,<t,$ASOP:\n";
    	print "r $QOP= $QSOP !:>r=int32:<r=int32:$QOPR:asm/${AOP}s >r,<r,$ASOP:$OF:$QOF\n";
    	print "r = t $QOP $QSOP !:>r=int32:<t=int32:$QOPR:asm/${AOP}s >r,<t,$ASOP:$OF:$QOF\n";	
    	for $i (@CONDS) {
    	    $QCOND= $i->[0];
    	    $ACOND= $i->[1];
    	    ($QFLAG = $QCOND) =~ s/!//;
    	
    	    print "r = t $QOP $QSOP if $QCOND:<r=int32:<t=int32:$QOPR:<?$QFLAG:asm/$AOP$ACOND <r,<t,$ASOP:\n";
    	    print "r $QOP= $QSOP if $QCOND:inplace>r=int32:<r=int32:$QOPR:<?$QFLAG:asm/$AOP$ACOND <r,<r,$ASOP:\n";  	
    	    print "r = t $QOP $QSOP if $QCOND !:<r=int32:<t=int32:$QOPR:<?$QFLAG:asm/${AOP}s${ACOND} <r,<t,$ASOP:$OF:$QOF\n";
    	    print "r $QOP= $QSOP if $QCOND !:inplace>r=int32:<r=int32:$QOPR:<?$QFLAG:asm/${AOP}s${ACOND} <r,<r,$ASOP:$OF:$QOF\n";  
    	}
    }
}

# BIC

for my $SOP (@SOPS) {
    $QSOP=$SOP->[0];
    $ASOP=$SOP->[1];
    $QOPR=$SOP->[2];
    $QOF= $SOP->[3];

    for my $S (@SS) {
	if ($S) {
	    $OF=">?negative:>?=:$QOF"; $NF=" !";
	}   else { $OF=$NF="";}
	print "r = t & ~$QSOP$NF:>r=int32:<t=int32:$QOPR:asm/bic$S >r,<t,$ASOP:$OF\n";
	print "r &= ~$QSOP$NF:>r=int32:<r=int32:$QOPR:asm/bic$S >r,<r,$ASOP:$OF\n";

    	for my $i (@CONDS) {
    	    $QCOND= $i->[0];
    	    $ACOND= $i->[1];
    	    ($QFLAG = $QCOND) =~ s/!//;
	    print "r = t & ~$QSOP if $QCOND$NF:inplace>r=int32:<r=int32:<t=int32:$QOPR:<?$QFLAG:asm/bic$S$ACOND <r,<t,$ASOP:$OF\n";
	    print "r &= ~$QSOP if $QCOND$NF:inplace>r=int32:<r=int32:<r=int32:$QOPR:<?$QFLAG:asm/bic$S$ACOND <r,<r,$ASOP:$OF\n";
	}
    }
}

# RSB
for my $SOP (@SOPS) {
    $QSOP=$SOP->[0];
    $ASOP=$SOP->[1];
    $QOPR=$SOP->[2];
    $QOF= $SOP->[3];

    for my $S (@SS) {
	if ($S) {
	    $OF=">?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?=:>?carry:"; $NF=" !";
	}   else { $OF=$NF="";}
	print "r = - t + $QSOP$NF:>r=int32:<t=int32:$QOPR:asm/rsb$S >r,<t,$ASOP:$OF\n";

    	for my $i (@CONDS) {
    	    $QCOND= $i->[0];
    	    $ACOND= $i->[1];
    	    ($QFLAG = $QCOND) =~ s/!//;

	    print "r = - t + $QSOP if $QCOND$NF:inplace>r=int32:<r=int32:<t=int32:$QOPR:<?$QFLAG:asm/rsb$S$ACOND <r,<t,$ASOP:$OF\n"; 
	}
    }
}

for $OP (@AOCS) {
    $QOP = $OP->[0];
    for my $S (@SS) {
	if ($S) {
	    $OF=">?unsigned>:>?unsigned<:>?signed>:>?signed<:>?negative:>?overflow:>?=:>?carry:<?carry:"; $NF=" !";
	}   else { $OF="<?carry:"; $NF="";}
    
	$AOP = $OP->[1].$S;

	for my $SOP (@SOPS) {
	    $QSOP=$SOP->[0];
	    $ASOP=$SOP->[1];
	    $QOPR=$SOP->[2];
	    $QOF= $SOP->[3];

	    print "r $QOP= $QSOP $QOP carry$NF:>r=int32:<r=int32:$QOPR:asm/$AOP >r,<r,$ASOP:$OF\n";
	    print "r = t $QOP $QSOP $QOP carry$NF:>r=int32:<t=int32:$QOPR:asm/$AOP >r,<t,$ASOP:$OF\n";
	    
	    for my $i (@CONDS) {
		$QCOND= $i->[0];
		$ACOND= $i->[1];
		($QFLAG = $QCOND) =~ s/!//;
		print "r $QOP= $QSOP $QOP carry if $QCOND$NF:inplace>r=int32:<r=int32:<r=int32:$QOPR:asm/$AOP$ACOND <r,<r,$ASOP:<?$QFLAG:$OF\n";
		print "r = t $QOP $QSOP $QOP carry if $QCOND$NF:inplace>r=int32:<r=int32:<t=int32:$QOPR:asm/$AOP$ACOND <r,<r,$ASOP:<?$QFLAG:$OF\n";
	    }
	}
    }
}

for $TST (@TSTS) {
    $QTST = $TST->[0];
    $ATST = $TST->[1];
    $OF = $TST->[2];
    
    for my $SOP (@SOPS) {
	$QSOP=$SOP->[0];
	$ASOP=$SOP->[1];
	$QOPR=$SOP->[2];
	if ($QTST =~ m/[+-]/) {
	    $QOF= "";
	} else {$QOF= $SOP->[3];}
	print "r $QTST $QSOP:<r=int32:$QOPR:asm/$ATST <r,$ASOP:$OF:$QOF\n";

	for my $i (@CONDS) {
	    $QCOND= $i->[0];
	    $ACOND= $i->[1];
	    ($QFLAG = $QCOND) =~ s/!//;

	    print "r $QTST $QSOP if $QCOND:<r=int32:$QOPR:asm/$ATST$ACOND <r,$ASOP:<?$QFLAG:$OF:$QOF\n";

	}   
    }
}

# MUL MLA UMULL UMLAL SMULL SMLAL no flags version (clearly better) only
print "r *= s:inplace>r=int32:<r=int32:<s=int32:asm/mul >r,<s,<r:\n";
print "r = s * t:>r=int32:<s=int32:<t=int32:asm/mul >r,<s,<t:\n";
print "r = s * t + u:>r=int32:<s=int32:<t=int32:<u=int32:asm/mla >r,<s,<t,<u:\n";
print "r += s * t:inplace>r=int32:<r=int32:<s=int32:<t=int32:asm/mla >r,<s,<t,<r:\n";
print "unsigned r s = t * u:>r=int32:>s=int32:<t=int32:<u=int32:asm/umull >s,>r,<t,<u:\n";
print "unsigned r s += t * u:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umlal <s,<r,<t,<u:\n";
print "unsigned r s = t * u + r + s:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umaal <s,<r,<t,<u:\n";
print "signed r s = t * u:>r=int32:>s=int32:<t=int32:<u=int32:asm/smull >s,>r,<t,<u:\n";
print "signed r s += t * u:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/smlal <s,<r,<t,<u:\n";
for my $i (@CONDS) {
    $QCOND= $i->[0];
    $ACOND= $i->[1];
    ($QFLAG = $QCOND) =~ s/!//;
    
    print "r *= s if $QCOND:inplace>r=int32:<r=int32:<r=int32:<s=int32:asm/mul$ACOND <r,<s,<r:<$QFLAG:\n";
    print "r = s * t if $QCOND:inplace>r=int32:<r=int32:<s=int32:<t=int32:asm/mul$ACOND <r,<s,<t:<$QFLAG:\n";
    print "r = s * t + u if $QCOND:inplace>r=int32:<r=int32:<s=int32:<t=int32:<u=int32:asm/mla$ACOND <r,<s,<t,<u:<$QFLAG:\n";
    print "unsigned r s = t * u if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umull$ACOND <s,<r,<t,<u:<$QFLAG:\n";
    print "unsigned r s += t * u if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umlal$ACOND <s,<r,<t,<u:<$QFLAG:\n";
    print "unsigned r s = t * u + r + s if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/umaal$ACOND <s,<r,<t,<u:<$QFLAG:\n";
    print "signed r s = t * u if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/smull$ACOND <s,<r,<t,<u:<$QFLAG:\n";
    print "signed r s += t * u if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:<t=int32:<u=int32:asm/smlal$ACOND <s,<r,<t,<u:<$QFLAG:\n"; 
}

@LDTYPE = (["","",32],["signed ","sb","8"],["unsigned ","b","8"],
	   ["signed ","sh","16"],["unsigned ","h","16"]);

for my $i (@LDTYPE) {
    $LDSGN = $i->[0];
    $LDSUF = $i->[1];
    $LDLEN = $i->[2];

    print "r = ${LDSGN}mem${LDLEN}[s]:>r=int32:<s=int32:asm/ldr$LDSUF >r,[<s]:\n";
    print "r = ${LDSGN}mem${LDLEN}[s + n]:>r=int32:<s=int32:#n:asm/ldr$LDSUF >r,[<s,\$#n]:\n";
    print "r = ${LDSGN}mem${LDLEN}[s - n]:>r=int32:<s=int32:#n:asm/ldr$LDSUF >r,[<s,\$-#n]:\n";
    print "r = ${LDSGN}mem${LDLEN}[s]; s += n:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF >r,[<s],\$#n:\n";
    print "r = ${LDSGN}mem${LDLEN}[s]; s -= n:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF >r,[<s],\$-#n:\n";
    print "r = ${LDSGN}mem${LDLEN}[s += n]:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF >r,[<s,\$#n]!:\n";
    print "r = ${LDSGN}mem${LDLEN}[s -= n]:>r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF >r,[<s,\$-#n]!:\n";
    print "r = ${LDSGN}mem${LDLEN}[s + t]:>r=int32:<s=int32:<t=int32:asm/ldr$LDSUF >r,[<s,<t]:\n";
    print "r = ${LDSGN}mem${LDLEN}[s + (t << n)]:>r=int32:<s=int32:<t=int32:#n:asm/ldr$LDSUF >r,[<s,<t, LSL \$#n]:\n";
    print "r = ${LDSGN}mem${LDLEN}[s + (t unsigned>> n)]:>r=int32:<s=int32:<t=int32:#n:asm/ldr$LDSUF >r,[<s,<t, LSR \$#n]:\n";

    for my $i (@CONDS) {
	$QCOND= $i->[0];
	$ACOND= $i->[1];
	($QFLAG = $QCOND) =~ s/!//;

	print "r = ${LDSGN}mem${LDLEN}[s] if $QCOND:inplace>r=int32:<r=int32:<s=int32:asm/ldr$LDSUF$ACOND <r,[<s]:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s + n] if $QCOND:inplace>r=int32:<r=int32:<s=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s,\$#n]:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s - n] if $QCOND:inplace>r=int32:<r=int32:<s=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s,\$-#n]:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s]; s += n if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s],\$#n:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s]; s -= n if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s],\$-#n:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s += n] if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s,\$#n]!:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s -= n] if $QCOND:inplace>r=int32:<r=int32:inplace>s=int32:<s=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s,\$-#n]!:<?$QFLAG:\n";
	print "r = ${LDSGN}mem${LDLEN}[s + (t << n)] if $QCOND:inplace>r=int32:<r=int32:<s=int32:<t=int32:#n:asm/ldr$LDSUF$ACOND <r,[<s,<t, LSL \$#n]:<?$QFLAG:\n";
    }
}

@STTYPE = (["",32],["b",8],["h",16]);    

for my $i (@STTYPE) {
    $STSUF = $i->[0];
    $STLEN = $i->[1];

    print "mem${STLEN}[s] = r:<r=int32:<s=int32:asm/str$STSUF <r,[<s]:\n";
    print "mem${STLEN}[s + n] = r:<r=int32:<s=int32:#n:asm/str$STSUF <r,[<s,\$#n]:\n";
    print "mem${STLEN}[s - n] = r:<r=int32:<s=int32:#n:asm/str$STSUF <r,[<s,\$-#n]:\n";
    print "mem${STLEN}[s] = r; s += n:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF <r,[<s],\$#n:\n";
    print "mem${STLEN}[s] = r; s -= n:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF <r,[<s],\$-#n:\n";
    print "mem${STLEN}[s += n] = r:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF <r,[<s,\$#n]!:\n";
    print "mem${STLEN}[s -= n] = r:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF <r,[<s,\$-#n]!:\n";
    print "mem${STLEN}[s + (t << n)] = r:<r=int32:<s=int32:<t=int32:#n:asm/str$STSUF <r,[<s,<t, LSL \$#n]:\n";

    for my $i (@CONDS) {
	$QCOND= $i->[0];
	$ACOND= $i->[1];
	($QFLAG = $QCOND) =~ s/!//;

	print "mem${STLEN}[s] = r if $QCOND:<r=int32:<s=int32:asm/str$STSUF$ACOND <r,[<s]:<?$QFLAG:\n";
	print "mem${STLEN}[s + n] = r if $QCOND:<r=int32:<s=int32:#n:asm/str$STSUF$ACOND <r,[<s,\$#n]:<?$QFLAG:\n";
	print "mem${STLEN}[s - n] = r if $QCOND:<r=int32:<s=int32:#n:asm/str$STSUF$ACOND <r,[<s,\$-#n]:<?$QFLAG:\n";
	print "mem${STLEN}[s] = r; s += n if $QCOND:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF$ACOND <r,[<s],\$#n:<?$QFLAG:\n";
	print "mem${STLEN}[s] = r; s -= n if $QCOND:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF$ACOND <r,[<s],\$-#n:<?$QFLAG:\n";
	print "mem${STLEN}[s += n] = r if $QCOND:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF$ACOND <r,[<s,\$#n]!:<?$QFLAG:\n";
	print "mem${STLEN}[s -= n] = r if $QCOND:<r=int32:inplace>s=int32:<s=int32:#n:asm/str$STSUF$ACOND <r,[<s,\$-#n]!:<?$QFLAG:\n";
	print "mem${STLEN}[s + (t << n)] = r if $QCOND:<r=int32:<s=int32:<t=int32:#n:asm/str$STSUF$ACOND <r,[<s,<t, LSL \$#n]:<?$QFLAG:\n";
    }
}


print "assign r0 to r:<r=int32#1:\n";
print "assign r1 to r:<r=int32#2:\n";
print "assign r2 to r:<r=int32#3:\n";
print "assign r3 to r:<r=int32#4:\n";
print "assign r4 to r:<r=int32#5:\n";
print "assign r5 to r:<r=int32#6:\n";
print "assign r6 to r:<r=int32#7:\n";
print "assign r7 to r:<r=int32#8:\n";
print "assign r8 to r:<r=int32#9:\n";
print "assign r9 to r:<r=int32#10:\n";
print "assign r10 to r:<r=int32#11:\n";
print "assign r11 to r:<r=int32#12:\n";
print "assign r12 to r:<r=int32#13:\n";
print "assign r14 to r:<r=int32#14:\n";

print "r = s:>r=int32:<s=stack32:asm/ldr >r,<s:\n";
print "s = r:<r=int32:>s=stack32:asm/str <r,>s:\n";
for $i (@CONDS) {
    $QCOND= $i->[0];
    $ACOND= $i->[1];
    ($QFLAG = $QCOND) =~ s/!//;
    print "r = s if $QCOND:inplace>r=int32:<r=int32:<s=stack32:<?$QFLAG:asm/ldr$ACOND <r,<s:\n";
    print "s = r if $QCOND:<r=int32:inplace>s=stack32:<s=stack32:<?$QFLAG:asm/ldr$ACOND <r,<s:\n";
}

# BFI BFC SBFX UBFX

print "r = s signed n bits from pos m:>r=int32:<s=int32:#n:#m:asm/sbfx >r,<s,\$#m,\$#n:\n";
print "r = s unsigned n bits from pos m:>r=int32:<s=int32:#n:#m:asm/ubfx >r,<s,\$#m,\$#n:\n";
print "r = (s << (32 - m - n)) unsigned>> (32 - m):>r=int32:<s=int32:#n:#m:asm/sbfx >r,<s,\$#m,\$#n:\n";
print "r = (s << (32 - m - n)) unsigned>> (32 - m):>r=int32:<s=int32:#n:#m:asm/ubfx >r,<s,\$#m,\$#n:\n";
print "r insert right n bits in s from pos m:>r=int32:<s=int32:#n:#m:asm/bfi >r,<s,\$#m,\$#n:\n";

@PAIRS = (["r0 r1",1,2], ["r2 r3",3,4], ["r4 r5",5,6], ["r6 r7",7,8],
	  ["r8 r9",9,10], ["r10 r11",11,12]);

for $i (@PAIRS) {
    print "assign $i->[0] to r s;mem64[t + n] = r s:<r=int32#$i->[1]:<s=int32#$i->[2]:<t=int32:#n:asm/strd <r,[<t,\$#n]:\n";
    print "assign $i->[0] to r s;mem64[t] = r s;t += n:<r=int32#$i->[1]:<s=int32#$i->[2]:<t=int32:#n:asm/strd <r,[<t],\$#n:\n";    
    print "assign $i->[0] to r s;mem64[t + u] = r s:<r=int32#$i->[1]:<s=int32#$i->[2]:<t=int32:<u=int32:asm/strd <r,[<t,<u]:\n";
    print "assign $i->[0] to r s;t = r s:<r=int32#$i->[1]:<s=int32#$i->[2]:>t=stack64:#n:asm/strd <r,>t:\n";
    print "assign $i->[0] to r s;mem64[&t] = r s:<r=int32#$i->[1]:<s=int32#$i->[2]:>t=stack32:#n:asm/strd <r,>t:\n";
    print "assign $i->[0] to r s = mem64[t + n]:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=int32:#n:asm/ldrd >r,[<t,\$#n]:\n";
    print "assign $i->[0] to r s = mem64[t]; t += n:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=int32:#n:asm/ldrd >r,[<t],\$#n:\n";
    print "assign $i->[0] to r s = mem64[t + u]:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=int32:<u=int32:asm/ldrd >r,[<t,<u]:\n";
    print "assign $i->[0] to r s = t:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=stack64:#n:asm/ldrd >r,<t:\n";    
    print "assign $i->[0] to r s = mem64[&t]:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=stack32:#n:asm/ldrd >r,<t:\n";    
    for my $j (@CONDS) {
    	$QCOND= $j->[0];
    	$ACOND= $j->[1];
    	($QFLAG = $QCOND) =~ s/!//;
        print "assign $i->[0] to r s;mem64[t + n] = r s if $QCOND:<r=int32#$i->[1]:<s=int32#$i->[2]:<t=int32:#n:<?$QFLAG:asm/strd$ACOND <r,[<t,\$#n]:\n";
        print "assign $i->[0] to r s;mem64[t] = r s;t += n if $QCOND:<r=int32#$i->[1]:<s=int32#$i->[2]:<t=int32:#n:<?$QFLAG:asm/strd$ACOND <r,[<t],\$#n:\n";    
        print "assign $i->[0] to r s;mem64[t + u] = r s if $QCOND:<r=int32#$i->[1]:<s=int32#$i->[2]:<t=int32:<u=int32:<?$QFLAG:asm/strd$ACOND <r,[<t,<u]:\n";
        print "assign $i->[0] to r s;t = r s if $QCOND:<r=int32#$i->[1]:<s=int32#$i->[2]:>t=stack64:#n:<?$QFLAG:asm/strd$ACOND <r,>t:\n";
        print "assign $i->[0] to r s = mem64[t + n] if $QCOND:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=int32:#n:<?$QFLAG:asm/ldrd$ACOND >r,[<t,\$#n]:\n";
        print "assign $i->[0] to r s = mem64[t]; t += n if $QCOND:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=int32:#n:<?$QFLAG:asm/ldrd$ACOND >r,[<t],\$#n:\n";
        print "assign $i->[0] to r s = mem64[t + u] if $QCOND:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=int32:<u=int32:<?$QFLAG:asm/ldrd$ACOND >r,[<t,<u]:\n";
        print "assign $i->[0] to r s = t if $QCOND:>r=int32#$i->[1]:>s=int32#$i->[2]:<t=stack64:#n:<?$QFLAG:asm/ldrd$ACOND >r,<t:\n";    
    }
}

for ($i=3;$i<15;$i++) {
  for ($j=2;$j<$i;$j++) {
    for ($k=1;$k<$j;$k++) {
      print "r s t = mem96[a]:>r=int32#$k:>s=int32#$j:>t=int32#$i:<a=int32:asm/ldm <a,{>r,>s,>t}:\n";
      print "r s t = mem96[a];a+=12:>r=int32#$k:>s=int32#$j:>t=int32#$i:inplace>a=int32:<a=int32:asm/ldm <a!,{>r,>s,>t}:\n";
      print "mem96[a] = r s t:<r=int32#$k:<s=int32#$j:<t=int32#$i:<a=int32:asm/stm <a,{<r,<s,<t}:\n";
      print "mem96[a] = r s t;a+=12:<r=int32#$k:<s=int32#$j:<t=int32#$i:inplace>a=int32:<a=int32:asm/stm <a!,{<r,<s,<t}:\n";
      print "r s t = mem96[a-12]:>r=int32#$k:>s=int32#$j:>t=int32#$i:<a=int32:asm/ldmdb <a,{>r,>s,>t}:\n";
      print "r s t = mem96[a-=12]:>r=int32#$k:>s=int32#$j:>t=int32#$i:inplace>a=int32:<a=int32:asm/ldmdb <a!,{>r,>s,>t}:\n";
      print "mem96[a-12] = r s t:<r=int32#$k:<s=int32#$j:<t=int32#$i:<a=int32:asm/stmdb <a,{<r,<s,<t}:\n";
      print "mem96[a-=12] = r s t:<r=int32#$k:<s=int32#$j:<t=int32#$i:inplace>a=int32:<a=int32:asm/stmdb <a!,{<r,<s,<t}:\n";
    }
  }
}

for ($i=4;$i<15;$i++) {
  for ($j=3;$j<$i;$j++) {
    for ($k=2;$k<$j;$k++) {
      for ($l=1;$l<$k;$l++) {
        print "r s t u = mem128[a]:>r=int32#$l:>s=int32#$k:>t=int32#$j:>u=int32#$i:<a=int32:asm/ldm <a,{>r,>s,>t,>u}:\n";
        print "r s t u = mem128[a];a+=16:>r=int32#$l:>s=int32#$k:>t=int32#$j:>u=int32#$i:inplace>a=int32:<a=int32:asm/ldm <a!,{>r,>s,>t,>u}:\n";
        print "mem128[a] = r s t u:<r=int32#$l:<s=int32#$k:<t=int32#$j:<u=int32#$i:<a=int32:asm/stm <a,{<r,<s,<t,<u}:\n";
        print "mem128[a] = r s t u;a+=16:<r=int32#$l:<s=int32#$k:<t=int32#$j:<u=int32#$i:inplace>a=int32:<a=int32:asm/stm <a!,{<r,<s,<t,<u}:\n";
        print "r s t u = mem128[a-16]:>r=int32#$l:>s=int32#$k:>t=int32#$j:>u=int32#$i:<a=int32:asm/ldmdb <a,{>r,>s,>t,>u}:\n";
        print "r s t u = mem128[a-=16]:>r=int32#$l:>s=int32#$k:>t=int32#$j:>u=int32#$i:inplace>a=int32:<a=int32:asm/ldmdb <a!,{>r,>s,>t,>u}:\n";
        print "mem128[a-16] = r s t u:<r=int32#$l:<s=int32#$k:<t=int32#$j:<u=int32#$i:<a=int32:asm/stmdb <a,{<r,<s,<t,<u}:\n";
        print "mem128[a-=16] = r s t u:<r=int32#$l:<s=int32#$k:<t=int32#$j:<u=int32#$i:inplace>a=int32:<a=int32:asm/stmdb <a!,{<r,<s,<t,<u}:\n";
      }
    }
  }
}

