def pythagorastriplet(a):
    a1=a[0]
    b1=a[1]
    c1=a[2]
    maxi=max(a1,b1,c1)
    a.remove(maxi)
    sumi=a[0]*a[0]+a[1]*a[1]
    
    
    if maxi*maxi==sumi:
        return True
    else:
        return False
a1=int(input())
b1=int(input())
c1=int(input())
a=[a1,b1,c1]
maxi=max(a1,b1,c1)
a.remove(maxi)
sumi=a[0]*a[0]+a[1]*a[1]
    
    
if maxi*maxi==sumi:
    print("true")
else:
    print("false")