#code
import sys
def form_paren(table,a,b,c):
    print(a,b,c)
    first=''
    if a==b or a+1==b:
        if a==b:
            first = chr(ord('A')+a)
        else:
            first = chr(ord('A')+a)+chr(ord('A')+b)
    else:
        ind = table[a][b][1]
        if len(ind)!=0:
            first = form_paren(table,*ind)
            
    second = ''
    if b==c:
         if b==c:
            first = chr(ord('A')+b)
         else:
            first = chr(ord('A')+b)+chr(ord('A')+c)
    else:
        ind= table[b+1][c][1]
        if len(ind) != 0:
            second =form_paren(table,*ind)
    return '('+first+second+')'
    
def solve(arr):
    
    table = [[[0,[]] for _ in range(0,len(arr))] for _ in range(0,len(arr))]
    
    for sub in range(2,len(arr)):
        for i in range(0,len(arr)-sub):
            j = i+sub-1
            paren = []
            min_op = sys.maxsize
            for k in range(i,j):
                op = (arr[i]*arr[k+1]*arr[j+1])+table[i][k][0]+table[k+1][j][0]
                if op < min_op:
                    min_op = op
                    paren = [i,k,j]
            table[i][j][0] = min_op
            table[i][j][1] = paren
    a,b,c = table[0][len(arr)-2][1]
    print(form_paren(table,a,b,c))
    
                
def read_input():
    test = int(input())
    for x in range(0,test):
        n = int(input())
        arr = [int(y) for y in input().strip().split()]
        solve(arr)
read_input()
