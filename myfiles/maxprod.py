#code
import  sys

def solve(arr, inp):
    
    max_so_far = 1
    min_so_far = -1
    max_prod = 1
    for x in range(0,len(arr)):
        
        if arr[x] > 0:
            print('P',max_so_far, min_so_far)
            max_so_far =max_so_far *arr[x]
            min_so_far = min_so_far * arr[x] if min_so_far <-1 else -1
            max_prod =  max(max_prod, max_so_far)
            print('P-End {0}'.format(arr[x]),':',max_so_far, min_so_far)
        if arr[x] < 0:
            print('N',max_so_far, min_so_far)
            max_prod =  max(max_prod, min_so_far*arr[x])
            prev_min = min_so_far
            if max_so_far > 0:
                min_so_far = max_so_far *arr[x]
            if prev_min < 0:
                max_so_far  = prev_min*arr[x]
            print('N -End {0}'.format(arr[x]),':',max_so_far, min_so_far)

        if arr[x] == 0:
            min_so_far = -1
            max_so_far =1


    
    return max_prod
    
    
test = int(input())


for x in range(0,test):
    inp = [int(y) for y in input().strip().split()]
    arr = [int(x) for x in input().strip().split()]
    print(solve(arr,inp))
