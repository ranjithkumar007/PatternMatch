import os 

init_path = os.getcwd()
pattern = "jurisdiction"
m = 0
overall = 0
fulldata = open("fullist.txt","w")
fulldata.write("                List of all files that have the pattern and total number of matches\n\n")
avoid = ["fullist.txt","datafile.txt","directory_data.txt"]

for root,dirs,files in os.walk(init_path,topdown=False) :
	j = 0
	os.chdir(os.path.dirname(root))
	dirdata = open("directory_data.txt","w")
	# prev = os.path.dirname(root)
	os.chdir(root)
	# print root
	dircount = 0
	# 
	for filename in files :
		if (filename[len(filename)-4:]==".txt" and not (filename in avoid)) :
			j = j+1
			temp = filename
			cnt = 0

			with open(filename) as temp2 :
				for line in temp2:
					cnt = cnt+line.count(pattern)
			datafile = open("localdata.txt","a")

			if (j==1) :
				datafile.write("Folder Location (Path) - "+ root + "\n\n")
				datafile.write("Name of the Present Directory - "+ os.path.basename(root)+"\n\n")
				datafile.write("word being checked is "+ pattern + "\n\n")
				datafile.write("                  File Name   	                  " + "                          Number of Times "+ pattern + " appeared\n")
			fancy = []
			for i in range(85-len(temp)) :
				fancy.append(" ")
			fancy = ''.join(fancy)

			if (cnt == 0) :
				datafile.write(str(j)+". "+temp[:(len(temp)-4)] +fancy+ "Not Found in this file\n")
			else :
				datafile.write(str(j)+". "+temp[:(len(temp)-4)]+fancy+str(cnt)+"\n")
				m = m+1
				fulldata.write(str(m)+"."+"Name of the File               ---- "+temp[:len(temp)-4]+"\n"+"  Path of this File              ---- "+root+"\n"+"  Count of Matching words found  ---- "+str(cnt)+"\n\n")
				dircount = dircount + cnt

			datafile.close()
	dirdata.write("Name of the Directory - "+ os.path.dirname(root)+"\n\n")
	overall = overall + dircount
	dirdata.write("Total number of times "+pattern+" appeared in the above Directry is  "+str(overall))
	# print dircount
	dirdata.close()
	os.chdir(init_path)
	#print dircount
	# print overall

fulldata.write("\n\nTotal number of times the Word "+pattern+" appeared in the entire Folder is "+str(overall)+"\n\n")
fulldata.close()

# import os
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))