a = set()
def getSplit(S):
    print(S)
    global a
    for x in ['.','?','!']:
        res = S.split(x)
        if len(res)==1 and res[len]:
            a.add(res[0].strip())
        else:
            for y in res:
                getSplit(y)
        


def solution(S):
    # write your code in Python 3.6
    high =0
    getSplit(S)
    for x in a:
        print(x)
        high = max(len(x.split(' ')),high)
        
    
    return high
