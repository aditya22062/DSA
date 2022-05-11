import threading, queue

class stack:
    def __init__(self):
        self.mainQ = queue.Queue()
        self.helperQ = queue.Queue()
    
    def size(self):
        # write your code here
        return self.mainQ.qsize()
        
    
    def push(self, data):
        # write your code here
        self.mainQ.put(data)

    def top(self):
        # write your code here
        if self.size()==0:
            print("Stack underflow")
            return -1
        else:
            while self.size()!=0:
                self.helperQ.put(self.mainQ.get())
            return self.helperQ[-1]
        
    def pop(self):
        # write your code here
        if self.size()==0:
            print("Stack underflow")
            return -1
        else:
            while self.size()!=0:
                self.helperQ.put(self.mainQ.get())
            while self.helperQ.qsize()!=0:
                self.mainQ.put(self.helperQ.get())
            val=self.mainQ.get()
            return val

            
def main():
    st = stack();
    sr = input().strip();
    srP = sr.split(" ");
    
    while(srP[0]!="quit"):
        
        if(srP[0].strip()=="push"):
            st.push(int(srP[1]));
            
        elif(srP[0].strip()=="pop"):
            val = st.get();
            if(val != -1):
                print(val);
            
        elif(srP[0].strip()=="top"):
            val = st.top();
            if(val != -1):
                print(val);
                
        elif(srP[0].strip()=="size"):
            print(st.size());
        
        sr = input().strip();
        srP = sr.split(" ");
main()