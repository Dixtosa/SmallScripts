# Author:      Dixtosa
# Description: makes it easy to shift subtitles
# Date:        2014

import sys, re
filename=sys.argv[1]
delta = int(sys.argv[2])

def func(m):
	a, b, c, mili = [int(p) for p in re.split(r"[,:]", m)]
	mili += 1000*c+1000*60*b+1000*60*60*a
	
	mili += delta
	
	MILI=mili%1000; mili /= 1000
	C = mili % 60;	mili /= 60
	B = mili % 60;  mili /= 60
	A = mili

	return "%02d:%02d:%02d,%03d" % (A, B, C, MILI)
	
file = open(filename, "r")
text = file.read()
file.close()
fa = re.findall(r"\d\d:\d\d:\d\d,\d\d\d", text)
for i in fa:
	text = text.replace(i, func(i))


file=open(filename[:-4]+"[SHIFTED].srt", "w")
file.write(text)
file.close()