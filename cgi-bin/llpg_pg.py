#!C:/Python27/python.exe
# -*- coding: UTF-8 -*-
import cgi
import json
import psycopg2

sql = """select a.uprn, a.address, ST_X(a.geometry), ST_Y(a.geometry)
from angusdata.address_gazetteer a
where a.address ilike '%%' || (%(p_address)s) || '%%'
order by address"""

form = cgi.FieldStorage ()

connection = psycopg2.connect ("host='PostGIS IP address' port='5432' dbname='PostGIS DB Name' user='PostGIS User' password='PostGIS Password'")
cursor = connection.cursor ()
cursor.execute (sql, {"p_address": form["address"].value})

list = []

for record in cursor:
	data = dict (zip (["uprn", "address", "easting", "northing"], record))
	list.append (data)

print "Content-Type: application/json\n"
print json.dumps (list, indent = 4)
