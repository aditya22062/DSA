import threading , queue

class Edge:
    def __init__(self,src,nbr):
        self.src = src
        self.nbr = nbr
        

def main():
    vtces = int(input())
    edges = int(input()) 
    graph = {}
    for i in range(vtces):
        graph[i] = []
    
    for i in range(edges):   
        lines = input().split(" ") 
        v1=int(lines[0]) 
        v2=int(lines[1])
        e1 = Edge(v1 ,v2 ) 
        graph[e1.src].append(e1) 
    visited=[False]*vtces
    st=[]
    for v in range(vtces):
        if visited[v]==False:
            topolgical(graph,v,visited,st)
    while len(st)>0:
        print(st.pop())
    # Write your code here   
def topolgical(graph,src,visited,st): 
   
    visited[src]=True

    for e in graph[src]:
        if visited[e.nbr]==False:
            topolgical(graph,e.nbr,visited,st)
    st.append(src)
if __name__ == "__main__":
    main()