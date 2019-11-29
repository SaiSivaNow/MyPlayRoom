import queue
class Graph:
    
    def __init__(self,v):
        self.adjList = [[0]*v for x in range(0,v)]
        
    def add(self,x,y):
        self.adjList[x][y]+=1


def solve(graph,src,des):
    
    paths=0
    visited = [False]*len(graph.adjList)
    q = queue.Queue()
    q.put(src)
    visited[src] = True
    while not q.empty():
        curr = q.get()
        print(curr,'-->')
        for x in range(0,len(graph.adjList[curr])):
            flag = False
            while graph.adjList[curr][x]!=0 and not visited[x]:
                print(x)
                if x == des:
                    paths+=1
                if x!=des:
                    q.put(x)
                graph.adjList[curr][x]-=1
                flag = True
            if flag and x!=des:
                visited[x] = True
            if flag and x==des:
                graph.adjList[curr][x]=1
                
    return paths
    
def read_input():
    test = int(input())
    for x in range(0,test):
        m,n = [int(a) for a in input().strip().split()]
        graph = Graph(m)
        count = 0
        temp = []
        for y in input().strip().split():
            temp.append(int(y))
            count+=1
            if count==2:
                graph.add(temp[0],temp[1])
                temp = []
                count = 0
        src,dest = [int(x) for x in input().strip().split()]
        print(solve(graph,src,dest))
read_input()
