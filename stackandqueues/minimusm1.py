class CustomStack:
       
    def __init__(self ):
        
        self.arr = []
        self.minimumst=[]
    def size(self):
        # write your code here
        return len(self.arr)
       

    def push(self , data):
        # write your code here
        if len(self.arr)==0 :
            self.arr.append(data)
            self.minimumst.append(data)
        elif data <=self.minimumst[-1]:
            self.arr.append(data)
            self.minimumst.append(data)
        else:
            self.arr.append(data)
   
       
    def top(self):
        # write your code here
        if len(self.arr)==0:
            print("Stack underflow")
            return -1
        else:
            return self.arr[-1]

       
   
    def pop(self):
        # write your code here
        if len(self.arr)==0:
            print("Stack underflow")
            return -1
        else:
            value=self.arr.pop()
            if value==self.minimumst[-1]:
                self.minimumst.pop()
        return value
       
    def display(self):
        # write your code here
        for i in range(len(self.arr)):
            print(i)
    def minimum(self) :
        if len(self.minimumst)==0:
            print("Stack underflow")
            return -1
        else:
            print(self.minimumst[-1])


def main():
   
    
   
    inpStr = str(input()).split(" ")
    st = CustomStack()

    while inpStr[0] != "quit":
        if inpStr[0].strip() == "push":
            val = inpStr[1]
            st.push(val)
        elif inpStr[0].strip() == "pop":
            val = st.pop()
            if val != -1:
                print(val)
        elif inpStr[0].strip() == "top":
            val = st.top()
            if val != -1:
                print(val)
        elif inpStr[0].strip() == "size":
            print(st.size())
        elif inpStr[0].strip() == "display":
            st.display()
        elif inpStr[0].strip()=="min":
            st.minimum()
           
        inpStr = str(input()).split(" ")
           
   
   
   
main()