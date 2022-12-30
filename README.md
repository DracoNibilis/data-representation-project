# data-representation-project
------
------

Repository contains Web application in Flask that has a RESTful API and is linked to database. Web page consume the API and performs CRUD operations on data. Application is 

------
Files included:

- planetDAO.py - Python script to connect with database,
- planetsviewer.html - HTML page to display results, data related to planets,
- server.py - Python script to connect with server,
- .gitignore - file contains all files that are not display in repository,
- images folder - contains images used on web page, 
- README.md,
- requirements.txt - file contain all modules that have to been installed to run scripts in virtual environment,
- datarepresentation folder - database created in MySQL contains table used in this project.

------
Imported libraries to run Python scripts:
- mysql.connector
- dbconfig as cfg ( configuration file )
- from flask import Flask, jsonify, request, abort.

------
Environments:
- Database is create and run on MySQL provided by Wampserver,all installation files available on https://wampserver.aviatechno.net/
- Python scripts are written and run on Python 3.8.8  by Visual Studio Code version 1.74.2.
- VM - Script was run on virtual environment, to run code please run - pip install -r requirements.txt to get all nessesary Python packedges.

------
------

