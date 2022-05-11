import sys
import math
  
class Node:
    def __init__(self, val,left,right):
        self.left = left
        self.right = right
        self.val = val



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
     

def size(node):
    if node==None:
        return 0
    lh=size(node.left)
    rh=size(node.right)
    th=lh+rh+1
    return th
        
def sumV(node):
    if node==None:
        return 0
    ls=sumV(node.left)
    rs=sumV(node.right)
    ts=ls+rs+node.val
    return ts
  

def maxV(root):
    if root.right!=None:
        return maxV(root.right)
    else:
        return root.val
    
def minV(root):
    if root.left!=None:
        return minV(root.left)
    else:
        return root.val
#     Write your code here
        
        
def find(node,data):
    if node==None:
        return False
    if data>node.val:
        return find(node.right,data)
    elif data<node.val:
        return find(node.left,data)
    else:
        return True
    
    

n=int(input())
values = list(map(str, input().split()))
arr=[0]*n
for i in range(0,n):
    if values[i]!="n":
        arr[i]=int(values[i])
    else:
        arr[i]=None
val=int(input())

root=construct(arr)

print(size(root))
print(sumV(root))
print(maxV(root))
print(minV(root))
print(find(root, val));