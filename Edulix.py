# http://www.edulix.com/unisearch/univreview.php
# CUNY : http://edulix.com/unisearch/univreview.php?stid=1479&univid=1501
# Albany : http://edulix.com/unisearch/univreview.php?stid=1479&univid=1583 

import requests
import urllib2
import re
from bs4 import BeautifulSoup
import os.path
import urllib


url = "http://edulix.com/unisearch/univreview.php?stid=1479&univid=1583"
user_url = "http://edulix.com/unisearch/"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

admit_data = soup.find_all("a",{ "class" : "admit"})
reject_data = soup.find_all("a",{ "class" : "reject"})


print "Admit links: "
f = open('Edulix_Admit.txt','w')
for adm in admit_data:
	
	print adm.text
	#http://edulix.com/unisearch/ + adm.get('href') [user.php?uid=3310]
	#user_url = "http://edulix.com/unisearch/user.php?uid=3312"
	user_url = "http://edulix.com/unisearch/"
	user_url = user_url + adm.get('href')
	#print user_url
	
	r = requests.get(user_url)
	soup = BeautifulSoup(r.text,"html.parser")
	#user_data = soup.find_all("td",{"text" : "Grade"})
	#user_data = soup.find_all('td', text = re.compile('\n'))
	user_data = soup.find_all('td')
	for mem in xrange(len(user_data)):
		if user_data[mem].text == "Grade":
			user_score = float(user_data[mem+1].text)
			if user_score < 10:
				if user_score < 6.0:
					print user_url
					s = adm.text + " " + user_url + "\n"
					f.write(s)

			else:
				if user_score < 60:
					print user_url
					s = adm.text + " " + user_url + "\n"
					f.write(s)
			break;
	else:
		print "No details given"

	f.closed

print "\n \n"

print "Reject links: "
f = open('Edulix_Reject.txt','w')
for adm in reject_data:
	print adm.text
	
	user_url = "http://edulix.com/unisearch/"
	user_url = user_url + adm.get('href')
	
	
	r = requests.get(user_url)
	soup = BeautifulSoup(r.text,"html.parser")
	user_data = soup.find_all('td')
	
	for mem in xrange(len(user_data)):
		if user_data[mem].text == "Grade":
			user_score = float(user_data[mem+1].text)
			if user_score < 10:
				if user_score < 6.0:
					print user_url
					s = adm.text + " " + user_url + "\n"
					f.write(s)

			else:
				if user_score < 60:
					print user_url
					s = adm.text + " " + user_url + "\n"
					f.write(s)
			break;
	
	else:
		print "No details given"

	f.closed