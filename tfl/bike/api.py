# -*- coding: utf-8 -*-
'''
https://www.cyclestreets.net/api/journey.xml?
key=63356ae9c48793e1
&plan=quietest
&itinerarypoints=-0.140085,51.502022,Buckingham+Palace|-0.129204,51.504353,Horse+Guards+Parade|-0.129394,51.499496,Westminster+Abbey
'''

import urllib2
from django.conf import settings
from pprint import pprint as pp


import urllib
from elementtree.ElementTree import parse

def get_boris_data():
	url = 'http://www.tfl.gov.uk/tfl/businessandpartners/syndication/feed.aspx?email=errkkgeorge@gmail.com&feedId=12'
	
	xmlfile = urllib.urlopen(url)

	doc = parse( xmlfile ).getroot()

	for element in doc:
		'''
		0	id
		1	name
		2	terminalName
		3	lat
		4	long
		5	installed
		6	installDate
		7	removalDate
		8	temporary
		9	nbBikes
		10	nbEmptyDocks
		11	nbDocks
		'''
		data = {
			'id' : int(element[0].text),
			'name' : element[1].text,
			'terminalName' : element[2].text,
			'lat' : float(element[3].text),
			'lng' : float(element[4].text),
			'nbBikes' : element[9].text,
			'nbEmptyDocks' : int(element[10].text),
			'nbDocks' : int(element[11].text),
		}

		yield data
		



