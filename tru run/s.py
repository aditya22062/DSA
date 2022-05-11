def generatepw(cs, ts, fmap, oddc, asf):
    if cs>ts:
        rev=asf[-1::-1]
        res=asf
        if oddc != "":
            res=res+oddc
        res=res+rev
        print(res)
        return
    for i in d:

        freq=d[i]
        if freq>0:
            d[i]=freq-1
            generatepw(cs+1,ts,fmap,oddc,asf+i)
            d[i]=freq

str1 = input()
d={}
for i in range(len(str1)):
    ch = str1[i]
    if ch not in d:
        d[ch]=1
    else:
        d[ch]+=1
odds=0
odd=""
lenf=0
for i in d:
    if d[i]%2==1:
        odds+=1
        odd=i
    else:
        d[i]=d[i]//2
        lenf+=d[i]
generatepw(1,lenf,d,odd,"")
