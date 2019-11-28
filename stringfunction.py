

def maxValue(t):

    totallen = len(t)
    funcmax = -1;
    for x in range(0,totallen):
        for y in range(x+1,totallen+1):
            funcvalue = func_sub(t,t[x:y],x,y,totallen)
            if funcvalue>funcmax:
                funcmax = funcvalue
    return funcmax
            

def func_sub(full,sub,x,y,fulllen):

    sublen = y - x
    count = 0
    for x in range(0,fulllen-sublen+1):
        if sub == full[x:x+sublen]:
            count+=1

    return sublen*count
            


print(maxValue('aaaaaa'))
