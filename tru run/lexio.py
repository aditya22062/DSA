def lexiograph(i,n):
    if i >n:
        return


    print(i)
    for j in range(10):
        lexiograph((10*i+j),n)

n=int(input())
for i in range(1,10):
    lexiograph(i,n)