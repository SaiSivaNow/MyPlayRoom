#code

test = int(input())

while test > 0:
    n = int(input())
    temp = [x for x in input().split(' ')]
    prices = []
    for x in temp:
        if x is not '':
            prices.append(int(x))
    
    
    stretch = []
    start = 0
    prev_price = prices[0]
    for x in range(1,len(prices)):
        if prices[x] < prev_price:
            print(prev_price,prices[x])
            stretch.append([start,x-1])
            start = x
        elif x==len(prices)-1:
            stretch.append([start,x])
        prev_price = prices[x]
    for x in stretch:
        if x[0] != x[1]:
            print('('+str(x[0])+' '+str(x[1])+') ',end='')
    print()
    test-=1
        
