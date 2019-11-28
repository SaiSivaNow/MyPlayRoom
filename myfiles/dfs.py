import sys

given = 'POON, PLEE, SAME, POIE, PLEA, PLIE, POIN'.split(', ')

dist = [sys.maxsize]*len(given)

word = { k:v for k,v in zip(given, dist) }


def can_reach(a,b):

    count =0
    for x in range(0,len(a)):
        if a[x]!=b[x]:
            count+=1
        if count == 2:
            return False
    return True
    

def find_shortest(src,word):
    
    if src == 'SAME':
        return None
    for x in word.keys():

        if x!=src and can_reach(src,x) and word[src]+1<word[x]:
            print(x)
            word[x]=word[src]+1
            find_shortest(x,word)
            
word['TOON']= 0
find_shortest('TOON',word)
print(word['SAME'])
