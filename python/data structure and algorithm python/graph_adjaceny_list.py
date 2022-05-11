def add_node(v):
    if v  in graph:
        return
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        return
    elif v2 not in graph:
        return
    else:
        
        graph[v1]+=v2
        graph[v2]+=v1
def delete_edge(v1,v2):
    if v1 not in graph:
        return
    elif v2 not in graph:
        return
    else:
    
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
    return graph
def delete_node(v):
    if v not in graph:
        return
    else:
        graph.pop(v)
        for i in graph:
            l=graph[i]
            if v in l:
                l.remove(v)
def DFS(node,Visited,graph):
    if node not in Visited:
        print(node)
        Visited.add(node)
        for i in graph[node]:
            DFS(i,Visited,graph)


if __name__=='__main__':
    Visited=set()
    graph={}
    add_node("b")
    add_node("c")
    add_node("a")
    add_node("e")
    add_node("d")
    add_edge("a","b")
    add_edge("a","c")
    add_edge("a","d")
    add_edge("d","e")
    add_edge("b","e")
    add_edge("c","d",)
    DFS("b",Visited,graph)
    
    
    