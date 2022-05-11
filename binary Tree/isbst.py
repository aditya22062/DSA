import math
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

def height(node):
    if(node == None):
        return -1
    else:
        ans =  max(height(node.left),height(node.right))+1
    return ans
    
     
import math
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

def height(node):
    if(node == None):
        return -1
    else:
        ans =  max(height(node.left),height(node.right))+1
    return ans
    
class bst:
    def __init__(self):
        self.isbst=False
        self.maxi= float('-inf')
        self.mini=float('inf')
        self.root=None
        self.size=0
        
def Bst(node):
    if(node==None):
        bres=bst()
        bres.isbst = True
        bres.maxi = -math.inf
        bres.mini = math.inf
        bres.size = 0
        return bres
        
    l = Bst(node.left)
    r = Bst(node.right)
    ans=bst()
    
    ans.maxi = max(node.data,max(l.maxi,r.maxi))
    ans.mini = min(node.data,min(l.mini,r.mini))
    
    if(l.isbst==True and r.isbst==True and (l.maxi<=node.data and r.mini>node.data)):
        ans.isbst=True
    

    return ans.isbst
    # write your code here
    
    

n = int(input())
st = input()
arr = [0]*n
arr = list(map(int,st.replace("n","-1").split(" ")));

ans=bst()

root = construct(arr)
ans = Bst(root)

print(ans)