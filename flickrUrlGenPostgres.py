import flickrapi
import psycopg2


api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
flickr = flickrapi.FlickrAPI(api_key)
photoset = 'xxxxxxxx'
def urlGen( photoset_id ):
	con = None
	try:
		con = psycopg2.connect(database='xxxxxxx', user='xxxxxxxxxxx') 
		cur = con.cursor()
		for photo in flickr.walk_set( photoset_id ):
			title = photo.get('title')
			photoid = photo.get('id')
			secret = photo.get('secret')
			server = photo.get('server')
			farm = photo.get('farm')
			url = ( title + ',' + 'http://farm' + farm + '.static.flickr.com/' + server + '/' + photoid + '_' + secret + '_m.jpg')
			cur.execute("DROP TABLE IF EXISTS flickrUrls")
			cur.execute("CREATE TABLE flickrUrls(title TEXT, url TEXT")
			query = "INSERT INTO coagis.flickrUrls (title, url) VALUES(%s, %s)"
			cur.executemany(query, flickrUrls)
		
			con.commit()
		
except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()		
	
			
urlGen(photoset)
	