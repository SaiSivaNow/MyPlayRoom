import queue
mini =  1000000000000000000
def get_moves():
    
    pass

def solve(board,start,target,n):
    global mini
    if target==start:
        return 0
    if n==2:
        return 1
    curr = start
    
    if not (0<curr[0]<=n and 0<curr[1]<=n):
            return
    for x in [+2,-2]:
        for y in [+1,-1]:
            a = curr[0]+x
            b = curr[1]+y
            if a== target[0] and b == target[1]:
                board[a][b]=1+board[curr[0]][curr[1]]
                if mini > board[a][b]:
                    mini = board[a][b]
                continue
            if 0<a<=n and 0<b<=n:
                if 1+board[curr[0]][curr[1]]<board[a][b]:
                    board[a][b]=1+board[curr[0]][curr[1]]
                    solve(board,[a,b],target,n)
            a = curr[0]+y
            b = curr[1]+x
            if a== target[0] and b == target[1]:
                board[a][b]=1+board[curr[0]][curr[1]]
                if mini > board[a][b]:
                    mini = board[a][b]
                continue
            if 0<a<=n and 0<b<=n:
                if 1+board[curr[0]][curr[1]]<board[a][b]:
                    board[a][b]=1+board[curr[0]][curr[1]]
                    solve(board,[a,b],target,n)
    
def read_input():
    test = int(input())
    for x in range(0,test):
        n = int(input())
        board = [[10000 for x in range(0,n+1)] for y in range(0,n+1)]
        start = [int(x) for x in input().strip().split()]
        target = [int(y) for y in input().strip().split()]
        board[start[0]][start[1]] = 0
        solve(board,start,target,n)
        print(mini)
read_input()
