class TwoStack :
    def __init__(self, cap) :
     # write your code here
        self.arr=[0]*cap
        self.tos1=-1
        self.tos=len(self.arr)
    

    def size1(self) :
     # write your code here
        return self.tos+1


    def size2(self) :
      # write your code here
        return len(self.arr)-self.tos
    

    def push1(self, val) :
        if self.tos==self.tos1+1:
            print("Stack overflow")
        else:
            self.tos1+=1
            self.arr[self.tos1]=val

    def push2(self,val) :
        if self.tos==self.tos1+1:
            print("Stack overflow")
        else:
            self.tos-=1
            self.arr[self.tos]=val
     

    def pop1(self) :
        if self.size1()==0:
            print("Stack underflow")
            return -1
        else:
            val=self.arr[self.tos1]
            self.tos1-=1
            return val
      

    def pop2(self) :
        if self.size2()==0:
            print("Stack underflow")
            return -1
        else:
            val=self.arr[self.tos]
            self.tos+=1
            return val

    def top1(self) :
        if self.size1()==0:
            print("Stack underflow")
            return -1
        else:
            val=self.arr[self.tos1]
            return val
    def top2(self) :
        if self.size2()==0:
            print("Stack underflow")
            return -1
        else:
            val=self.arr[self.tos]
            return val
   

cap=int(input()) 
l1 = TwoStack(cap)
while 1 > 0 :
        str = input()
        if str[0] == 'q':
            break
    
        elif str[0] == 'p'and str[4]=='1':
            val = int(str[-3] + str[-2])
            l1.push1(val)
        elif str[0] == 'p'and str[4]=='2':
            val = int(str[-3] + str[-2])
            l1.push2(val)
        
        elif str[0] == 't'and str[3]=='1':
            val=l1.top1()
            if val != -1:
                print(val)

        
        elif str[0] == 't'and str[3]=='2':
            val=l1.top2()
            if val != -1:
                print(val)

        elif str[0] == 'p'and str[3]=='1':
            val=l1.pop1()
            if val != -1:
                print(val)

        
        elif str[0] == 'p'and str[3]=='2':
            val=l1.pop2()
            if val != -1:
                print(val)

        
        elif str[0] == 's':
        
            print(l1.size())
        
        