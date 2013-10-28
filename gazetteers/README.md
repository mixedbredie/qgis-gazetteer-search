Local Authorities in Great Britain all create a similar set of datasets which are essential to the functioning of the organisation. These include address gazetteers, various datasets required for planning and certain obligatory datasets. These can all be made availble to search with this plugin.

I have provided two examples of files which will create web services. One searches the LLPG (Local Land and Property Gazetteer) and the other the LSG (Local Street Gazetteer). Just copy and edit these files for each web service you want to create.

Provided you have suitable tables in your PostGIS database with UPRN (Unique Property Reference Number / Primary Key) and ADDRESS fields and a point geomoetry, a record in the `gazetteers/config.ini` file and a file in the cgi-bin the search will work. If your table does not have UPRN or ADDRESS fields than create a view with a unique field called UPRN and an ADDRESS field with the information you wish to search on.
