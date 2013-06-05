import flickrapi
import csv

api_key = '69f5c4bed93103c83054f0ac3dc0a2fc'
flickr = flickrapi.FlickrAPI(api_key)
photoset = '72157630529238250'
def urlGen( photoset_id ):
	with open('graveurls.csv', 'w') as o:
		for photo in flickr.walk_set( photoset_id ):
			title = photo.get('title')
			id = photo.get('id')
			secret = photo.get('secret')
			server = photo.get('server')
			farm = photo.get('farm')
			url = ( title + ',' + 'http://farm' + farm + '.static.flickr.com/' + server + '/' + id + '_' + secret + '_m.jpg')
			print>>o, url
	
			
urlGen(photoset)
	