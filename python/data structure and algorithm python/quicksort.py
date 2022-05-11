def swap(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]
def partition(start,end,elements):
    piviot_index=start
    piviot=elements[piviot_index]

    while start<end:
        while start<len(elements)and elements[start]<=piviot:
            start+=1
        while elements[end]>piviot:
            end-=1
        if start<end:
            swap(start,end,elements)
    swap(piviot_index,end,elements)
    return end
def quick_sort(elements,start,end):
    if start < end:
        pi=partition(start,end,elements)
        quick_sort(elements,start,pi-1)
        quick_sort(elements,pi+1,end)


if __name__=='__main__':
    a=[4,3,2,1,0,5,6]
    quick_sort(a,0,len(a)-1)
    print(a)

