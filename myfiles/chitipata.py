
def distribute(initialamount,portifolio,month):

    portifolio[month][1]=initialamount[0]*5
    for x,y in portifolio.items():
        
        if x!=month:
                
            portifolio[x][0]+=initialamount[0]


    initialamount[0]+=200












initialamount=[8800]

portifolio={1:[0,0,1] ,2:[0,0,2], 3:[0,0,3],4:[0,0,4] ,5:[0,0,5], 6:[0,0,6]}

for x in range(1,7):
    distribute(initialamount,portifolio,x)


print(portifolio)
