###february 16 2023
###developed in windows 10
#this script is used to download a video to the current directory
#from the tedTalk website using a url
###python TEDDownload.py (insert url here)


from bs4 import BeautifulSoup as bs#I use aliases to save time typing
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

for val in soup.findAll("script"):
    if(re.search("props",str(val))) is not None:
        result=str(val)

urlMp4=re.search("(?P<url>https?://[^\s]+)(mp4)",result).group("url")+"mp4"
print("----------------------")

print("saving video as:{}".format(urlMp4))

fileName=urlMp4.split("/")[len(urlMp4.split("/"))-1].split("?")[0]

r=req.get(urlMp4)
print("storing video in {}".format(fileName))

with open(fileName,'wb') as file:
    file.write (r.content)

print("download finished")