def mergeOverlappingIntervals(arr):
    
    # write your code here
    arr=sorted(arr)
    st=[]
    st.append(arr[0])
    for start,end in arr[1:]:
        if start<=st[-1][1]:
            st[-1][1]=max(end,st[-1][1])
        else:
            st.append([start,end])
    
    for i in range(len(st)-1,-1,-1):
        print(*st[i])    



def main():
    n = int(input())
    arr = [ ]
    
    
    # input from user
    for i in range(n):
        narr = []
        inp = str(input()).strip().split(" ")
        narr.append(int(inp[0]))
        narr.append(int(inp[1]))
        arr.append(narr)
    
    
    mergeOverlappingIntervals(arr)



main()