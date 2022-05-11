

hl=['stdio.h','math.h']
d={}
l=[]
for i in hl:
    if i not in d:
        d[i]=0
        break
    l.append(d)
print(l)