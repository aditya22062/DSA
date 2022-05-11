def printsubsequence(s,idx,ssf):
    if idx==len(s):
        print(ssf)
        return

    printsubsequence(s,idx+1,ssf+s[idx])
    printsubsequence(s,idx+1,ssf)
s=input()
printsubsequence(s,0,"")