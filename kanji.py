from bs4 import BeautifulSoup as bs
import requests


response=requests.get(url)
content=response.content#this is different from the global content in line 13
soup=bs(content,'html.parser')