def getnum(s,d):
    sumofs=""
    for i in s:
        sumofs+=str(d[i])
    return int(sumofs)

def solution(s,idx,d,boarr,s1,s2,s3):
    if idx==len(s):
        n1=getnum(s1,d)
        n2=getnum(s2,d)
        n3=getnum(s3,d)
        if n1+n2==n3:
            for i in range(26):
                ch=chr(ord('a')+i)
                if ch in d:
                    print(ch +" "+str(d[ch]),end=" ")
            print()
        return 



    ch=s[idx]
    for i in range(10):
        if boarr[i]==False:
            d[ch]=i
            boarr[i]=True
            solution(s,idx+1,d,boarr,s1,s2,s3)
            boarr[i]=False
            d[ch]=-1






s1=input()
s2=input()
s3=input()

d={}
s=""
for i in s1:
    if i not in d:
        d[i]=-1
        s=s+i
for i in s2:
    if i not in d:
        d[i]=-1
        s=s+i
for i in s3:
    if i not in d:
        d[i]=-1
        s=s+i
boarr=[False]*10
print(solution(s,0,d,boarr,s1,s2,s3))