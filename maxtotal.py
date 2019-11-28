
n=int(input())
checkpoints=[int(x) for x in input().split()]

print(checkpoints)
maxtotal=0
for i in range(0,n):
    total=sum(checkpoints[0:i+1])*sum(checkpoints[i+1:])
    if total>maxtotal:
        maxtotal=total
    
    
    
print(maxtotal)
