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


def areMirror(root1, root2):
    if len(root1.children)!=len(root2.children):
        return False
    for i in range(len(root1.children)-1):
        j=len(root1.children)-1-i
        r1=root1.children.pop(i)
        r2=root1.children.pop(j)
        if areMirror(r1,r2)==False:
            return False
    return True
    # Write your code here
def symmetric(node):
    return areMirror(node,node)
    

# main function

if __name__ == "__main__":
    
    lst1 = []                                                        
    n1 = int(input())
    lst1 = list(map(int, input().split(" ")))
    root1 = constructor(lst1, n1)

    flag = symmetric(root1)
    if flag == False:
        print("false")
    
    else:
        print("true")