#Trying to hacking sites

import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# URL of the web page you want to extract
url = "https://newweigh.ie/"

# initialize a session
session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

#helps to make all file to html
html = session.get(url).content
# f = open('fakenewweigh01.html','wb')
# f.write(html)
# f.close()
# print(html)

## parse HTML using beautiful soup
soup = bs(html, "html.parser")

# get the JavaScript files
script_files = []

for script in soup.find_all("script"):
    if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)
# print('javaScript Files',script_files)

# get the CSS files
css_files = []

for css in soup.find_all("link"):
    if css.attrs.get("href"):
        # if the link tag has the 'href' attribute
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)

# print(css_files)
f = open('fakenewweigh.txt','w')
f.write(css_url)
f.close()


# print(html)
