import sys
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]

    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptSet=[False]*self.V

        for y in range(self.V):

            u=self.minDistance(dist,sptSet)
            sptSet[u]=True

            for v in range(self.V):
                if self.graph[u][v]>0 and sptSet[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]
                    
        self.printPath(dist)

    def printPath(self,dist):
        for x,y in enumerate(dist):
            print(x,':',y)

    def minDistance(self,dist,sptSet):
        mini=sys.maxsize
        min_index=0
        for x in range(self.V):
            if sptSet[x]==False and dist[x]<mini:
                mini=dist[x]
                min_index=x
                
        return min_index


g  = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];
 
g.dijkstra(0);
