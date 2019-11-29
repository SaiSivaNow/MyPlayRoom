def resolve(a,b,x,y):
        
    while x<len(a) and y<len(b):
        
        if ord(a[x])<ord(b[y]):
            return 1
        if ord(a[x])>ord(b[y]):
            return 2
        x+=1
        y+=1
        
    if x==len(a) and y==len(b):
        return 1
    
    if x==len(a) and y!=len(b):
        for l in b[y:len(b)]:
            if ord(a[x-1])>ord(l):
                return 2
            if ord(a[x-1])<ord(l):
                return 1
    if y==len(b) and x!=len(a):
        for l in a[x:len(a)]:
            if ord(b[y-1])>ord(l):
                return 1
            if ord(b[y-1])<ord(l):
                return 2
    
        
        
        

# Complete the morganAndString function below.
def morganAndString(a, b):
    c=[]
    x=0
    y=0
    while x<len(a) and y<len(b):
        if ord(a[x])<ord(b[y]):
            c.append(a[x])
            x+=1
        elif ord(a[x])>ord(b[y]):
            c.append(b[y])
            y+=1
        else:
            if resolve(a,b,x+1,y+1)==1:
                c.append(a[x]);
                x+=1
            else:
                c.append(b[y])
                y+=1
            

    if x==len(a):
        for l in b[y:len(b)]:
            c.append(l)
    if y==len(b):
        for l in a[x:len(a)]:
            c.append(l)
        
    return ''.join(c)
