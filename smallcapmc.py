import requests
from lxml import html
from bs4 import BeautifulSoup
import operator
import csv

def getportifolio(companies,url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    flag=True

    for table in soup.findAll("table", attrs={'class':'tblporhd'}):
        for tr in table.findAll('tr'):
            company=''
            shares,value,i=0,0,0
            for td in tr.findAll('td'):
                for a in td.findAll('a'):
                    company=a.text
                if i>3 :
                    break
                if i==2 :
                    shares=td.text.replace(',','')
                    if shares!='-':
                        shares=float(shares)
                if i==3 :
                    value=td.text.replace(',','')
                    if value!='-':
                        value=float(value)
                i+=1
                
            if company in companies:
                if type(shares)==type(2.0)and type(shares)==type(companies[company][0]):
                    shares=shares+float(companies[company][0])
                if type(value)==type(3.0) and type(shares)==type(companies[company][1]):
                    value=float(value)+float(companies[company][1])
                number=1+companies[company][2]
                companies[company]=[shares,value,number]
            else:
                companies[company]=[shares,value,1]

                
        del(companies[''])
        break
                    
                    
                



def getMF(urlList,url):
    r=requests.get(url)
    print(r.content)
    soup=BeautifulSoup(r.content,"html.parser")

    for mf in soup.findAll("a",attrs={'class':'robo_medium'}):

        link=mf['href']
        urlList.append(link.split('/')[4])

        
    
            
    

urlList=[]

getMF(urlList,'http://www.moneycontrol.com/mutual-funds/performance-tracker/returns/large-cap.html')


companies={}
print(len(urlList))
i=0
for x in urlList:
    getportifolio(companies,'http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/'+x)
    print(x)
    print(i)
    i+=1


print(companies)

with open('largecap.csv','w') as mfcomp:
    writer = csv.writer(mfcomp,lineterminator='\n')
    writer.writerow(['Company','Shares','Value','Frequency'])
    for x,y in companies.items():
        writer.writerow([x]+y)



