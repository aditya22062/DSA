class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

# create a new tree node

def newNode(data):
    temp = Node(data)
    return temp                            


# n-ary tree level wise

def constructor(lst, n):
    root = None
    stack = []
    for i in range(0, n) :
        if lst[i] == -1:
            stack.pop()
        else:
            t = Node(lst[i])
            if len(stack) > 0:
                stack[-1].children.append(t)

            else:
                root = t

            stack.append(t)

    return root

def findpath(root,val):
    if root.data==val:
        arr=[]
        arr.append(root.data)
        return arr
    for child in root.children:
        a=findpath(child,val)
        if len(a)>0:
            a.append(root.data)
            return a
    return []
def nodeToRootPath(root,val1,val2):
    s1=findpath(root,val1)
    s2=findpath(root,val2)
    i=len(s1)-1
    j=len(s2)-1
    while s1[i]==s2[j] and i>=0 and j>=0:
        i-=1
        j-=1
    i+=1
    j+=1
    return s1[i]
    # Write your code here
    
    

# main function

if __name__ == "__main__":
    lst = []                                                        
    n = int(input())
    lst = list(map(int, input().split(" ")))
    val1 = int(input())
    val2=int(input())
    root = constructor(lst, n)
    path = nodeToRootPath(root, val1,val2)
    print(path)