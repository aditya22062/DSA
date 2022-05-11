def cooldownInfiniteTransaction(arr,n):
   #write your code here
    obsp=-arr[0]
    ossp=0
    ocsp=0
    nbsp=0
    ncsp=0
    nssp=0
    for i in range(1,len(arr)):
        nbsp=max(obsp,ocsp-arr[i])
        nssp=max(ossp,arr[i]+obsp)
        ncsp=max(ossp,ocsp)
        obsp=nbsp
        ossp=nssp
        ocsp=ncsp
    print(ossp)

def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    cooldownInfiniteTransaction(array,n)

if __name__ == '__main__':
    main()