
inp = str(input())


# write your code here
st=[]
count=1

for i in inp:
    if i=='d':
        st.append(count)
        count+=1
    
    else:
        st.append(count)
        count+=1
        while len(st)!=0:
            print(st.pop())
st.append(count)
arr=[]
for i in range(len(st)):
    a=st.pop()
    arr.append(a)
for i in range(len(arr)):
    print(arr[i],end="")

