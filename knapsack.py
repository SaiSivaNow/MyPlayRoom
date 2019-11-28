def optimum(subweights,mydict,weight):
    value=0
    opti=0
    for x in subweights:
        value+=x
        opti+=mydict[x]

    if(value<=weight):
        return opti
    return 0
        
            
def biggest(maxi,a,b):
    lst=[maxi,a,b]
    maxer=0
    for x in lst:
        if x >maxer:
            maxer=x

    return maxer

def solution(maxi,subweights,values,weights,weight,mydict):

    if(len(subweights)==len(values)):
        return optimum(subweights,mydict,weight)
    const=subweights
    for x in weights:
        if not x in subweights:
            const.append(x)
        else:
            continue
        a=optimum(const,mydict,weight)
        b=solution(maxi,const,values,weights,weight,mydict)
        maxi=biggest(maxi,a,b)
        const.remove(x)
        
    return maxi

values=[60,100,120,30]
weights=[10,20,30,45]
mydict= {10:60 ,20:100,30:120,45:30}
weight=65
maxi=0

print(solution(maxi,[],values,weights,weight,mydict))
