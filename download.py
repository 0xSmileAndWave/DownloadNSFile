
# Written by Lau
# Using python 3

import urllib.request
import time
import os

def createDir():
	dir=os.getcwd() + "\\swf"
	if os.path.exists(dir) :
		os.chdir(dir)
	else:
		os.mkdir(dir)
		os.chdir(dir)
	#print(dir)

def lulz():
	createDir()
	url="https://ns-static-bwhcb6a5289.netdna-ssl.com/swf/3.3.00422/swf/skills/"
	skill=""
	start=2004			# change this to skill number
	end=2005			# change this to skill number
	for i in range(start,end+1):
		if i <= 9:
			skill="skill_0" + str(i) + ".swf"
		else:
			skill="skill_" + str(i) + ".swf"
		urlTxt=url+skill
		try:
			urllib.request.urlretrieve(urlTxt, skill)
			print(urlTxt)
		except urllib.error.HTTPError as err:
			if err.code == 404:
				print("File " + skill + " not found")
		time.sleep(10)		# modify this delay if needed	
	
lulz()