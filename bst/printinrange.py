class Node:
    def __init__(self, data,left,right):
        self.data = data
        self.left = left
        self.right = right
        
class Pair:
    def __init__(self,node,st):
        self.node=node;
        self.state=st;
        

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
        

def pir(node,d1, d2):
    #write your code here
    if node==None:
        return
    if d1>node.data and d2>node.data:
        pir(node.right,d1,d2)
    elif d1<node.data and d2<node.data:
        pir(node.left.d1,d2)
    else:
        pir(node.left,d1,d2)
        print(node.data)
        pir(node.right,d1,d2)
    
n=int(input())
values = list(map(str, input().split()))
arr=[0]*n
for i in range(0,n):
    if values[i]!="n":
        arr[i]=int(values[i])
    else:
        arr[i]=None
d1=int(input())
d2=int(input())
root=construct(arr)
pir(root,d1,d2)