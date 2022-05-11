class Node:
    def __init__(self,val,next=None) -> None:
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def addFirst(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
        return self.head
    def addLast(self,data):
        node=Node(data)
        if self.head is None:
            print(node.val)
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=node
        return self.head
    def removeFirst(self):
        if self.head is None:
            print("working")
        else:
            self.head=self.head.next
        return self.head
    def size(self):
        
        c=0
        n=self.head
        while n:
            n=n.next
            c+=1
        print(c)


    def removeLast(self):
        if self.head is None :
            print("working")
        else:
            n=self.head
            while n.next.next:
                n=n.next
            n.next=None
        return self.head
    def printll(self):
        if self.head is None:
            return
        else:
            n=self.head
            while n :
                print(n.val,"-->",end=" ")
                n=n.next
if __name__=='__main__':
    
    node=LinkedList()
    node.addFirst(10)
    node.addLast(20)
    node.addLast(30)

    node.addLast(50)
    node.size()
    
    node.printll()

    
