

def backtrack(board,col,dim):

    if col>=dim:
        return True
    for x in board:
        print(x,'\n')

    print('----------------')

    for x in range(dim):

        if not isAttack(x,col,board):

            board[x][col] = 1

            if(backtrack(board,col+1,dim)):
                return True

            board[x][col] = 0
            
    return False

    
                    

def isAttack(x,y,twoD):
    for a in  range(0,len(twoD)):
        for b in range(0,len(twoD)):
            if (a!=x or b!=y) and((a+b)==(x+y)or (a-b)==(x-y))and twoD[a][b]==1:
                return True

            if a==x and b!=y and twoD[a][b]==1:
                return True

            if b==y and a!=x and twoD[a][b]==1:
                return True

    return False


def solver(n):
    twoD=[]
    for x in range(0,n):
        a = []
        for y in range(0,n):
            a.append(0)
        twoD.append(a)
    backtrack(twoD,0,n)
    return twoD
            


for  x in solver(4):
    print(x,'\n')
