from collections import defaultdict
from queue import Queue
import sys
class SubSet:
    def __init__(self,parent,rank):
        self.parent=parent
        self.rank=rank
        

class Node:
    def __init__(self,des,weight):
        self.des=des
        self.weight=weight

    def __str__(self):
        return '--('+str(self.weight)+')-->'+ str(self.des)

class Graph:
    def __init__(self,dirc=False):
        self.mainlist=defaultdict(list)
        self.graph=[]
        self.dirc=dirc

    def addEdge(self,src,dst,weight=1):
        self.graph.append([src,dst,weight])
        if not self.dirc :
            self.mainlist[src].append(Node(dst,weight))
        else:
            self.mainlist[dst].append(Node(src,weight))
            self.mainlist[src].append(Node(dst,weight))

            
    '''Depth First Search'''
    def DFS(self,src):
        print('DFS Started')
        visited=[False]*(len(self.mainlist)+1)
        self.DFSUtil(src,visited)

    def DFSUtil(self,src,visited):

        visited[src]=True
        print(src)
        for x in self.mainlist[src]:
            if visited[x.des]==False:
                self.DFSUtil(x.des,visited)
    '''Breadth(Level) First Search'''
    def BFS(self,src):
        print('BFS Started')
        visited=[False]*(len(self.mainlist)+1)
        self.BFSUtil(src,visited)

    def BFSUtil(self,src,visited):
        q=Queue()
        q.put(src)
        visited[src]=True
        while not q.empty():
            y=q.get()
            print(y)
            for x in self.mainlist[y]:
                if visited[x.des]==False:
                    q.put(x.des)
                    visited[x.des]=True
                    
        
    def print(self):
        for y in self.mainlist:
              print(y,*self.mainlist[y])
              
    '''Kruskal's Minimum Spanning Tree'''
    def kruskalMST(self):
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key= lambda item:item[2])

        subsets=[]
        for z in range(0,len(self.mainlist)+1):
            subsets.append(SubSet(z,0))

        while len(result)<len(self.mainlist):
           u,v,w=self.graph[i]
           i=i+1
           x=self.findparent(subsets,u)
           y=self.findparent(subsets,v)
           if(x!=y):
               result.append([u,v,w])
               self.union(subsets,x,y)
               
        for x in result:
            
            print(*x)
            
            
    '''Disjoint Set DS parent'''    
    def findparent(self,subsets,x):
        if(subsets[x].parent==x):
            return  x
        else:
            return self.findparent(subsets,subsets[x].parent)

    ''' Union operation on two subsets'''
    def union(self,subsets,x,y):
        xrank=subsets[x].rank
        yrank=subsets[y].rank
        if xrank<yrank:
            subsets[x].parent=y
        elif xrank>yrank:
            subsets[y].parent=x
        else:
            subsets[y].parent=x
            subsets[x].rank+=1

    '''Djkstra's shortest path algorithm'''        

    def dijkstra(self,src):

        dist=[sys.maxsize]*(len(self.mainlist)+1)
        sptSet=[False]*(len(self.mainlist)+1)
        dist[src]=0

        for i in range(len(self.mainlist)):
            u = self.minDistance(dist,sptSet)
            sptSet[u]=True;
            for x in self.mainlist[u]:
                if sptSet[x.des]==False and dist[x.des]>dist[u]+x.weight:
                    dist[x.des]=dist[u]+x.weight
                    sptSet[x.des]=True

        for x,y in enumerate(dist):
            print(x,':',y)

    def minDistance(self,dist,sptSet):
        mini=sys.maxsize
        minindex=0
        for x in range(len(dist)):
            if sptSet[x]==False and dist[x]<mini:
                minindex=x
                mini=dist[x]
        return minindex        

        
            
        
        

g=Graph()

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.dijkstra(2)
g.print()
g.kruskalMST()
g.DFS(2);
g.BFS(2);
        
