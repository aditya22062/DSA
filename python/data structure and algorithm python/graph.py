def insert_node(v):

    if v in node:
        return
    else:
        node.append(v)
        for i in graph:
           i.append(0)
        temp=[]
        for i in range(len(node)):
            temp.append(0)
        graph.append(temp)
    return graph
def add_edge(v1,v2,weight):
    if v1 not in node:
        return
    elif v2 not in node:
        return
    else:
        index1=node.index(v1)
        index2=node.index(v2)
        graph[index1][index2]=weight
        graph[index2][index1]=weight
def print_graph():
    for i in range(len(node)):
        for j in range(len(node)):
            print(format(graph[i][j],"<3"),end=" ")
        print()
def delete_node(v):
    pass
def delete_edge(v1,v2):
    if v1 not in node:
        return
    elif v2 not in node:
        return
    else:
        index1=node.index(v1)
        index2=node.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0
def delete_node(v):
    if v not in node:
        return
    else:
        index=node.index(v)
        a=len(node)
        node.remove(v)
        a-=1
        graph.pop(index)
        for i in graph:
            i.pop(index)


            

if __name__=='__main__':
    node=[]
    graph=[]
    insert_node("a")
    insert_node("b")
    insert_node("c")
    insert_node(5)
    add_edge("a","b",10)
    add_edge("a","c",10)
    add_edge("b","c",10)
    delete_node("b")

    delete_edge("a","b")
    print(graph)
    print_graph()
    

  