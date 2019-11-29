

def solver(s,c=23,totalcount=1):
    if(s==''):
        return 0
    count=0
    flag=True
    l=c
    prevcount=1
    while l<len(s):
        flag=False        
        if ord(s[l+1])==ord(' '):
            count+=1
            l=l+c+1
            if len(str(count))>totalcount :
                return solver(s,c-1,totalcount+1)
            if len(str(count))> prevcount:
                c=c-1
                prevcount+=1
        else :
            l=l-1
        
        
        
           
            
    if flag:
        count+=1
        
    if(s[l-24:len(s)]!='') and not flag:
        count+=1
    

    return count

n=int(input())
while n>0:
    print(solver(input()))
    n=n-1

