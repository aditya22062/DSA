class Node:
     
    def _init_(self, key, children):
        self.key = key
        self.children=[]
def newNode(key):   
    temp = Node()
    temp.key = key;
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
    
def removeLeaves(root):
    # write code here
    for i in range(len(root.children)-1,-1,-1):
        chil=root.children[i]
        if len(chil.children)==0:
            root.children.remove(chil)
    for child in root.children:
        removeLeaves(child)
    
     
    
lst = []
n = int(input())
lst = list(map(int, input().split()))
root = constructor(lst,n)
removeLeaves(root)
display(root)