import sys
import math


class Node:
    def __init__(self, data,left,right):
        self.left = left
        self.right = right
        self.data = data
        
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
     
 
def display(node) :
    if (node == None):
        return;
        
    s = " <- " + str(node.data) + " -> ";
    left = "." if node.left is None else ""+str(node.left.data);
    right = "." if node.right is None else "" + str(node.right.data);
    
    s=left + s + right;
    print(s);
    
    display(node.left);
    display(node.right);
 
 
def maxs(node):
    if node.right is None:
        return node.data
        
    return maxs(node.right)
    

def removeNode(root, data):
    if root==None:
        return None
    if data>root.data:
        root.right=removeNode(root.left,data)
    elif data<root.data:
        root.right=removeNode(root.right,data)
    else:
        if root.left!=None and root.right!=None:
            return maxs(root.left)
        elif root.left!=None:
            return root.left
        elif root.right!=None:
            return root.right
        else:
            return None
    return root
 
 
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

root = removeNode(root, val)
display(root)