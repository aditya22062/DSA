
n = int(input())
arr =[]
for i in range (n):
    x = int(input())
    arr.append(x)
lw=[0]*len(arr)
st=[]
st.append(0)
lw[0]=-1
for i in range(1,len(arr)):
    while len(st)>0 and arr[i]<=arr[st[-1]]:
        st.pop()
    if len(st)==0:
        lw[i]=-1
    else:
        lw[i]=st[-1]
    st.append(i)

rw=[0]*len(arr)
st=[]
st.append(len(arr)-1)
rw[len(arr)-1]=len(arr)
for i in range(len(arr)-2,-1,-1):
    while len(st)>0 and arr[i]<=arr[st[-1]]:
        st.pop()
    if len(st)==0:
        rw[i]=len(arr)
    else:
        rw[i]=st[-1]
    st.append(i)
area=0
for i in range(len(arr)):
    width=rw[i]-lw[i]-1
    area=max(area,arr[i]*width)
print(area)
#write your code here

