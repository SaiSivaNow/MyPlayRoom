

def sort(ds):

    for x in range(1,len(ds)):
        comp=ds[x]
        current=x
        for y in range(x-1,-1,-1):
            if comp<ds[y]:
                current=y
                ds[current+1]=ds[current]
        ds[current]=comp

        

ds=[5,4,3,2,1]
sort(ds)
print(ds)
