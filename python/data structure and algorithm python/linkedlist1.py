class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=new_node
            new_node.next=None
    def delete_data(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return


        n=self.head
        while n.next:
            if n.next.data==data:
                n.next=n.next.next
                break
            n=n.next
            if n.next is None:
                print(data," is not there")
    def len(self):
        c=0
        if self.head is None:
            return
        
        n=self.head
        while n:
            c+=1
            n=n.next
        return c
    def add_after(self,data,x):
        new_node=Node(data)
        n= self.head
        while n:
            if x==n.data:
                break
            n=n.next
        if n is None:
            print("node is not present")
        else:
            new_node.next=n.next
            n.next=new_node
    def add_before(self,data,x):
        new_node=Node(data)
        if x==self.head.data:
            new_node.next=self.head
            self.head=new_node
            return
        n=self.head
        while n:
            if x==n.next.data:
                break
            n=n.next
        if n is None:
            print("node is not there")
        else:
            new_node.next=n.next
            n.next=new_node

                
    def printll(self):
        if self.head is None:
            return
        else:
            n=self.head
            while n :
                print(n.data,"-->",end=" ")
                n=n.next
    
if __name__=="__main__":
    a=LinkedList()
    a.add_begin(10)
    

    a.add_before(1,10)
    
    a.printll()
    print()
    print(a.len())
                
