string = input()

#write your code here
d={}
for i in string:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
maxi=0
for i in d:
    maxi=max(maxi,d[i])
print(maxi)
for i in d:
    if d[i]==maxi:
        print(i)
