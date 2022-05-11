def display(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=" ")
        print()

def solveSudoku(board,i,j):
    if i == len(board):
        display(board)
        return
        
    ni=0
    nj=0
    if j ==len(board[0])-1:
        ni=i+1
        nj=0
    else:
        ni=i
        nj=j+1

    if board[i][j]!=0:
        solveSudoku(board,ni,nj)
    else:
        for val in range(1,10):
            if isValid(board,i,j,val):
                board[i][j]=val
                solveSudoku(board,ni,nj)
                board[i][j]=0

def isValid(board,i,j,val):
    for x in range(len(board)):
        if board[x][j]==val:
            return False
    for y in range(len(board)):
        if board[i][y]==val:
            return False

    i=(i//3)  *3
    j=(j//3) * 3
    for x in range(3):
      for y in range(3):
        if (board[x + i][y + j] == val):
          return False
    return True
if __name__=='__main__':
    arr=[]
    for i in range(9):
        l=list(map(int,input().split()))
        arr.append(l)
    solveSudoku(arr, 0, 0)