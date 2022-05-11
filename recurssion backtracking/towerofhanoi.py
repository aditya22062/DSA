def TowerOfHanoi(n,n1,n2,n3):
    # write your code here
    if n==0:
        return

    TowerOfHanoi(n-1,n1,n3,n2)
    print(f"{n}[{n1} ->{n2}]")
    TowerOfHanoi(n-1,n3,n2,n1)


n = int(input())
n1=int(input())
n2=int(input())
n3= int(input())
TowerOfHanoi(n,n1,n2,n3)