# Pattern Match
This is a Part of a Small Project .
Project is to automate the downloading of all the PDF files from https://icann562016.sched.org/ and also from its Child sites.
Then converting all the pdf files to txt files using pdftotext command.
And the major part is to identify how many times the word 'jurisdiction' appeared and in which file.


## Getting Familiar with Filename :

1.fullist.txt- 
this file contains all the details like Name of the PDF,Path of the file(absolute) and number of times the word repeated in that file.

2.Directories like Monday,Sunday ...  - These contain the PDFs that belong on that day.Within this Directory there is a file called diretory_data.txt that gives 										    the count of how many times the word repeated in that particular directory. 

3.localdata.txt - It is in the deep most Directory that corresponds to a link in original website. this file contains the details(Name and count ) locally regarding to that Particular link

4.Script Files - 
	these are the core of this project. Each of these script file is designed in order to perform a specific task .All files are written in Python.

	i) downloader.py - run this script file to download automatically all the PDFS from the actual website and it organises the data very well.

	ii)pdftotextconvertor.py - as the name says,this file is used to convert all the PDFS downloaded in part i) to .txt format

	iii)stringfinder.py - this file uses the txt files generated in part (ii) and searches the whole txt file for the word 'jurisdiction' and reports the necessary   details regarding the file

## Overall Result  
```
	As a whole , there are 329 matches of the word 'jurisdiction' in 35 files.
	158 files didn't contain the word 'jurisdiction'.
```

### Contact
* **[Harsh Gupta](https://github.com/hargup)**
* **[Ranjith Kumar](https://github.com/ranjithkumar007)**
* **[Buridi Aditya](https://github.com/buridiaditya)**
