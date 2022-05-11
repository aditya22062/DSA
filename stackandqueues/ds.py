

heights=list(map(int,input().split()))
nsl=[0]*(len(heights))
st=[]
st.append(-1)
nsl[0]=-1
for i in range(1,len(heights)):
    while len(st)>0 and heights[i]<heights[st[-1]]:
        st.pop()
    if len(st)==0:
        nsl[i]=-1
    else:
        nsl[i]=st[-1]
    st.append(i)
    
nsr=[0]*(len(heights))
st1=[]
st1.append(len(heights)-1)
nsr[len(heights)-1]=len(heights)
for i in range(len(heights)-2,-1,-1):
    while len(st1)>0 and heights[i]<heights[st1[-1]]:
        st1.pop()
    if len(st)==0:
        nsr[i]=len(heights)
    else:
        nsr[i]=st1[-1]
    st1.append(i)
area=0
for i in range(len(heights)):
    area=max(area,abs(nsl[i]-nsr[i]-1)*heights[i])
print(area)