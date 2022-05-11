n=input()
a=0
ab=0
abc=0
for i in n:
    if i=='a':
        a=2*a+1
    elif i =='b':
        ab=2*ab+a
    else:
        abc=2*abc+ab
print(abc)