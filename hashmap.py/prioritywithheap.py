data=[]



def size():
   #write your code here
    return len(data)


def add(val):
   #write your code here
   data.append(val)
   upheafify(len(data)-1)
def upheafify(indx):
    if indx==0:
        return
    pi=(indx-1)//2
    if data[indx]<data[pi]:
        swap(indx,pi)
        upheafify(pi)
   

def swap(i,j):
    data[j],data[i]=data[i],data[j]
def remove():
    #write your code here
    if size()==0:
        print("Underflow")
        return -1
    swap(0,len(data)-1)
    val=len(data)-1
    downheapify(0)
    return val
def downheapify(i):
    mini=i
    li=2*i+1
    if li<len(data) and data[li]<data[mini]:
        mini=li
    
    ri=2*i+2
    if ri<len(data) and data[ri]<data[mini]:
        mini=ri         
    if mini!=i:
        swap(i,mini)
        downheapify(mini)
def peek():
   #write your code here
   if size()==0:
       print("Underflow")
       return -1
   return data[0]
   



while(1):
    s=input().split()
    if s[0]=='add':
        num=s[1]
        val=int(num)
        add(val)
   
    elif s[0]=='remove':
        val=remove()
        if val!=-1:
            print(val,end="\n")
   
    elif s[0]=='peek':
        val=peek()
        if val!=-1:
            print(val,end="\n")
           
    else:
        break