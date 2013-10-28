The plugin expects the JSON data to be in the format: UPRN, ADDRESS, EASTING, NORTHING

You could create a view for each of the datasets you want to search and name the fields as above. This is OK even for the LSG and Postcodes as the user does not see the field name, only the results returned.

Point datasets in PostGIS will work as the code extracts the X and Y from the geometry. Need to check whether it works with multipoints - I suspect not.

Line and polygon features, like the street gazetteer and postcode areas, will need to have the geometric centroid extracted and this is shown in the `lsg_pg.py` file. It uses the PostGIS `ST_Centroid` function. Bear in mind that for certain shapes the centroid may be outside the polygon or off the line feature.  For area features like postcode areas you could also use the `ST_PointOnSurface` function if you want to return a point that is definitely inside the polygon.
