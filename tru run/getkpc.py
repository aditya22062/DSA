
def solution(str1,asf,count,pos):

    if pos==len(str1):
        if count==0:
            print(asf)
        else:
            print(asf+str(count))
        return
    if count>0:
        solution(str1,asf+str(count)+str1[pos],0,pos+1)
    else:
        solution(str1,asf+str1[pos],0,pos+1)
    solution(str1,asf,count+1,pos+1)






inp=input()

solution(inp,"",0,0)