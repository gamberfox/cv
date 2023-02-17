#february 16 2023
#this script is used to download a video to the current directory
#from the tedTalk website using a url
###python TEDDownload.py (insert url here)


from bs4 import BeautifulSoup as bs#I use aliases to some time typing
import requests as req
import re
import sys

if len(sys.argv)>1:
    url=sys.argv[1]
else:
    sys.exit("error: enter tedTalk url")
r=req.get(url)

print("download starting...")#it's easier to visualize the process this way

soup=bs(r.content, features="lxml")

def getRes():
    for val in soup.findAll("script"):
        if(re.search("props",str(val))) is not None:
            return str(val)

result= getRes()