


import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def is_fit(total,n,avail,chain):
    if total != n:
        return False
    for x in avail:
        if compare(x,chain):
            return False
    avail.append(chain)
    return True


def getWays(n, c):

    total=0
    count=0
    avail=[]
    chain=[]
    find_fit(count,total,n,c,avail,chain)
    print(avail)
    print(len(avail))

def find_fit(count,total,n,c,avail,chain):

    flag=True

    while flag:
        for x in c:
            flag=False
            newtotal=total+x
            newchain=[x for x in chain]
            newchain.append(x)
            if is_fit(newtotal,n,avail,newchain):
                count+=1
            if newtotal>=n:
                continue
            total=newtotal
            flag=True
            

a=[int(x) for x in '49 22 45 6 11 20 30 10 46 8 32 48 2 41 43 5 39 16 28 44 14 4 27 36'.split(' ')]

#print(a)    
getWays(3,[1,2,3])        
