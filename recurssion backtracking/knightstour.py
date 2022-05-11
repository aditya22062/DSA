def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j],"",end='')
        print()
    print()
    
    
def printKnightsTour(chess,n,r,c,upcomingMove):
    # write your code here
    if r<0 or c<0 or r>=len(chess) or c>=len(chess) or chess[r][c]>0:
        return
    elif upcomingMove==len(chess)*len(chess):
        chess[r][c]=upcomingMove
        displayBoard(chess)
        chess[r][c]=0
        return


    chess[r][c]=upcomingMove
    printKnightsTour(chess,n,r-2,c+1,upcomingMove+1)
    printKnightsTour(chess,n,r-1,c+2,upcomingMove+1)
    printKnightsTour(chess,n,r+1,c+2,upcomingMove+1)
    printKnightsTour(chess,n,r+2,c+1,upcomingMove+1)
    printKnightsTour(chess,n,r+2,c-1,upcomingMove+1)
    printKnightsTour(chess,n,r+1,c-2,upcomingMove+1)
    printKnightsTour(chess,n,r-1,c-2,upcomingMove+1)
    printKnightsTour(chess,n,r-2,c-1,upcomingMove+1)
    chess[r][c]=0



def main():
    n=int(input())
    chess=[]
    for i in range(n):
        a=[]
        for j in range(n):
            a.append(0)
        chess.append(a)
    row=int(input())    
    col=int(input()) 
    printKnightsTour(chess,n,row,col,1)
main()