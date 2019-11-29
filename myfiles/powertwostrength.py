

def twoTwo(a):

    count = 0
    strlen = len(a)
    for x in range(0,strlen):
        prevint = [0]
        for y in range(x+1, strlen+1):
            if ispoweroftwo(prevint,int(a[y-1]),a[x]):
                count+=1

    return count

    

def ispoweroftwo(prevint,val,full):
   
    if full == '0':
        x = 0
    else :
        x = prevint[0]*10+val
        prevint[0]=x
    return (x and (not(x & (x - 1))) )


print(twoTwo('023223'))

