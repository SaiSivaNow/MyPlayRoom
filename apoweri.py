def solve(a):
    if len(a) == 0:
        return None
    if len(a) ==1:
        return a
    superfinal=[]
    for x in range(1,len(a)):
        first = a[0:x]
        resa = solve(first)
        res = solve(a[x:len(a)])
        final = []
        
        for sub in res:
            for b in resa:
                final.append(b+' '+sub)
        superfinal+=final
    superfinal.append(a)
    return superfinal
        
    pass
def read_input():
    test = int(input())
    for x in range(0,test):
        a = input()
        res = solve(a)
        for y in range(0,len(res)):
            if res[y] not in res[0:y]:
                print('('+res[y]+')',end='')
                
        print()
            
        
read_input()
