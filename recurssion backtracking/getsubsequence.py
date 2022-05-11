s = input()

def getSS(s):
    #Write your code here
    if len(s)==0:
        bres=[]
        bres.append("")
        return bres
    s0=s[0]
    sres=s[1:]
    rres=getSS(sres)
    mres=[]
    for i in rres:
        mres.append(""+i)
    for i in rres:
        mres.append(s0+i)

    return mres
    
ans = getSS(s)

print("["+', '.join(ans) + "]")