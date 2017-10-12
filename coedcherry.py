import re
import urllib2  
import time
import random 

def get2ndpages(path):
	file = open(path, 'r')
	pattern = re.compile(r'wrapper.*target')
	list = re.findall(pattern,file.read())

	finalurl = [''] * len(list)
	count = 0
	for i in list:
		finalurl[count] = 'https://www.coedcherry.com' + i[18:-8] 
		print finalurl[count]
		count = count + 1
	return finalurl


def make2ndtxt(finalurl):
	count = 0
	print 'start to download ' + str(len(finalurl)) + 'files:'
	for i in finalurl:
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		headers = { 'User-Agent' : user_agent , 'Referer': 'https://www.coedcherry.com/models/sybil-a?page=1' }  
		data = None
		request = urllib2.Request(i, data, headers) 
		d = urllib2.urlopen(request).read()
		txtfile = open(str(count) + '.txt','wb')
		txtfile.write(d)
		txtfile.close
		print count
		count = count + 1
		time.sleep(random.randint(5, 10))
	return len(finalurl)

def makejpgurl(filepath):
	urlfile = open(filepath, 'r')
	pattern = re.compile(r'src=".*jpg"')
	reurl = re.findall(pattern, urlfile.read())
	url = ['']*len(reurl)
	count = 0
	for i in reurl:
		url[count] = i[5:-1] 
		count = count + 1
	finalurl = ['']*len(reurl)
	count = 0
	for i in url:
		pattern = re.compile(r'.*th')
		first = re.match(pattern, i).group()[:-2]
		pattern = re.compile(r'240_.*')
		finalurl[count] = first + re.search(pattern,i).group()[4:]
		# print finalurl[count]
		count = count + 1
	return finalurl

def downloadpictures(finalurl, count):
	for i in finalurl:
		print i
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		headers = { 'User-Agent' : user_agent , 'Referer': 'https://www.coedcherry.com/models/sybil-a?page=1' }  
		data = None
		request = urllib2.Request(i, data, headers) 
		d = urllib2.urlopen(request).read()
		jpgfile = open(str(count) + '.jpg','wb')
		jpgfile.write(d)
		jpgfile.close
		print count
		count = count + 1
		time.sleep(random.randint(5, 10))

for i in range(make2ndtxt(get2ndpages('mmm.txt'))):
	downloadpictures(makejpgurl(str(i) + '.txt'), 50*i)