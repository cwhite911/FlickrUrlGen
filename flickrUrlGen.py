import flickrapi
import csv

api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
flickr = flickrapi.FlickrAPI(api_key)
photoset = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
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
	