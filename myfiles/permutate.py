

def permute(string,curr,n):


    if curr>=n:
        print(string)
        return

    for x in range(curr,n):
        string[curr],string[x]=string[x],string[curr]
        permute(string,curr+1,n)
        string[curr],string[x]=string[x],string[curr]


permute([x for x in 'ABCA'],0,4)
