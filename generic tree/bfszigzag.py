from collections import deque
class Node:
     
    def _init_(self, key, children):
         
        self.key = key
        # self.child = []
        self.children=[]
   
 # Utility function to create a new tree node
def newNode(key):   
    temp = Node()
    temp.key = key;
    # temp.child = []
    temp.children = []
    return temp
    
    
def display(root):
    s = ""
    s = str(root.key) + " -> "
    for child in root.children:
        s += str(child.key) + ", "
    
    s += "."   
    print(s)
    for child in root.children:
        display(child)
# Prints the n-ary tree level wise
def constructor(lst,n):
    root = None
    stack = []
    for i in range(0,n):
        if lst[i]==-1:
            stack.pop()
        else:
            t= newNode(lst[i])
            if len(stack) > 0:
                stack[-1].children.append(t)
                
            else:
                root=t
                
            stack.append(t)
    return root
def getTail(root):
    while len(root.children) == 1:
        root=root.children[0]
    return root    

def linearize(root):
    # write your code here
    mq=deque()
    mq.append(root)
    cq=deque()

    while len(mq)!=0:
        r=mq.popleft()
        print(r.key,end=" ")
        for child in r.children:
            cq.append(child)
        if len(mq)==0:
            mq=cq
            cq=deque()
            print()
                    

lst = []
# number of elements as input
n = int(input())
# s1 =input().split()
# values = input().split()

lst = list(map(int, input().split()))
     

root = constructor(lst,n)
linearize(root)
#display(root)
