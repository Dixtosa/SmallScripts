# Author:      Dixtosa
# Description: Gets problems from timus parses and outputs into a file
# Date:        2013
# Dependecies: BeautifulSoup
#                   can be installed with this command: $ sudo apt-get install python-bs4

import urllib2
import sys
from bs4 import BeautifulSoup, NavigableString

def getID(soup):
	return soup.h2.string[:4]
def getName(soup):
	return soup.h2.string[6:]

def getSamples(soup, sub):
	SAMPLES="\n"
	Table = soup.find_all("h3", class_="problem_subtitle")[sub].next_sibling.find_all("tr")[1:]
	
	INPUT_SAMPLES=[]
	OOUTPUT_SAMPLES=[]
	cnt = 1
	
	for i in Table:
		SAMPLES+="----------" + str(cnt) + " testcase----------:\n"; cnt+=1
		IN = i.contents[0].get_text().strip()
		
		OUT = i.contents[1].get_text().strip()
		IN = IN.replace("\r\n", "\n")
		OUT = OUT.replace("\r\n", "\n")
		SAMPLES+="\tINPUT:\n"+IN+"\n"
		SAMPLES+="\tOUTPUT:\n"+ OUT+"\n"

	return SAMPLES

def getTag(soup):
	tagHtml = soup.find_all("div", class_="problem_content")[0].next_sibling.contents[1];
	if type(tagHtml) == NavigableString:
		return tagHtml.strip()
	else:
		return tagHtml.get_text();

def getDifficulty(soup):
	return soup.find_all("div", class_="problem_links")[0].contents[0].contents[0].split (":")[1].strip()

def parse(PAGE):
	soup = BeautifulSoup(PAGE)


	subtitles = soup.find_all("h3", class_="problem_subtitle");
	sub=0

	ID = getID(soup)
	NAME = getName(soup)
	
	Limits = soup.find_all("div", class_="problem_limits")[0].contents;
	TIME_LIMIT = Limits[0].split (":")[1][1:];
	MEMORY_LIMIT = Limits[1].get_text().split (":")[1][1:];

	print TIME_LIMIT, MEMORY_LIMIT

	BACKGROUND = "		   None"
	if subtitles[0].contents[sub] == "Background":
		BACKGROUND = subtitles[sub].next_sibling.get_text() + "\n"
		sub+=1

	print TIME_LIMIT, MEMORY_LIMIT	
	
	PROBLEM=""
	paragraphs = soup.find_all("div", class_="problem_par");

	if subtitles[-1].get_text() == "Hint":
		paragraphs = paragraphs[:-1]
	paragraphs = paragraphs[:-2]
	if (sub == 1):
		paragraphs = paragraphs[1:]
		sub+=1

	
	for paragraph in paragraphs:
		PROBLEM += "\t" + paragraph.get_text() + "\n"		
	
	INPUT_TEXT = subtitles[sub].next_sibling.get_text();  sub+=1
	
	OUTPUT_TEXT = subtitles[sub].next_sibling.get_text(); sub+=1

	SAMPLES = getSamples(soup, sub); sub+=1

	HINT_TEXT = "				 None"
	if sub < len(subtitles):
		HINT_TEXT = "\n" + subtitles[sub].next_sibling.get_text() + "\n"

	SOURCE = soup.find_all("div", class_="problem_source")[0].get_text();
	
	TAG = getTag(soup)

	DIFFICULTY = getDifficulty(soup);
	
	ALL = soup.find_all("a", href="status.aspx?space=1&num="+ID)[0].contents[0].split (" (")[1][:-1]
	
	ALLACC = soup.find_all("a", href="status.aspx?space=1&num="+ID+"&status=accepted")[0].contents[0].split (" (")[1][:-1]

	
	return (ID, NAME, TIME_LIMIT, MEMORY_LIMIT,
				   BACKGROUND, PROBLEM, INPUT_TEXT, OUTPUT_TEXT, SAMPLES, HINT_TEXT, SOURCE, TAG.title(), DIFFICULTY, ALL, ALLACC)
	
def formatProblem(*args):
	result = """\
PROBLEM CODE:		 %s
PROBLEM TITLE:		%s
TIME LIMIT:		   %s
MEMORY LIMIT:		 %s
BACKGROUND:%s
PROBLEM TEXT:
%s\n
INPUT:
%s\n
OUTPUT:
%s\n
SAMPLES:%s
HINT:%s
SOURCE: %s
TAG:				  %s
DIFFICULTY:		   %s
ALL SUBS:			 %s
ACCS:				 %s
"""
	return result % args


problemsFilename = "problems.txt"
queryURL = "http://acm.timus.ru/problem.aspx?space=1&num="

def Main():
	print "usage: \n\t\tgettimus.py start end\n\t\tgettimus.py end <- assumes start=1000\nindices are inclusive"
	start, end = "1000", ""

	if len(sys.argv) == 2:
		end = sys.argv[1]
	elif len(sys.argv) == 3:
		start, end = sys.argv[1:3]
	else:
		print "read usage!"
		quit()
	start = int(start)
	end = int(end)
	problems = [str(p) for p in range(start, end + 1)]
	exclusion = []

	#if  the first problem is 1000 then rewrite otherwise append
	problemsFile = open(problemsFilename, "w" if start == 1000 else "a") 

	for counter, number in enumerate(problems):
		URL = queryURL + number
		pgObj = None
		try:
			pgObj = urllib2.urlopen(URL)
		except:
			print "Exception occured"
			if raw_input("continue? [Y/n]:").lower() == "y":
				print "OK, skipping %sth" % (number)
				continue
			else:
				print "Continue from ", number
				break
		
		try:
			parameters = parse( pgObj.read() )
			difficulties.append(parameters[-3]) #I know I know ugly
			problemBody = formatProblem(parameters) + "\n"*7
			problemsFile.write(problemBody.encode ("utf8"))
		except:
			exclusion.append(number);
			
		print "%f\% done" % (100.0 * counter / len(problems))
	
	problemsFile.close()
	print "Omitted problems (total %d):" % (len(exclusion))
	#print exclusion
	#print difficulties

Main()