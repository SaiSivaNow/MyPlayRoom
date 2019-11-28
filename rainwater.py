#code

def find_volume(chunks,walls):
    volume = 0
    i = 0
    while i<len(chunks)-1:
        start = chunks[i]
        end = chunks[i+1]
        for x in range(start+1,end):
            volume+=(walls[start]-walls[x])
        i+=1
    return volume

test = int(input())

while test>0:
    
    n = int(input())
    walls = [int(x) for x in input().split(' ')]
    

    max_till = walls[0]
    chunks=[0]
    volume = 0
    max_till = walls[0]
    for x in range(1,n):
        if max_till<walls[x]:
            max_till = walls[x]
            chunks.append(x)
    volume = find_volume(chunks,walls)
    
    if chunks[len(chunks)-1] == len(walls)-1:
        print(volume)
        continue
    new_walls = walls[chunks[len(chunks)-1]:]
    new_walls = list(reversed(new_walls))
    max_till = new_walls[0]
    chunks = [0]
    for x in range(1,len(new_walls)):
        if max_till<new_walls[x]:
            max_till = new_walls[x]
            chunks.append(x)
    new_volume = find_volume(chunks,new_walls)
    print(volume+new_volume)
    test-=1
    
