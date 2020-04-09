#low_price_finder.py

import requests, html5lib
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


#TODO - user 

def scrapeGoogleShopping(name):
	url = 'https://www.google.com/search?hl=en-US&biw=1366&bih=577&tbm=shop&ei=S5mOXtLHKua9ggfMr4qoCA&q=' + name + '&oq=' + name + '&gs_l=psy-ab-sh.3..0i67k1l3j0l7.46925.46925.0.47131.1.1.0.0.0.0.129.129.0j1.1.0....0...1c.1.64.psy-ab-sh..0.1.127....0.3JxsFVizsFI'
	r = requests.get(url)
	#print(r.content)
	soup = BeautifulSoup(r.content, 'html5lib')
	#print(soup.prettify())
	return soup

#might be the wrong HTML labelling
def cleanText(page):
	products = []
	table = page.find('div', attrs = {'class':'ZGFjDb'})
	print(table)
	for row in table.findAll('div', attrs = {'class':'quote'}):
		info = {}
		info['name'] = row.h5.text
		info['url'] = row.a['href']
		info['img'] = row.img['src']
		info['price'] = row.h6.text
		info['seller'] = row.p.text
		info.append(info) 

    return None





def main():
	search_term = input("Welcome to the Low Price Finder WebScraper app! What product would you like to find the lowest price for?")
	page = scrapeGoogleShopping(search_term)
	cleanText(page)



	



main()