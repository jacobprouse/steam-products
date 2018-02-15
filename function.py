from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re


def steamContent(type):

	#specials
	specialUrl = 'http://store.steampowered.com/search/?specials=1&os=win.html'

	#topsellers
	topSellUrl = 'http://store.steampowered.com/search/?filter=topsellers&os=win.html'
	
	#upcoming
	upcomingUrl = 'http://store.steampowered.com/search/?filter=comingsoon&os=win.html'

	if type == "Top Sellers":
		url = topSellUrl

	elif type == "Specials":
		url = specialUrl

	else:
		url = upcomingUrl


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

	#make an array
	name_array = []

	for links in soup.find_all(href = re.compile("app")):

		#creating array with regex to parse link
		names = re.findall(r'[A-Z][A-Za-z]*', links.get("href"))

		#append to an array
		name_array.append(' '.join(names))


		# #joining array
		# print(' '.join(names))
	return name_array
