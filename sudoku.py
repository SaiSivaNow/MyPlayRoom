def heapify(arr,parent,total):
    i = parent
    left = 2*parent+1
    right = 2*parent+2
    if left < total and arr[left]<arr[parent]:
        parent = left
    if right< total and arr[right]<arr[parent]:
        parent = right
    if parent !=i:
        temp = arr[i]
        arr[i] = arr[parent]
        arr[parent] =temp
        heapify(arr,parent,total)

def solve(arr):
    for x in range(len(arr)//2,-1,-1):
        heapify(arr,x,len(arr))
    print(arr)
    elem = len(arr)
    cost =0
    for x in range(0, elem-1):
        print(arr)
        a = arr[0]
        arr[0]=arr[elem-(x+1)]
        heapify(arr,0,elem-(x+1))
        b = arr[0]
        arr[0] = arr[elem-(x+2)]
        heapify(arr,0,elem-(x+2))
        print(a+b)
        cost+= (a+b)
        arr[elem-(x+2)]=arr[0]
        arr[0] = a+b
        heapify(arr,0,elem-(x+2))
    return cost
def read_input():
    test = int(input())
    for x in range(0,test):
        n = int(input())
        arr = [int(y) for y in input().strip().split()]
        print(solve(arr))
read_input()
