from bs4 import BeautifulSoup
from requests.exceptions import ProxyError
import requests
import os
import urllib

def links_by_requests(url_link) :
	try :
		req = requests.get(url_link)
	except ProxyError :
		print "Proxy Error raised"
	finally :
		print "error in requests module"
	sp = BeautifulSoup(req.content)
	return sp

actual = "https://icann562016.sched.org"
soup = links_by_requests(actual)

#to avoid file name redundancy 
allfiles = []

dircnt = [1,38,42,40,32]  # hard-coded values for number of links under each day 
dirname = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]

i = j =0
k = 2

originaldir = os.getcwd()
backslash = "/"

for link in soup.find_all('a',class_="name"):
    fn = link.get("href")
    link = actual + fn

    if (j==0) : 
    	os.chdir(originaldir)
    	os.mkdir(dirname[i])
    	os.chdir(dirname[i])
    	prev = os.getcwd()
    	allfiles = []
    else :
    	os.chdir(prev)

    j=j+1

    if (j==dircnt[i]):
		j = 0
		i=i+1

    print link

    newsp = links_by_requests(link)
    tempdir = newsp.title.string

    if (tempdir.find(backslash)!=-1) :
    	pos = tempdir.find(backslash)
    	tempdir = tempdir[:(pos)] + "_"+tempdir[pos+1:]

    #renames a file if there exists a file with same name 
    if (tempdir in allfiles) :
    	tempdir = tempdir+"_"+str(k)
    	k = k+1

    os.mkdir(tempdir)
    os.chdir(tempdir)
    
    allfiles.append(tempdir)

    for innerlink in newsp.find_all('a',class_= "file-uploaded file-uploaded-pdf") :
		innerlink1 = innerlink.get("href")
		try :
			urllib.urlretrieve(innerlink1,filename=innerlink.get_text())
		except Exception as inst:
			print "Error in urllib module"