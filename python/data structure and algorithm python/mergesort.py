def findMedianSortedArrays( nums1, nums2) -> float:
        l=[]
        a=len(nums1)
        b=len(nums2)
        i=0
        j=0
        while i<a and j<b:
            if nums1[i] <= nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        while i<a:
                l.append(nums1[i])
                i+=1
        while j<b:
                l.append(nums2[j])
                j+=1
        
if __name__=='__main__':
    n=[1,2]
    n1=[1,5,9,10,11,13,12,13,15]
    print(findMedianSortedArrays(n,n1))
        