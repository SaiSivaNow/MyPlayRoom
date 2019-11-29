input().split(' ')
hap = 0
a = input().split()
b = input().split()
c = input().split()

print(a)
print(b)
print(c)

for x in a:
    if x in a:
        hap +=1
    if x in b:
        hap -=1
        
print(hap)
