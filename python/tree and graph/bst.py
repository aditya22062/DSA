class BST:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None
    
    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        else:
            if self.key>data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left=BST(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right=BST(data)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder_traversal()

    def search(self,data):
        if self.key==data:
            print(True)
        
        if self.key>data:
            if self.left:
                self.left.search(data)
            else:
                print( False)
            
        if self.key<data:
            if self.right:
                self.right.search(data)
            else:
                print(False)
            
    def minimum(self):
        if self.left:
            self.left.minimum()
        else:
            print( self.key)
    def maximum(self):
        if self.right:
            self.right.maximum()
        else:
            print(self.key)
    def delete(self,data):
        #check if tree is empty or not
        #find the key to delete
        #delete the key

        if self.key is None:
            return
        if self.key<data:
            if self.right:
                self.right=self.right.delete(data)
            else:
                return
        if self.key>data:
            if self.left:
               self.left= self.left.delete(data)
            else:
                return
        else:
            if self.left ==None:
                temp=self.right
                self=None
                return temp
            if self.right==None:
                temp=self.left
                self=None
                return temp

            node=self.right
            while node.left:
                node=node.left
            self.key=node.key
            self.right=self.right.delete(node.key)


        return self

if __name__=='__main__':
    root=BST(None)
    root.insert(10)
    root.insert(11)
    root.insert(5)
    root.insert(6)
    root.insert(8)
    root.insert(13)
    root.inorder_traversal()
    root.delete(10)
    print()
    root.inorder_traversal()