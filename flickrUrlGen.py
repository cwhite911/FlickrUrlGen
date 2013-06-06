import flickrapi


api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
flickr = flickrapi.FlickrAPI(api_key)
photoset = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
def urlGen( photoset_id ):
	with open('graveurls.csv', 'w') as o:
		o.write('title, url\n')
		for photo in flickr.walk_set( photoset_id ):
			title = photo.get('title')
			id = photo.get('id')
			secret = photo.get('secret')
			server = photo.get('server')
			farm = photo.get('farm')
			url = ( title + ',' + 'http://farm' + farm + '.static.flickr.com/' + server + '/' + id + '_' + secret + '_m.jpg\n')
			o.write(url)
	
			
urlGen(photoset)

	