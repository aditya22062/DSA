s = input()
codes=[".;","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"]
def getKPC(s):
    #Write your code here
    if len(s)==0:
        bres=[]
        bres.append("")
        return bres
    s0=s[0]
    ros=s[1:]
    ares=[]
    stba=getKPC(ros)
    codeforch=codes[int(s0)]
    for i in range(len(codeforch)):
        ch=codeforch[i]
        for rstr in stba:
            ares.append(ch+rstr)
    return ares
    
ans = getKPC(s)

print("["+', '.join(ans) + "]")