"""Only hacking the text of internet site and Details"""

import nltk   
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

response = urllib.request.urlopen('https://newweigh.ie/')
html = response.read()
clean = BeautifulSoup(html).get_text()
print(clean)
