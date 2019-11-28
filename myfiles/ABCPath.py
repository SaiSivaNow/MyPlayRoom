



def solver(twoD,a,b):
    maxpath = 0       
    for x,y in getAdj(twoD,a,b):
        path=1+solver(twoD,x,y)
        if(maxpath<path):
            maxpath=path

    return maxpath

def feasible(twoD):
    maxpath = 0
    for x in range(0,len(twoD)):
        for y in range(0,len(twoD[0])):
            if twoD[x][y]=='A':
                path = 1+solver(twoD,x,y)
                if(maxpath<path):
                    maxpath=path

    return maxpath


def getAdj(twoD,a,b):
                   val=ord(twoD[a][b])
                   maxx=len(twoD)
                   maxy=len(twoD[0])
                   tuplist=[]
                   if ((b+1)<maxy) and (val+1==ord(twoD[a][b+1])):
                       tuplist.append((a,b+1))
                   if ((b-1)>0) and (val+1==ord(twoD[a][b-1])):
                       tuplist.append((a,b-1))
                   if ((a-1)>0) and ((b-1)>0) and (val+1==ord(twoD[a-1][b-1])):
                        tuplist.append((a-1,b-1))
                   
                   return tuplist
                                            

print(feasible(["ABC"]))
