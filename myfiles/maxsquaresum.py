
a =[int(x) for x in input().split(' ')]

maxofgiven=[]
check = a[1]
for x in range(0,a[0]):
    maxo = -1
    for y in input().split(' '):
        y_int = int(y)
        mod = y_int%check
        if mod > maxo:
            maxo = mod
    maxofgiven.append(maxo)
maxtotal = 0
for x in maxofgiven:
    maxtotal += x**2

print(maxtotal)
