#By Dixtosa

path=raw_input('link to CS(for example:c:\Games\counter strike):')

path+='\platform\config\ServerBrowser.vdf'

import os
if not os.path.isfile(path):
    print 'Araswori Link'
    import sys,time
    time.sleep(5)
    sys.exit()

print 'Downloading IPs'

from HTMLParser import HTMLParser
from urllib2 import urlopen

STR='/server_info/'
L_str=len(STR)
class Spider(HTMLParser):
    def __init__(self, html_source):
        HTMLParser.__init__(self)
        self.result=[]
        self.feed(html_source)
        self.ret()
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs:
            if attrs[0][1].find('/server_info/')!=-1:
                self.result.append(attrs[0][1][L_str:][:-1])
    def ret(self):
        return self.result

data=[];y=1
while True:
    req = urlopen('http://www.gametracker.com/search/cs/GE/?searchipp=50&searchpge='+str(y))
    s=req.read()
    if s.find('btn_next_disabled')==-1:
        data+=Spider(s).ret()
    else:
        break
    y+=1

print data
all=''
l=1
for i in data:
    text='''
        '%d'
        {
            'name'        '%s'
            'gamedir'        'cstrike'
            'players'        '12'
            'maxplayers'        '24'
            'map'        'de_inferno'
            'address'        '%s'
            'lastplayed'        '0'
            'secure'        '0'
            'type'        '1'
        }'''%(l,i,i)
    all+=text
    l+=1

a=''''{'
{
    'Favorites'
    {'''

a+=all
a+="""
    }
}"""

f=open(path,'w')
f.write(a)
f.close()
