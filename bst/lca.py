import sys
import math

class Node:
    def __init__(self, key,left,right):
        self.left = left
        self.right = right
        self.val = key
        
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
    while(len(st)>0):
        top=st[-1];
        if top.state==1:
            idx+=1
            if(arr[idx]!=None):
                top.node.left = Node(arr[idx], None, None);
                lp = Pair(top.node.left, 1);
                st.append(lp);
            else:
                top.node.left=None;
            top.state+=1
        elif top.state==2:
            idx+=1
            if(arr[idx]!=None):
                top.node.right =  Node(arr[idx], None, None);
                rp =  Pair(top.node.right, 1);
                st.append(rp);
            else:
                top.node.right=None;
            top.state+=1
        else:
            st.pop();
    return root; 
     
def lca(root, n1, n2):
    if n1>root.val and n2>root.val:
        return lca(root.right,n1,n2)
    elif n2<root.val and n2<root.val:
        return lca(root.left,n1,n2)
    else:
        return root.data
 

n=int(input())
values = list(map(str, input().split()))
arr=[0]*n
for i in range(0,n):
    if values[i]!="n":
        arr[i]=int(values[i])
    else:
        arr[i]=None
        
n1=int(input())
n2=int(input())

root=construct(arr)
ans = root.val
lca(root, n1, n2)
print(ans)
