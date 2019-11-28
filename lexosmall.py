
def getoptimum(mylist,compare,start,ignore):
    minord=compare
    for x in range(len(mylist)-1,start,-1):
        if x not in ignore:
            if ord(minord)>ord(mylist[x]):
                minord=mylist[x]
                tup=(x,mylist[x])

    if minord==compare:
        return None
    else:
        return tup

def getrevoptimum(mylist,compare,start,ignore):
    minord='z'
    for x in range(start,len(mylist)-1):
        if x not in ignore:
            if ord(minord)>ord(mylist[x]):
                minord=mylist[x]
                tup=(x,mylist[x])

    if minord=='z':
        return None
    else:
        print('Last:{0}'.format(tup))
        return tup
    
def solver(mylist,n):
    ignore=[]
    values=[]
    for x in mylist:
        indice=mylist.index(x)
        tup=getoptimum(mylist,x,indice,ignore)
        if tup is not None and n>=2:
            a,b=tup
            print(a,b)
            n-=2
            mylist[mylist.index(x)]=b
            ignore.append(a)
            values.append(x)
        if n==1:
            values.sort()
            tup=getrevoptimum(mylist,values[0],indice+1,ignore)
            if tup is not None:
                a,b=tup
                ignore.append(a)
                values.append(b)
            i=0
            values.sort()
            ignore.sort()
            for x in ignore:
                mylist[x]=values[i]
                i+=1
            break        
        elif n==0:
            i=0
            values.sort()
            ignore.sort()
            for x in ignore:
                mylist[x]=values[i]
                i+=1


mylist= [x for x in 'qghum']
solver(mylist,3)

print(mylist)
                 
