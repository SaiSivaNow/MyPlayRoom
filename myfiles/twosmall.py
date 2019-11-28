


def findnsmall(ds):
    a=10000
    b=10000
    for x in ds:
        if x <a:
            a=x
        elif x<b  and x!=a:
            b=x
    return (a,b)



print(findnsmall([12, 13, 1, 10, 34, 1]))
