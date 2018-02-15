from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re

#the site to request access content
url = 'http://store.steampowered.com/search/?specials=1&os=win.html'

#create request
request = Request(url)

#create a response to request content
response = urlopen(request)

#store content
steamHtml = response.read()

#closing request
response.close()

#creating a soup
soup = BeautifulSoup(steamHtml, "html.parser")

for links in soup.find_all(href = re.compile("app")):

	#creating array with regex to parse link
	names = re.findall(r'[A-Z][A-Za-z]*', links.get("href"))

	#joining array
	print(' '.join(names))
