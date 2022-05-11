def queencombination(qpsf,n,chess,lc):
    if qpsf==n:
        for i in range(len(chess)):
            for j in range(len(chess)):
                if chess[i][j]==True:
                    print("q")
                else:
                    print("-\n",end="")
            print()
        print()
        
        return

    for i in range(n*n):
        row=i//n
        col=i%n

        chess[row][col]=True
        queencombination(qpsf+1,n,chess,i)
        chess[row][col]=False

n=int(input())
chess=[[False for i in range(n)]for j in range(n)]
queencombination(0,n,chess,-1)