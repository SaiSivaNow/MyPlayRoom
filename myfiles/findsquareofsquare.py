import math

def decompose(n):
    # your code
    a = []
    find_square(n**2,n-1,a)

    b = []

    for x in range(len(a)-1,-1,-1):
        b.append(a[x])
    return b
    
def find_square(rem,init,a):
    while init>0:
        rem -= init**2
        a.append(init)
        if rem == 0:
            return True
        elif rem >0:
            b = init-1
            if find_square(rem,b,a):
                return a            
        a.remove(init)
        rem+=init**2
        init-=1
    return False

print(decompose(50))
