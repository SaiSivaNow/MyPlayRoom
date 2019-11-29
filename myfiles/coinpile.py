#code
def solve(arr, inp):
    
    arr = sorted(arr)
    last = arr[-1]
    count=0
    print(arr)
    for x in range(len(arr)-1,-1,-1):
        if arr[x]-arr[0]>inp[1]:
            last = (x,arr[x])
            count+=(arr[x]-(arr[0]+inp[1]))
    print(last)
    itemcount = len(arr)
    min_count =  count
    for x in range(0,len(arr)):
        if last-arr[x]>inp[1]:
            frontcount+=arr[x]
    print(frontcount)
    print(min(count,frontcount))
            
    
    
test = int(input())


for x in range(0,test):
    inp = [int(y) for y in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    solve(arr,inp)
