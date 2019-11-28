

def sort(ds,start,end):
    if start<end:
        pivot=findpivot(ds,start,end)
        sort(ds,start,pivot-1)
        sort(ds,pivot+1,end)


def findpivot(ds,start,end):
    current=start
    while current<end:
        if ds[current]<ds[end]:
            current+=1
        else :
            break

    ds[current],ds[end]=ds[end],ds[current]

    return current


ds=[1,2,3,4,5]
sort(ds,0,len(ds)-1)
print(ds)
        
        
    
    
    
    
