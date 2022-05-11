class BinaryTree:
    def __init__(self,data) -> None:
        self.data=data
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.data is None:
            self.data=data
        if self.data>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BinaryTree(data)
        if self.data<data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BinaryTree(data)
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.data,end=" ")
        if self.rchild:
            self.rchild.in_order()
    def pre_order(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.data,end=" ")
    def search(self,data):
        if self.data is None:
            print("false")
        if self.data==data:
            print("True")    
        if self.data>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("false")

        if self.data<data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("false")        
    def Max(self):
        if self.rchild:
            self.rchild.Max()
        else:
            return self.data
    def Min(self):
        if self.lchild :
            self.lchild.Min()
        else:
            return self.data
    def Delete(self,data):
    
        if self.data>data:
            if self.lchild:
                self.lchild=self.lchild.Delete(data)
        elif self.data<data:
            if self.rchild:
                self.rchild=self.rchild.Delete(data)   
        else:
            if self.lchild is None and self.rchild is None:
                return None
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild
            
            min_value=self.rchild.Min()
            self.data=min_value
            self.rchild=self.rchild.Delete(min_value)
        return self


if __name__=='__main__':
    root=BinaryTree(10)
    l=[1,9,8,5,6,2,4,15,25,39,24]
    for i in l:
        root.insert(i)
   
    #root.search(int(input() ))
    root.Delete(int(input()))
    root.in_order()