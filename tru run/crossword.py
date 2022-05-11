def solution(arr, words,  vidx):
    if(vidx == len(words)):
        print1(arr)
        return

    for i in range(10):
        for j in range(10):
            word = words[vidx]
            if(arr[i][j] == "-" or arr[i][j] == word[0]):
                if(canPlaceVertical(arr, word, i, j)):
                    
                    visited=placeVertical(arr, word, i, j)

                    solution(arr, word, vidx + 1)
                    unplaceVertical(arr, word, i, j, visited)

                if(canPlaceHorizontal(arr, word, i, j)):
                    
                    visitedv=placeHorizontal(arr, word, i, j)

                    solution(arr, word, vidx + 1)
                    unplaceHorizontal(arr, word, i, j, visitedv)


def canPlaceVertical(arr, word, r, c):
    if(r- 1 >= 0 and arr[r-1][c] != "+") :
        return False
    elif(r+len(word)<=len(arr) and arr[r+len(word)][c]!="+"):
        return False
    for i in range(len(word)):
        if(r + i >= len(arr)):
            return False
        
        if(arr[r+i][c] == "-" or arr[r+i][c] == word[i]):
            continue
        else:
            return False
    


def canPlaceHorizontal(arr, word,  r,  c):
    if(c- 1 >= 0 and arr[r][c - 1] != "+") :
        return False
    elif(c+len(word)<=len(arr[0]) and arr[r][c+len(word)]!="+"):
        return False
    for i in range(len(word)):
        if(c + i >= len(arr)):
            return False
        
        if(arr[r][c + i] == "-" or arr[r][c + i] == word[i]):
            continue
        else:
            return False

  


def placeVertical(arr,word,r,c):
    visitedv=[False]*len(word)
    for i in range(len(word)):
        if (arr[r+i][c] == "-"):
            arr[r+i][c] = word[i]
            visitedv[i] = True
    return visitedv
        


def unplaceVertical(arr,word,r,c,visitedv):
    for i in len(word):
        if(visitedv[i]):
            arr[r + i][c] = "-"
 

def placeHorizontal(arr, word, r, c):
    visited=[False]*len(word)
    for i in range(len(word)):
        if (arr[r][c + i] == "-"):
            arr[r][c + i] = word[i]
            visited[i] = True
    return visited
        
        


def unplaceHorizontal(arr, word, r,  c, visited):
    for i in range(len(word)):
        if(visited[i]):
            arr[r][c + i] = "-"	
    

def print1(arr):

    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j],end=" ")
        print()
        


                    

if __name__=='__main__':

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    n=int(input())
    words=[]
    for i in range(n):
        a=input()
        words.append(a)
    solution(crossword,words,0)
                    


                    


                    
                            
