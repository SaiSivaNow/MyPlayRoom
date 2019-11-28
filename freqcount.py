
def rotate(arr):
    
    temp = []
    temp= [arr[-1]]
    temp+= arr[0:len(arr)-1]
    return temp

def solve(arr):
    if len(arr) == 0:
        return arr[0]
    flag = [False for x in arr]
    count = 0
    index = 0
    elem = len(arr)
    curr = len(arr)-2
    loop = True
    while loop:
        flag[curr] = True
        print(arr[curr])
        index+=curr
        count+=1
        if count == len(arr)-2:
            break
        moved = 0
        while moved<3:
            curr-=1
            if curr<0:
                loop = False
            if not flag[curr]:
                moved+=1
                
    for x in range(0,len(flag)):
        if not flag[x]:
            print(arr[x])
            break
    
def read_input():
    test = int(input())
    for x in range(0,test):
        n = int(input())
        arr = [int(y) for y in input().strip().split()]
        print(solve(arr))
read_input()
