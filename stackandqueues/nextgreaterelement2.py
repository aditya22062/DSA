from sys import stdin
def display(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = "\n")
def solve(arr2):
    #write your code here
    nge=[0]*len(arr2)
    st=[]
    st.append(0)
    for i in range(1,len(arr2)):
        while len(st)>0 and arr[i]>arr[st[-1]]:
            pos=st[-1]
            nge[pos]=arr[i]
            st.pop()
        st.append(i)
    while len(st)>0:
        pos=st[-1]
        nge[pos]=-1
        st.pop()
    return nge

n = int(input())
arr =[]
for i in range (n):
    x = int(input())
    arr.append(x)

nge = solve(arr)
display(nge)