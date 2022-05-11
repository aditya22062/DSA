from numpy import array


array=list(map(int,input().split()))
k=int(input())
dicti={}

for i in array:
    if i in dicti:
        dicti[i]+=1
    else:
        dicti[i]=1
listi=[]
st=set(array)
for i in st:
    listi.append([dicti[i],i])


listi=sorted(listi,reverse=True)
print(listi)
res=[]
for i in range(k):
    res.append(listi[i][1])
print(res)