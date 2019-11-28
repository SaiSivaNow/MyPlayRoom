from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re,csv
import time
import qextract
from qextract import extractPage

url= 'https://www.quora.com/'
urlList=['https://www.quora.com/topic/Stock-Markets-2','https://www.quora.com/topic/Stocks-financial','https://www.quora.com/topic/Investing','https://www.quora.com/topic/Stock-Market-in-India','https://www.quora.com/topic/Trading-finance]']
driver=webdriver.Firefox()
driver.get(url)
topiclist=[]
for topicrange in range(len(urlList)):
	topicname=re.search(r'topic\/(.*)',str(urlList[topicrange])).group(1)
	topiclist.append(topicname)

# userName=re.search(r'class="regular_login".*?input\sid\=\"(.*?)\".*?name=\"email\"',html).group(2)
# userName1='\''+userName+'\''
element1=driver.find_element_by_xpath("//input[(@name='email') and (@placeholder='Email')]")
element1.send_keys('enter your login id')
element2=driver.find_element_by_xpath("//input[(@name='password') and (@placeholder='Password')]")
element2.send_keys('enter your password')
clicked=0;
while clicked==0:
	try:
		element3=driver.find_element_by_xpath("//input[(@value='Login') and (@type='submit')]")
		element3.click();
		clicked=1;
		time.sleep(1.0)
	except:
		continue;
		
for urlOfTopic in range(len(urlList)):		
	driver.get(urlList[urlOfTopic])
	last_height=0;
	current_height = driver.execute_script("return document.body.scrollHeight")
	while last_height<current_height:
		last_height=current_height
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2.0)
		current_height = driver.execute_script("return document.body.scrollHeight")
		
	html= driver.page_source
	question_url=re.findall(r'question_link(.*?)href=\"(.*?)\"',html)
	print(len(question_url));
	with open(str(topiclist[urlOfTopic])+'.csv','w') as quoraw:
		writer=csv.writer(quoraw,lineterminator='\n')
		for page in range(len(question_url)):
			target_url=url.encode('UTF-8')+question_url[page][1].encode('UTF-8')
			driver.get(target_url)
			page_html=driver.page_source
			pageRow=[target_url]+extractPage(page_html)
			writer.writerow(pageRow)
			# with open(str(page)+'.txt','w') as qwe:  ##wriing page source to text file
				# qwe.write(page_html.encode('UTF-8'))
			time.sleep(2)

#output = number of followers, number of answers, Sum of answer viewers, sum of answer upvotes		
	
#question_link
#answer_permalink	
#FollowSecondaryActionItem ActionItemComponent ItemComponent action_item  ##for follow in question
#answer_count ##for answers in page
#ContentFooter AnswerFooter #for number of views for answer
#class="count" ## for upvotes
