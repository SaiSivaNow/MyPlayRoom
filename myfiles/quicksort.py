
def partition(mylist,i,k):
    pivot=mylist[k]
    # j holds the pointer to the last element which is smaller than the pivot
    j=i-1 
    for x in range(i,k):
        if mylist[x]>=pivot:
            # Advances the pointer only the last iterated element is smaller than pivot
            j=j+1
            # Exchanges the next found small element  with element next to the last iterated smaller element
            mylist[j],mylist[x]=mylist[x],mylist[j]
            
    mylist[j+1],mylist[k]=mylist[k],mylist[j+1]

    return j+1





def quicksort(count,mylist,i,k):
        count[0]=count[0]+1

        if i<k:
            j=partition(mylist,i,k)
            quicksort(count,mylist,i,j-1)
            quicksort(count,mylist,j+1,k)





count=[0]
mylist=[1,3,4,6,5,7]
quicksort(count,mylist,0,len(mylist)-1)
print(mylist,count)
