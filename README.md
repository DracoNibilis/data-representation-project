# data-representation-project

Repositorium contains Web application in Flask that has a RESTful API, application is linked to database. Web page consume the API and performs CRUD operations on data.

Files included:

- planetDAO.py - Python script to connect with database,
- planetsviewer.html - HTML page to display results, data related to planets,
- server.py - Python script to connect with server,
- .gitignore - file contains all files that are not display in repository,
- images folder - contains images used on web page, 
- README.md .

Imported libraries to run Python scripts:
- mysql.connector
- dbconfig as cfg ( configuration file )
- from flask import Flask, jsonify, request, abort.


Enviroments:
- Database is create and run on MySQL provided by Wampserver all installation files available on https://wampserver.aviatechno.net/
- Python scripts are written and run on Python 3.8.8  by Visual Studio Code version 1.74.2.



