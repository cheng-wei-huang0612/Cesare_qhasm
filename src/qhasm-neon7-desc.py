#!/usr/bin/python3

PART  = [["","",1], ["[0]","%bot",2], ["[1]","%top",2]]

PART2 = [["","","","",1],
         ["[0]","[0]","%bot","%bot",2], ["[0]","[1]","%bot","%top",2],
         ["[1]","[0]","%top","%bot",2], ["[1]","[1]","%top","%top",2]]

PART3 = [["","","","","","",1],
         ["[0]","[0]","[0]","%bot","%bot","%bot",2],
         ["[0]","[0]","[1]","%bot","%bot","%top",2],
         ["[0]","[1]","[0]","%bot","%top","%bot",2],
         ["[0]","[1]","[1]","%bot","%top","%top",2],
         ["[1]","[0]","[0]","%top","%bot","%bot",2],
         ["[1]","[0]","[1]","%top","%bot","%top",2],
         ["[1]","[1]","[0]","%top","%top","%bot",2],
         ["[1]","[1]","[1]","%top","%top","%top",2]]

LOP = [["^","eor","^="], ["|","orr","|="], ["| ~","orn","|= ~"],
       ["&","and","&="], ["& ~","bic","&= ~"]]


LMOP = [["=","mull",">r=reg128",">r"],
        ["+=","mlal","inplace>r=reg128:<r=reg128","<r"],
        ["-=","mlsl","inplace>r=reg128:<r=reg128","<r"],
        ["= 2* SAT","qdmull",">r=reg128",">r"],
        ["+= 2* SAT","qdmlal","inplace>r=reg128:<r=reg128","<r"],
        ["-= 2* SAT","qdmlsl","inplace>r=reg128:<r=reg128","<r"]]

MOP = [["=", "mul",">r=reg128",">r"],
       ["= 2* SAT HIGH","qdmulh",">r=reg128",">r"],
       ["= 2* SAT ROUND HIGH","qrdmulh",">r=reg128",">r"],
       ["+=","mla","inplace>r=reg128:<r=reg128","<r"],
       ["-=","mls","inplace>r=reg128:<r=reg128","<r"],
       #["= 2* SAT HIGH","qdmlah","inplace>r=reg128:<r=reg128",">r"],
       #["= 2* SAT ROUND HIGH","qrdmlah","inplace>r=reg128:<r=reg128",">r"] 
       ]


AOP = [["+","add"], ["-","sub"]]

SIZEM = [["u8",8,"unsigned"],["s8",8,"signed"],
         ["u16",16,"unsigned"],["u32",32,"unsigned"],
         ["s16",16,"signed"],["s32",32,"signed"],
         ["i16",16,""],["i32",32,""],["i8",8,""]]
# SIZEM[2:8] does the short muladds
# SIZEM[2:6] does the long muladds
# SIZEM[4:6] does the q(r)dmulh and q(r)dmull


SIZEMP = [["p8",8,"poly"], ["p16",16,"poly"], ["f32",32,"float"]]



SIZEA1 = [["u8",8,"unsigned"],["s8",8,"signed"],
          ["u16",16,"unsigned"],["s16",16,"signed"],
          ["u32",32,"unsigned"],["s32",32,"signed"],
          ["u64",64,"unsigned"],["s64",64,"signed"]]
# SIZEA1[2:] does the Widening
# SIZEA1[:6] does the Long

SIZEA = [["i8",8], ["i16",16], ["i32",32], ["i64",64]]


for i in LOP :
    for j in PART3 :
        print("r%s = s%s %s t%s:>r=reg128:<s=reg128:<t=reg128:asm/v%s >r%s,<s%s,<t%s:" % (j[0],j[1],i[0],j[2],i[1],j[3],j[4],j[5]))
    for j in PART2 :
        print("r%s %s s%s:inplace>r=reg128:<r=reg128:<s=reg128:asm/v%s <r%s,<r%s,<s%s:" % (j[0],i[2],j[1],i[1],j[2],j[2],j[3]))


