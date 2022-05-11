class MinStack:
       
    def __init__(self):
        self.data = [ ];
        self.minival = 0
       
    def size(self):
        return len(self.data)
       

    def push(self , val):
        # write your code here
        if len(self.data)==0:
            self.data.append(val)
        elif val>=self.minival:
            self.data.append(val)
        else:
            self.data.append(val+val-self.minival)
        
   
       
    def top(self):
        # write your code here
        if len(self.data)==0:
            print("Stack underflow")
            return -1
        else:
            if self.data[-1]>=self.minival:
                return self.data[-1]
            else:
                return self.minival
       
       
   
    def pop(self):
        # write your code here
        if len(self.data)==0:
            print("Stack underflow")
            return -1
        else:
            
            if self.data[-1]>=self.minival:
                value=self.data.pop()
                return value
            else:
                ov =self.minival
                minival=2*self.minival-self.data[-1]
                return ov
       
    def minimum(self):
        # write your code here
        if len(self.data)==0:
            print("Stack underflow")
            return -1
        else :
            return self.minival


def main():
   
   
    inpStr = str(input()).strip().split(" ")
    st = MinStack()
   
    while inpStr[0] != "quit":
        if inpStr[0].strip() == "push":
            val = inpStr[1]
            st.push(int(val))
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
        elif inpStr[0].strip() == "min":
            val = st.minimum()
            if val != -1:
                print(val)
           
        inpStr = str(input()).strip().split(" ")
   
   
main()