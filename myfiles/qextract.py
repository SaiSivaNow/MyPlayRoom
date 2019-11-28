from bs4 import BeautifulSoup as bs
import re
import kcon
from kcon import qnum

def extractPage(x):
	followercount=0;answercounted=0;answerviewcount=0;answervotecount=0;
	soup=bs(x,'html.parser')
			### Followers for question code
	for followers in soup.find_all('div',re.compile('.*?FollowSecondaryActionItem*?')):
	
		soup1=bs(str(followers),'html.parser')
		strcount=1; 
		for string in soup1.stripped_strings:
			if (strcount%2==0):
				followercount+=qnum(string);		
			strcount+=1;
	###Answer Count		
	for answercount in soup.find_all('div','answer_count'):
		soup2=bs(str(answercount),'html.parser')
		strcount=0;
		for string in soup2.stripped_strings:
			if (strcount%2==0):
				answercounted+=qnum(string);		
			strcount+=1;
	for answerviews in soup.find_all('div',re.compile('.*?AnswerFooter.*?')):
		soup3=bs(str(answerviews),'html.parser')
		strcount=0;
		for string in soup3.stripped_strings:
			if (strcount%2==0):
				answerviewcount+=qnum(string);break;		
			strcount+=1;
	avcount=0		
	for answervotes in soup.find_all('span','count'):
		soup4=bs(str(answervotes),'html.parser')
		
		for string in soup4.stripped_strings:
			if avcount<2:
				avcount+=1;continue;
			else:	
				answervotecount+=qnum(string);
	pageresult=[followercount,answercounted,answerviewcount,answervotecount]						
	return(pageresult)			
if __name__=="__main__":
	pass;	
						
						
		