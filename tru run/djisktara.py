import threading 
import queue


class pair:
    def __init__(self,v,psf,wt):
        self.v=v
        self.psf=psf
        self.wt=wt
    def __eq__(self, other):
        return self.wt == other.wt
class Edge:
    def __init__(self,src,nbr,wt):
        self.src = src
        self.nbr = nbr
        self.wt=wt



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
        wt=int(lines[2])
        e1 = Edge(v1 ,v2 ,wt)
        e2 = Edge(v2 ,v1 ,wt)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)
        
    src = int(input())
    visited=[False]*vtces
    q=queue.PriorityQueue()
    #write your code here
    q.put(pair(src,str(src)+"",0))
    while q.size()>0:
        r=q.get()

        if visited[r.v]==True:
            continue
        visited[r.v]=True
        print(str(r.v)+" via "+r.psf+" @ "+str(r.wt))

        for e  in graph[r.v]:
            if visited[e.nbr]==False:
                q.append(pair(e.nbr,r.psf+str(e.nbr),r.wt+e.wt))

   
if __name__ == '__main__':
    main()
      
    