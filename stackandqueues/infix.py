def infix(exp):
    # write your code here  
    stofoperands=[]
    stofoperators=[]
    for i in exp:
        if i=='(':
            stofoperators.append(i)
        elif i==')':
            while stofoperators[-1] !='(':
                operator=stofoperators.pop()
                v2=stofoperands.pop()
                v1=stofoperands.pop()
                opv=operation(v1,v2,operator)
                stofoperands.append(opv)
            stofoperators.pop()

        elif i=='+' or i =='-' or i =='*' or i =='/':
            while len(stofoperators)>0 and stofoperators[-1]!='(' and precedence(i)<=precedence(stofoperators[-1]):
                
                operator=stofoperators.pop()
                v2=stofoperands.pop()
                v1=stofoperands.pop()
                opv=operation(v1,v2,operator)
                stofoperands.append(opv)
            stofoperators.append(i)
        else:
            stofoperands.append(ord(i)-ord('0'))
    while len(stofoperators) !=0:
        operator=stofoperators.pop()
        v2=stofoperands.pop()
        v1=stofoperands.pop()
        opv=operation(v1,v2,operator)
        stofoperands.append(opv)
    print(stofoperands[-1])    

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