#code
def solve(arr):
    result = [arr[0]]
    flag = False
    for x in range(1,len(arr)):
        print(arr[x],result[-1])
        if arr[x] == result[-1]:
            flag =  True
            continue
        else:
            if flag:
                print('del',result[-1])
                del result[-1]
            flag = False
            result.append(arr[x])
    if flag:
        del result[-1]
    curr = ''.join(result)
    if curr==arr:
        return curr
    else:
        return solve(curr)
    
test = int(input())


for x in range(0,test):
    arr = input().strip()
    print(solve(arr))
