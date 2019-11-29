#code
def solve(arr, inp):
    global lis
    if len(arr) == 1:
        return 1
    localmax =  0
    for x in range(0,len(arr)-1):
        if arr[len(arr)-1]> arr[x]:
            res = 1+solve(arr[0:x+1],inp)
            if res > localmax:
                localmax = res
    
    return localmax
    
test = int(input())


for x in range(0,test):
    inp = [int(y) for y in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    print(solve(arr,inp))
