def sortbyvalue(arr,key):
    size=len(arr)
    for j in range(size-1):
        for i in range(size-1-j):
            if arr[i][key]>arr[i+1][key]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
if __name__=="__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sortbyvalue(elements,key='name')
    for i in sortbyvalue(elements,key='name'):
        print(i)
    
    