import urllib, simplejson

def get_busstop_locations():
	bounds = ( 50,0.3,52,-0.3 )
	# bounds = ( 51.50,0.1,51.51,0 )
	url = 'http://countdown.tfl.gov.uk/markers/swLat/%s/swLng/%s/neLat/%s/neLng/%s/?_dc=1315936072189' % bounds

	result = simplejson.load(urllib.urlopen(url))


	for item in result['markers']:

		data = { 'id':item['id'], 'name':item['name'],'direction':item['direction'], 'letter':item['stopIndicator'], 'lat':str(item['lat']), 'lng':str(item['lng']) }

		yield data




		