def buuble_sort(element):
    for j in range(len(element)-1):
        for i in range(len(element)-1-j):
            if element[i]>element[i+1]:
                element[i],element[i+1]=element[i+1],element[i]
                



if __name__=="__main__":
    a=[1,5,94,78,5,6]
    s=buuble_sort(a)
    print(a)
