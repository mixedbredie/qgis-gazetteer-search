# LLPG file

import json
import collections

url = "http://<yourserveriphere>/cgi-bin/llpg_pg.py"
params = {
	'address': '##searchstring##'
}

def parseRequestResults (data):
	json_result = json.loads (data)

	for item in json_result:
		result = collections.namedtuple ('Result', ['description','x','y','zoom', 'epsg'])
		result.description = item['address']
		result.x = float (item['easting'])
		result.y = float (item['northing'])
		result.zoom = 1250
		result.epsg = 27700
		yield result
