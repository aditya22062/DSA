class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = None
        self.right = None
class Pair:
    def __init__(self,node,state):
        self.node = node
        self.state = state

def construct(arr):
    root=Node(arr[0],None,None)
    rtp=Pair(root,1);
    
    st=[]
    st.append(rtp);
    
    idx=0;
    n = len(arr)
    while(len(st)>0):
        top=st[-1];
        if top.state==1:
            idx+=1
            st[-1].state+=1
            if(arr[idx]!=-1):
                top.node.left = Node(arr[idx], None, None);
                lp = Pair(top.node.left, 1);
                st.append(lp);
            else:
                top.node.left=None;
        elif top.state==2:
            idx+=1
            st[-1].state+=1
            if(arr[idx]!=-1):
                top.node.right =  Node(arr[idx], None, None);
                rp =  Pair(top.node.right, 1);
                st.append(rp);
            else:
                top.node.right=None;
        else:
            st.pop()
    return root;


    
def size(node):
    # Write your code here
    if node==None:
        return 0
    ls=size(node.left)
    rs=size(node.right)
    ts=ls+rs+1
    return ts 
def add(node):
    # Write your code here
    if node==None:
        return 0
    la=add(node.left)
    ra=add(node.right)
    ta=la+ra+node.data
    return ta
        
def maximum(node):
    # Write your code here
    if node==None:
        return float('-inf')
    lm=maximum(node.left)
    rm=maximum(node.right)
    tm=max(node.data,lm,rm)
    return tm
def height(node):
    # Write your code here
    if node==None:
        return-1
    lh=height(node.left)
    rh=height(node.right)
    th=max(lh,rh)+1
    return th

n = int(input())
st = input()
arr = list(map(int,st.replace("n","-1").split(" ")))
root = construct(arr)
print(size(root))
print(add(root))
print(maximum(root))
print(height(root))
