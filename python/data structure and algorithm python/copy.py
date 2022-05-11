arr=[2, 2, 4, 9, 9, 9, 11, 17, 21, 25, 32, 38]
index_to_delete=[]
for i in arr:
    index_to_delete.append(i)
index_to_delete=list(set(index_to_delete))
index_to_delete.sort()
del index_to_delete[0]
print(index_to_delete)
