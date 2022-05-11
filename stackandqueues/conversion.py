def infix(exp):
    # write your code here  
    postfix=[]
    operators=[]
    prefix=[]
    for i in exp:
        if i=='(':
            operators.append(i)
        elif i==')':
            while operator[-1]!='(':
                operator=operators.pop()
                post2=postfix.pop()
                post1=postfix.pop()
                postv=str(post1)+str(post2)+operator
                postfix.append(postv)
            
                pre2=prefix.pop()
                pre1=prefix.pop()
                prev=operator+str(pre1)+str(pre2)
                prefix.append(prev)
            operators.pop()

        elif i=='+' or i =='-' or i =='*' or i =='/':
            while len(operators)>0 and operators[-1]!='(' and precedence(i)<=precedence(operators[-1]):
                
                operator=operators.pop()
                post2=postfix.pop()
                post1=postfix.pop()
                postv=str(post1)+str(post2)+operator
                postfix.append(postv)
                
                
                pre2=prefix.pop()
                pre1=prefix.pop()
                prev=operator+str(pre1)+str(pre2)
                prefix.append(prev)
            operators.append(i)
        else:
            postfix.append(i)
            prefix.append(i)
    while len(operators) !=0:
        operator=operators.pop()
        post2=postfix.pop()
        post1=postfix.pop()
        postv=str(post1)+str(post2)+operator
        postfix.append(postv)
        
        
        pre2=prefix.pop()
        pre1=prefix.pop()
        prev=operator+str(pre1)+str(pre2)
        prefix.append(prev)
    

    print(postfix[-1])
    print(prefix[-1])    

def precedence(ch):
    if ch=='+':
        return 1
    elif ch=='-':
        return 1
    elif ch=='*':
        return 2
    elif ch=='/':
        return 2
def operation(v1,v2,exp1):
    if exp1=='+':
        return v1+v2
    elif exp1=='-':
        return v1-v2
    elif exp1=='*':
        return v1*v2
    elif exp1=='/':
        return v1/v2

    
exp = input()
exp = exp.replace(" ", "")


infix(exp)

# i/p test case
# 2 + 6 * 4 / 8 - 3