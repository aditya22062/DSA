from collections import deque
class Node:
     
    def __init__(self, key):
         
        self.key = key
        self.child = []

def newNode(key):   
    temp = Node(key)
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
    
def LevelOrderTraversal(root):
    #rpa
    q=deque()
    q.append(root)
    while len(q)!=0:
        r=q.popleft()
        print(str(r.key)+" ",end="")
        for child in r.child:
            
            q.append(child)
    print(".")

        
lst = []
n = int(input())
lst = list(map(int, input().split()))
root = constructor(lst,n)  
LevelOrderTraversal(root)
