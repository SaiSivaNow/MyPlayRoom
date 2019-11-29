
binaries=[x for x in input().split(',')]

strlist=[];

for binary in binaries:
    intd=int(binary,2)
    if not intd%5:
        strlist.append(binary)
    else:
        continue

print(','.join(strlist))
