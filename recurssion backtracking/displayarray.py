def display(arr,idx,n):
   # Write your code here
   if idx==n:
       return
   print(arr[idx])
   display(arr,idx+1,n)




def main():
  
  # Write your code here
  n=int(input())
  l=[]
  for i in range(n):
      l.append(int(input()))
  display(l,0,n)
main()