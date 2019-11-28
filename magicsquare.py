

def formingMagicSquare(s):
    num=[[x,0] for x in range(1,10)]
    print(num)
    for x in s:
        for y in x:
            num[y-1][1]+=1

    numsort=sorted(num,key = lambda x:x[1])

    miss=[]
    dup=[]
    for x in numsort:
        if x[1]==0:
            miss.append(x)
        if x[1]>1:
            dup.append(x)

    cost=0
    print(miss)
    print(dup)
    for x in range(len(miss)-1,-1,-1):
        cost+=abs(miss[x][0]-dup[x][0])
        
    return cost       
            
    
        
        
s=[[4,9,2],[3,5,7],[8,1,5]]

print(formingMagicSquare(s))
