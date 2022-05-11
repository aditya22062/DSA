n=int(input())
#on k liye we use OR
#off k liye we use AND
#toggle k liye we use XOR
#check k liye we use AND
i=int(input())
j=int(input())
k=int(input())
m=int(input())
onmask=(1<<i)
offmask=~(1<<j)
togglemask=(1<<k)
checkmask=(1<<m)

print(n|onmask)
print(n&offmask)
print(n^togglemask)
print(n&checkmask)
