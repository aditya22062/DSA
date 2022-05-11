class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nref = None
        self.pref = None


class Double_Linked_List:
    def __init__(self) -> None:
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def printLL(self):
        print()
        if self.head is None:
            return
        else:
            n = self.head
            while n:
                print(n.data, "-->", end=" ")
                n = n.nref

    def printRVL(self):
        print()
        if self.head is None:
            return
        else:
            n = self.head
            while n.nref:
                n = n.nref
            while n:
                print(n.data, "-->", end=" ")
                n = n.pref

    def add_after(self, data, x):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("no node")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref:
                    n.nref.pref = new_node
                n.nref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("no node")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref=n.pref
                if n.pref:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node
    def delete_begin(self):
        if self.head is None:
            return
        if self.head.nref is None:
            self.head =None

        else:
            self.head=self.head.nref
            self.head.pref=None
    def delete_end(self):
        if self.head is None:
            return
        if self.head.nref is None:
            self.head =None
        else:
            n= self.head
            while n.nref:
                n=n.nref
            n.pref.nref=None
    def delete_value(self,x):
        if self.head is None:
            print("empty")
            return
        if self.head.nref is None:
            if x==self.head:
                self.head=None
            else:
                print("gg")
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None  
            return  
        n= self.head
        while n:
            if x==n.data:
                break
            n=n.nref
        if n.nref:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("not in list")
            



if __name__ == '__main__':
    s = Double_Linked_List()
    s.add_begin(10)
    s.add_begin(20)
    s.add_end(30)
    s.add_begin(500)
    s.add_begin(600)
    s.add_after(100, 10)
    s.add_before(5,500)
    s.add_end(50)
    s.delete_value(50)
    s.printLL()
