def climbingLeaderboard(scores, alice):
    aliceranks=[]
    ranks=[]
    prev=-1
    for x in scores:
        if x!=prev:
            ranks.append(x)
        prev=x

    maxrank=len(ranks)
    for x in alice:
        for y in ranks[::-1]:
            if x<y:
                aliceranks.append(ranks.index(y)+2)
                break
            if x==y:
                aliceranks.append(ranks.index(y)+1)
                break    
    return aliceranks


scores=[100,100,50,50,40,40,20,10]
alice=[5,25,50,120]

print(climbingLeaderboard(scores,alice))