for i in AOP :  # add, sub
    for j in SIZEA : # plain
        for k in PART3 :
            print("%dx r%s = s%s %s t%s:>r=reg128:<s=reg128:<t=reg128:asm/v%s.%s >r%s,<s%s,<t%s:" % ((128/(k[6]*j[1])),k[0],k[1],i[0],k[2],i[1],j[0],k[3],k[4],k[5]))
        for k in PART2 :
             print("%dx r%s %s= s%s:>r=reg128:<s=reg128:<t=reg128:asm/v%s.%s >r%s,<s%s,<t%s:" % ((64/(k[4]*j[1])),k[0],i[0],k[1],i[1],j[0],k[2],k[2],k[3]))       

    for j in SIZEA1 : # saturated
        for k in PART3 :
            print("%dx r%s = SAT s%s %s%s t%s:>r=reg128:<s=reg128:<t=reg128:asm/vq%s.%s >r%s,<s%s,<t%s:" % ((128/(k[6]*j[1])),k[0],k[1],j[2],i[0],k[2],i[1],j[0],k[3],k[4],k[5]))
        for k in PART2 :
             print("%dx r%s %s%s= SAT s%s:>r=reg128:<s=reg128:<t=reg128:asm/vq%s.%s >r%s,<s%s,<t%s:" % ((64/(k[4]*j[1])),k[0],j[2],i[0],k[1],i[1],j[0],k[2],k[2],k[3]))       
        
    for j in SIZEA1[2:] : # addw, subw
        for k in PART[1:] : 
            print("%dx r = s %s%s t%s:>r=reg128:<s=reg128:<t=reg128:asm/v%sw.%s >r,<s,<t%s:" % (128/j[1],j[2],i[0],k[0],i[1],j[0],k[1]))
            print("%dx r %s%s= s%s:inplace>r=reg128:<r=reg128:<s=reg128:asm/v%sw.%s <r,<r,<s%s:" % (128/j[1],j[2],i[0],k[0],i[1],j[0],k[1]))

    for j in SIZEA1[:6] : # addl, subl
        for k in PART2[1:] : 
            print("%dx r = s%s %s%s t%s:>r=reg128:<s=reg128:<t=reg128:asm/v%sl.%s >r,<s%s,<t%s:" % (64/j[1],k[0],j[2],i[0],k[1],i[1],j[0],k[2],k[3]))


for i in LMOP : # mull, mlal, other double-length mults
    if i[1] == "mull" : S = SIZEM[:6] + SIZEMP[:2]; S2 = SIZEM[2:6] + SIZEMP[:2]
    else : S = SIZEM[2:6]; S2 = SIZEM[2:6]

    for j in S :
        for k in PART2[1:] :
            print("%dx r %s s%s %s* t%s:%s:<s=reg128:<t=reg128:asm/v%s.%s %s,<s%s,<t%s:" % (128/(k[4]*j[1]),i[0],k[0],j[2],k[1],i[2],i[1],j[0],i[3],k[2],k[3]))
    
    for j in S2 :
        for k in PART2[1:] :
            x = "1"
            for l in range(1,j[1]//4) : x+= (","+str(1+l))
            print("%dx r %s s%s %s* t%s[n]:%s:<s=reg128:<t=reg128#%s:#n:asm/v%s.%s %s,<s%s,<t%s[#n]:" % (128/(k[4]*j[1]),i[0],k[0],j[2],k[1],i[2],x,i[1],j[0],i[3],k[2],k[3]))

for i in MOP : # mul, mla, other same-size mults
    if i[1] == "mul" : S = SIZEM + SIZEMP; S2 = SIZEM[2:] + SIZEMP
    else : S = SIZEM; S2 = SIZEM[2:]
    
    for j in S :
        for k in PART3 :
            print("%dx r%s %s s%s %s* t%s:%s:<s=reg128:<t=reg128:asm/v%s.%s %s%s,<s%s,<t%s:" % (128/(j[1]*k[6]),k[0],i[0],k[1],j[2],k[2],i[2],i[1],j[0],i[3],k[3],k[4],k[5]))

    for j in S2 :
        for k in PART2 :
            x = "1"
            for l in range(1,j[1]//4) : x+= (","+str(1+l))
            for m in PART[1:] :
                print("%dx r%s %s s%s %s* t%s[n]:%s:<s=reg128:<t=reg128#%s:#n:asm/v%s.%s %s%s,<s%s,<t%s[#n]:" % (128/(j[1]*k[4]),k[0],i[0],k[1],j[2],m[0],i[2],x,i[1],j[0],i[3],k[2],k[3],m[1]))
