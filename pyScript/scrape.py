#scraper
import requests

from bs4 import BeautifulSoup #web scraping
import smtplib #send email
from email.mime.multipart import MIMEMultipart #email body
from email.mime.text import MIMEText        #email body
import datetime #system date and time manipulation
