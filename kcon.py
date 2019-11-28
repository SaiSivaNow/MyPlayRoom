import re

def qnum(num):
	if re.search(r'.*?\..*?k',num):
		first=re.search(r'(.*?)\.',num).group(1)
		second=re.search(r'\.(.*?)k',num).group(1)
		result=int(first)*1000+int(second)*100
	elif re.search(r'.*?k',num):
		first=re.search(r'(\d+)k',num).group(1)
		result=int(first)*1000
	elif re.search(r'.*?m',num):
		first=re.search(r'(\d+)m',num).group(1)
		result=int(first)*1000000
	elif re.search(r'.*?\..*?m',num):
		first=re.search(r'(.*?)\.',num).group(1)
		second=re.search(r'\.(.*?)m',num).group(1)
		result=int(first)*1000000+int(second)*100000	
	else:
		result = int(num);
	return result

if __name__=="__main__":
	pass;

