#  using python 2.7

import re
import urllib2  
import time
import random  
import os 
import sys

def make1sttxt(url):
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
	headers = { 'User-Agent' : user_agent , 'Referer': 'https://www.coedcherry.com/models/sybil-a?page=1' }  
	data = None
	request = urllib2.Request(url, data, headers)
	txt = urllib2.urlopen(request).read()
	filename = 'origin.txt'
	txtfile = open(filename,'wb')
	txtfile.write(txt)
	txtfile.close
	print 'got the url'
	return filename

def get2ndpages(path):
	file = open(path, 'r')
	pattern = re.compile(r'wrapper.*target')
	list = re.findall(pattern,file.read())

	finalurl = [''] * len(list)
	print 'found ' + str(len(list)) + ' urls, ready to download pages'
	count = 0
	for i in list:
		finalurl[count] = 'https://www.coedcherry.com' + i[18:-8] 
		print finalurl[count]
		count = count + 1
	# os.remove(path)
	return finalurl

def make2ndtxt(finalurl):
	count = 0
	print 'start to download ' + str(len(finalurl)) + ' files:'
	for i in finalurl:
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		headers = { 'User-Agent' : user_agent , 'Referer': 'https://www.coedcherry.com/models/sybil-a?page=1' }  
		data = None	
		request = urllib2.Request(i, data, headers) 
		d = urllib2.urlopen(request).read()
		txtfile = open(str(count) + '.txt','wb')
		txtfile.write(d)
		txtfile.close
		print 'downloaded ' + str(count) + ' files'
		count = count + 1
		time.sleep(random.randint(3, 5))
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

def downloadpictures(finalurl, count, num):
	l = len(finalurl)
	numbers = 0
	for i in finalurl:
		user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		headers = { 'User-Agent' : user_agent , 'Referer': 'https://www.coedcherry.com/models/sybil-a?page=1' }  
		data = None
		request = urllib2.Request(i, data, headers) 
		d = urllib2.urlopen(request).read()
		jpgfile = open('result/' + str(count) + '_' + str(numbers) + '.jpg','wb')
		jpgfile.write(d)
		jpgfile.close
		numbers = numbers + 1
		print str(numbers) + '/' + str(l) + ' ' + str(count+1) + '/' + str(num)
		time.sleep(random.randint(3, 5))
print 'please paste the url you want to download: '
xxx = raw_input()

if os.path.exists('result') == False:
	os.mkdir('result') 
print 'start download!'
num = make2ndtxt(get2ndpages(make1sttxt(xxx)))
# start = 7
print 'start to download pictures:'
# num = 30

for i in range(num):
	downloadpictures(makejpgurl(str(i) + '.txt'), i, num)
for i in range(num):
	os.remove(str(i)+'.txt')
os.remove('origin.txt')
print 'congratulations! download over!'
