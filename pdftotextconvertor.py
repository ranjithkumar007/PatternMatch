# !/usr/bin/python
import os
from os.path import join,isfile
import string

init_path = os.getcwd()
braces = "()&"

for root,dirs,files in os.walk(init_path):
	# print root
	# print "----------------"
	for name in files :
		# print name 
		#skips the script file in the current directory
		if (name[len(name)-3:] == ".py" or name[len(name)-4:]==".txt") :
			continue
		temp = name
		name = name.translate(None,braces)
		os.chdir(root)
		os.rename(temp,name)

		# newname is used as whitespaces are only considered if we use  a backslash infront of it
		newname = []
		for i in name:
			if (i.isspace()):
				newname.append('\\')
			newname.append(i)
		newname = ''.join(newname)
		os.system(("pdftotext %s")%(newname))
		os.chdir(init_path)