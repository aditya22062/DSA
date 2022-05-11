l=2
ar=[1,2,3,5,2]
ans=[]
for i in range(len(ar)):
    if ar[i]==l:
        ans.append(i)
print(ans[0],ans[-1])