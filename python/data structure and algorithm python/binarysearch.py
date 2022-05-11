def binarysearch(number_list,number_to_find):
    
    left_index=0
    right_index= len(number_list)-1
    mid_index=0

    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=number_list[mid_index]
        if mid_number==number_to_find:
            return mid_index
        if mid_number<number_to_find:
            left_index=mid_index +1
        else:
            right_index=mid_index-1
    return -1    

if __name__=="__main__":
    a=[22,23,24,25,26,26,26,27,28,29,30]
    c=26
    s=binarysearch(a,c)
    print(s)
