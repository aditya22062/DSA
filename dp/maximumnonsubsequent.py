n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
inc=a[0]
exc=0
for i in range(1,len(a)):
    temp=inc
    inc=exc+a[i]
    exc=max(temp,exc)
print(max(inc,exc))
