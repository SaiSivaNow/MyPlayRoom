


def response():
    res = {}
    with open(r'C:\Users\Sai Siva\Documents\answer.txt') as file:
        lines = file.readlines()
        options =[]
        for  line in lines:
            currline = line.split(':')
            if 'Question ID' in currline[0]:
                last = currline[1].strip()
                res[last]=None
            if 'Options' not in currline[0].split(' ')[0] and 'Option' in currline[0].split(' ')[0]:
                options.append(currline[1].strip())
            if len(currline) == 2 and '--' in currline[1]:
                options=[]
                continue
            if 'Chosen Option' in currline[0] :
                res[last]=options[int(currline[1].strip())-1]
                options=[]
            
    return res         
            



def answer():
    ans={}
    with open(r'C:\Users\Sai Siva\Documents\correct.txt') as file:
        lines = file.readlines()
        m=[]
        p=[]
        c=[]
        for line in lines:
            currline = line.split(' ')
            if len(currline) == 5 and 'Paper' in currline[0]:
                answer = currline[4].split('\t')
                if 'M' in answer[0]:
                    m.append(answer[1])
                if 'P' in answer[0]:
                    p.append(answer[1])
                if 'C' in answer[0]:
                    c.append(answer[1])
                ans[answer[1]]=answer[2]
    return (m,p,c,ans)             

res = response()
m,p,c,ans= answer()
count = 0
maths = 0
chem = 0
phy = 0
for x,y in res.items():
    attempt = sum([1 if x is not None else 0 for x in res.values()])
    if y is None:
        continue
    if y == ans[x]:
        if x in m:
            maths+=1
        elif x in p:
            phy+=1
        else:
            chem+=1
        count+=1
print(maths,phy,chem,attempt,count)
