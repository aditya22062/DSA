def prefix(exp):
    # write your code here
    postfix=[]
    infix=[]
    val=[]
    
    for i in range(len(exp)):
        ch=exp[i]
        if ch =='+' or ch=='-' or ch=='*' or ch=='/':
            val2=val.pop()
            val1=val.pop()
            tval=operation(val1,val2,ch)
            val.append(tval)
            
            inv2=infix.pop()
            inv1=infix.pop()
            ival='('+''+inv1+''+ch+''+inv2+')'
            infix.append(ival)

            prev2=postfix.pop()
            prev1=postfix.pop()
            prevall=prev1+prev2+ch
            postfix.append(prevall)
        else:
            val.append(ch)
            infix.append(ch)
            postfix.append(ch)
    print(val[-1])
    print(infix[-1])
    print(postfix[-1])
def operation(v1,v2,exp):
    if exp=='+':
        return int(v1)+int(v2)
    elif exp=='-':
        return int(v1)-int(v2)
    elif exp=='*':
        return int(v1)*int(v2)
    elif exp=='/':
        return int(v1)/int(v2)

exp = input()
prefix(exp)
