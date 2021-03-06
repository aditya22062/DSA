
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
    
    
    
pre=""
post=""
ino=""
def iterativePrePostInTraversal(node):
    # write your code here
    global pre
    global post
    global ino
    q=[]
    newnode=Pair(node,1)
    q.append(newnode)
    while len(q)>0:
        tq=q.pop()
        if tq.state==1:
            pre+=str(tq.node.data)+" "
            tq.state+=1
            if tq.node.left !=None:
                pq=Pair(tq.node.left,1)
                q.append(pq)
        elif tq.state==2:
            ino+=str(tq.node.data)+" "
            tq.state+=1
            if tq.node.right != None:
                iq=Pair(tq.node.right,1)
                q.append(iq)

        else:
            post+=str(tq.node.data)+" "
            q.pop()
n = int(input())
st = input()
arr = [0]*n
arr = list(map(int,st.replace("n","-1").split(" ")));


root = construct(arr)
iterativePrePostInTraversal(root)
print(pre)
print(ino)
print(post)