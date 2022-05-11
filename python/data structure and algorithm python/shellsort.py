def shellsort(arr):
    size=len(arr)
    gap=size//2
    while gap>0:
        for i in range(gap,size):
            anchor=arr[i]
            j=i
            while j>=gap and arr[j-gap]>anchor:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=anchor
        gap=gap//2

if __name__ == '__main__':
    a=[21,38,2,2,9,9,17,4,25,11,32,9]
    shellsort(a)
    print(sorted(set(a)))