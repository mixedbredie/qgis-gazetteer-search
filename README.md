qgis-gazetteer-search
=====================

Search plugin for QGIS 2.0 based on @AstunTechnology's QGIS Gazetteer Search plugin by Nathan Woodrow (@NathanW2). Enhancements by Matt Travis, Kevin Williams and Simon Miles (and probably others).

This plugin requires QGIS 2.0+ and the QGIS Gazetteer Plugin installed.  It will also need a webserver (Apache), a database (PostgeSQL/PostGIS), Python 2.7 and psycopg2, the python/postgresql connector. I have it installed and running on Windows 7 Professional.

1. Download the zipped plugin from https://github.com/AstunTechnology/QGIS-Gazetteer-Plugin and unzip it into C:\Users\Your User Name\\.qgis2\python\plugins\gazetteersearch (make sure that the directory is called gazetteersearch and all the files are in this folder and not a subfolder)

2. In the "gazetteers" subfolder, edit config.ini to include the gazetteers you want to search e.g:

  [LLPG]
  gazetteer:llpg
  
  [LSG]
  gazetteer:lsg

  The other gazetteers listed in the config.ini can be removed (Astun, Geonames, Yahoo) which I did as I couldn't get the proxy authentication to work through the firewall.  Any gazetteers listed here will show up in the plugin in QGIS.

3. Create a file called llpg.py (ie, the same name that you specified in the config.ini file) – see the attached version to duplicate and edit (the URL will need to be changed to point to your own web server).

4. On the web server machine, install Python 2.7 (http://www.python.org/download/releases/2.7.5/) and psycopg2 ( http://www.stickpeople.com/projects/python/win-psycopg/) choosing the correct version to match your set up.

5. You could use the latest Apache web server (http://www.apachehaus.com/cgi-bin/download.plx) installed on your own PC in which case the URL will be http://localhost/cgi-bin/llpg_pg.py otherwise if installed on another machine adjust the URL accordingly.

6. Create a file in the cgi-bin folder of your web server. I have attached a script llpg_pg.py which you should be able to tweak to connect to your Postgres/PostGIS database. For each gazetteer listed in gazetteers/config.ini there will be a corresponding file in the gazetteers directory and another in the cgi-bin directory of your webserver.

7. Check the httpd.conf and make sure the cgi-bin module is enabled, the path to apache2 is correct and permissions set to allow access. This may need to be tweaked to suit your environment.

This is the way that we have set up the plugin, with a web service generating search results in JSON format, which the plugin then reads.  You might be able to avoid using the web service by doing the SQL query directly within the plugin code, but the web service is useful as it can be re-used by other applications.

Readme amended and updated from original supplied by @mtravis.
