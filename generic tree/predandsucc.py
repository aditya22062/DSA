state=0
pred = None
succ = None
class Node:
     
    def __init__(self, data):
        self.data = data
        self.child = []
   
 # Utility function to create a new tree node
def newNode(data):   
    temp = Node(data)
    return temp
     
def constructor(lst,n):
    root = None
    stack = []
    for i in range(0,n):
        if lst[i]==-1:
            stack.pop()
        else:
            t= Node(lst[i])
            if len(stack) > 0:
                stack[-1].child.append(t)
                
            else:
                root=t
                
            stack.append(t)
    return root

    

def prendsucc(node,data):
    #Write your code here
    global state
    global pred
    global succ
    if state==0:
        if node.data==data:
            state=1
        else:
            pred=node
    elif state==1:
        succ=node
        state=2
    for child in node.child:
        prendsucc(node,data)
  
lst = []
# number of elements as input
n = int(input())

lst = list(map(int, input().split()))


root = constructor(lst,n)  
data = int(input())
prendsucc(root,data)

if pred == None:
    print("Predecessor = Not found")
else:
    print("Predecessor =" , pred.data)
    
if succ == None:
    print("Successor = Not found")
else:
    print("Successor =", succ.data)
