
def get_keys(key):
    localkeys=[]
    for x in key.split(' '):
        localkeys.append(x)
    for x in key.split('@'):
        localkeys.append(x)
    for x  in key.split('.'):
        localkeys.append(x)
    for x  in key.split('-'):
        localkeys.append(x)
    return localkeys
    



def func():
    table = {}
    important = set()
    total = 0
    atm  = 0
    for x in range(3,0,-1):
        path =r'C:\Users\Sai Siva\Desktop\HDFC '+str(x)+'.txt'
        with open(path) as f:
            flag = True
            count = 2
            for line in f.readlines():
                trans = line.split(',')
                if count !=0:
                    count-=1
                    continue
                keys = trans[1].strip()
                superkeys = []
                for x in keys.split(' '):
                    for y in get_keys(x):
                        superkeys.append(y)

                for x in keys.split('@'):
                    for y in get_keys(x):
                        superkeys.append(y)

                for x in keys.split('.'):
                   for y in get_keys(x):
                        superkeys.append(y)

                for x in keys.split('-'):
                    for y in get_keys(x):
                        superkeys.append(y)
                trans[3]=trans[3].strip().split('.')[0].replace(',','')
                trans[4]=trans[4].strip().split('.')[0].replace(',','')
                done={}
                good = True
                res = 0
                curr =0
                try:
                    res = int(trans[3].strip())
                    curr= int(trans[4].strip())
                except ValueError:
                    good = False
                    #print(trans)
                if good and curr >1000 and ('SALARY' in trans[1] or 'FULL' in trans[1] or'AMAZON' in trans[1] or curr >100000):
                    total+=curr
                    #print(trans[0]+" "+trans[1]+" "+str(curr))
                if ('ATW' in trans[1] or 'NWD' in trans[1]) and 'BANGALORE' not in trans[1]:
                    #print('W'+trans[0]+" "+trans[1]+" "+str(res))
                    atm+=res
                if '512967XXXXXX9319' in trans[1] and 'CENTRAL' in trans[1]:
                    print('W'+trans[0]+" "+trans[1]+" "+str(res))
                for x in superkeys:
                    if not good:
                        break
                        
                    if x not in table and x not in done:
                        try:
                            table[x]= res
                            done[x]=''
                            important.add(x)
                        except ValueError:
                            print(trans)
                    elif x not in done:
                        try:
                            table[x]+=res
                            done[x]=''
                        except ValueError:
                            print(trans)

    print('INFLOW : '+str(total))
    print('CASH : '+str(atm))
    with open(r'C:\Users\Sai Siva\Desktop\output.txt','w+') as out:
        for x in important:
            if x in table:
                if x =='ZERODHA' or 'HIMADRI'==x or x=='PAYTM' or 'UPI'== x or x=='SURI' or x=='N SURI BABU' or 'UBER'==x or x=='FOOD' or x=='AMAZON' or x=='RAPIDO' or x=='POS' or x=='NESTAWAY' or x=='IMPS':
                    print(x+" "+str(table[x]))
                out.write(str(x)+" "+str(table[x])+" "+"\n")
    
                        

                
                
                
                

func()
                
