import math
class Node:
    isbal = True
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


        
isbal2=True     
def isbalance(node):
    # write your code here
    global isbal2
    
    if node==None:
        return 0
    lh=isbalance(node.left)
    rh=isbalance(node.right)
    gap=abs(lh-rh)
    if gap>1:
        isbal2=False
    
    

n = int(input())
st = input()
arr = [0]*n
arr = list(map(int,st.replace("n","-1").split(" ")));



root = construct(arr)
isbalance(root)
if isbal2:
    print("false")
else:
    print("true")