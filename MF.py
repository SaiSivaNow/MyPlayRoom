import requests
from lxml import html
from bs4 import BeautifulSoup
import operator
import csv

def getportifolio(companies,url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    flag=True

    for table in soup.findAll("table", attrs={'class':'table table-striped table-hover table-bordered'}):
        if(flag):
            flag=False
            continue
        headdict={}
        for thead in table.findAll('thead'):
            for cname in thead.text.split('\n'):
                if len(cname)>2:
                    headdict[cname]=[]
        keys=list(headdict.keys())
        
        for tr in table.findAll('tr'):
            i=0
            for td in tr.findAll('td'):
                headdict[keys[i]].append(td.text.split('\r\n')[1].strip(' '))
                i+=1
                
            
        for x in headdict[keys[0]]:
            if x in companies:
                companies[x]+=1
            else:
                companies[x]=1
                



def getMF(urlList,url):
    r=requests.get(url)

    soup=BeautifulSoup(r.content,"html.parser")

    for table in soup.findAll("table",attrs={'class':'table table-striped table-hover table-bordered'}):
    
        for tr in table.findAll("tr"):
            i=0
            for td in tr.findAll('td'):
                for a in td.findAll('a'):
                    urlList[a.text]=a['href']
            
    

urlList={}
for x in range(1,6):
    getMF(urlList,'https://www.mutualfundindia.com/MF/Return/TopFunds?dataMfiPageIndex='+str(x))
    y=0
    for r,k in urlList.items():
        if y==0:
            y=1
            break
    
companies={}
i=0;
for x,y in urlList.items():
    getportifolio(companies,'https://www.mutualfundindia.com'+y)
    i=i+1

companies_x=sorted(companies.items(),key=operator.itemgetter(1))

with open('company.csv','w') as mfcomp:
    writer = csv.writer(mfcomp,lineterminator='\n')
    for x in companies_x:
        a,b=x
        writer.writerow([a,b])
        



