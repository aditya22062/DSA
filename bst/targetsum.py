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
    
def find(node,data):
    if node==None:
        return False
    if data>node.data:
        return find(node.right,data)
    elif data<node.data:
        return find(node.left,data)
    else:
        return True
def travelAndPrint(root,node ,tar):
    #write your code here
    if node==None:
        return
    travelAndPrint(root,node.left,tar)
    comp=tar-node.data
    if node.data<comp:
        if find(node,comp)==True:
            print(str(node.data)+" "+str(comp))
    travelAndPrint(root,node.right,tar)    
n=int(input())
values = list(map(str, input().split()))
arr=[0]*n
for i in range(0,n):
    if values[i]!="n":
        arr[i]=int(values[i])
    else:
        arr[i]=None
d1=int(input())
root=construct(arr)
print(travelAndPrint(root,root,d1))