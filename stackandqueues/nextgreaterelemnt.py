from sys import stdin
def display(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = "\n")
def solve(arr2):
    #write your code here
    nge=[0]*len(arr2)
    st=[]
    st.append(arr2[-1])
    nge[len(arr2)-1]=-1
    for i in range(len(arr2)-2,-1,-1):
        while len(st)>0 and arr2[i]>=st[-1]:
            st.pop()
        if len(st)==0:
            nge[i]=-1
        else:
            nge[i]=st[-1]
        
        st.append(arr2[i])
    return nge

n = int(input())
arr =[]
for i in range (n):
    x = int(input())
    arr.append(x)

nge = solve(arr)
display(nge)