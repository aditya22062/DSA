def findCelebrity(arr):
    # write your code here
    st=[]
    for i in range(len(arr)):
        st.append(arr[i])
    while len(st)>=2:
        i=st.pop()
        j=st.pop()
        if arr[i][j]==1:
            st.append(j)
        else:
            st.append(i)
    potential=st.pop()
    for i in range(len(arr)):
        if i !=potential:
            if arr[potential][i]==1 or arr[i][potential]==0:
                print("false")
                return
    print("true")

n=int(input())
arr = [[0 for i in range(n)]for j in range(n)]

for i in range(n):
    line = input().split()
    for j in range(len(line)):
        arr[i][j] = ord(line[j]) - ord('0')


findCelebrity(arr)
  