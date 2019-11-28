import copy
n=int(input())

while n>0:
    lannisters,hours=[int(x) for x in input().split()]
    pos=[int(x) for x in input().split()]
    for y in range(0,hours):
        positions=copy.deepcopy(pos)
        for x in range(1,lannisters-1): 
            positions[x]=pos[x-1]&pos[x+1]

        positions[x]=pos[x+1]
        positions[x]=pos[x-1]             
        pos=copy.deepcopy(positions)
    n=n-1
    print(*pos,end=' ')
    print()
    
