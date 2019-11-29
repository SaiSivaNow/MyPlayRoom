def maxHeapify(mylist,i,n):
    l= 2*i+1
    r=l+1
    largest=i
    if l<n and mylist[l]>mylist[largest]:
        largest=l
    if r<n and mylist[r]>mylist[largest]:
        largest=r
    if  largest != i:
        mylist[largest],mylist[i]=mylist[i],mylist[largest]
        maxHeapify(mylist,largest,n)
        
    



def buildMaxHeap(mylist):
    #Performing Max Heapify from bottom up approach
    for i in range(len(mylist)//2,-1,-1):
        maxHeapify(mylist,i,len(mylist))





def heapSort(mylist):

    buildMaxHeap(mylist)
    for x in range(0,(len(mylist))):
        mylist[0],mylist[len(mylist)-x-1]=mylist[len(mylist)-x-1],mylist[0]
        print(mylist)
        maxHeapify(mylist,0,len(mylist)-x-1)




mylist=[1,2,3,4,5,6]

heapSort(mylist)
        
print(mylist)





        
    



    
    
    
    
