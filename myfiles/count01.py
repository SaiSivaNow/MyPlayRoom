


def func(n):
    bi= bin(n)
    bi=bi[2:]
    countzero=0
    countone=0
    if bi[0]=='1':
        posprod =1
        negprod =0
        evesum=0
        oddsum=1
        tot=1
        pro=1
        countone+=1
    else:
        posprod=0
        negprod=1
        evesum=1
        oddsum=0
        tot=0
        pro=-1
        countzero+=1
    for x in range(1,len(bi)):
        x=bi[x]
        if x=='1':
            tot+=1
            countone+=1
        if x=='0':
            pro*=-1
            countzero+=1

        if tot%2==1:
            countone+=oddsum
            oddsum+=1
        else:
            countone+=evesum
            evesum+=1
        if pro<0:
            countzero+=posprod
            negprod+=1
        else:
            countzero+=negprod
            posprod+=1
            
    print(countzero, countone)
def fun(n):
    countzero=0
    countone=0
    bi= bin(n)
    bi=bi[2:]
    print(bi)
    for x in range(2,len(bi)+1):
        for y in range(0,len(bi)-x+1):
            zer=0
            one=0
            for z in bi[y:y+x]:
                if z=='0':
                    zer+=1
                else:
                    one+=1
            if zer%2==1:
                countzero+=1
            if one%2==1:
                countone+=1
            print(bi[y:y+x])
    for x in bi:
        if x=='0':
            countzero+=1
        else:
            countone+=1
    print(countzero,countone)

    

func(10)
fun(17)
    
