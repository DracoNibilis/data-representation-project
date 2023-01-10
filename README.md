# data-representation-project
------
------

Repository contains Web application in Flask that has a RESTful API and is linked to database. Web page consume the API and performs CRUD operations on data. Application is create to stock list of planets already discovered in our Solar System and beyond.

------
Files included:

- planetDAO.py - Python script to connect with database,
- planetsviewer.html - HTML page to display results, data related to planets,
- server.py - Python script to connect with server,
- .gitignore - file contains all files that are not display in repository,
- images folder - contains images used on web page, 
- README.md,
- requirements.txt - file contain all modules that have to been installed to run scripts in virtual environment,

------
Imported libraries to run Python scripts:
- mysql.connector
- dbconfig as cfg ( configuration file for database )
- from flask import Flask, jsonify, request, abort.

------
Environments:
- to run page use link: http://draconibilis.eu.pythonanywhere.com/planetsviewer.html
- Database is create on eu.pythonanywhere.com 
- Python scripts are written and run on Python 3.8.8  by Visual Studio Code version 1.74.2.
- VM - Script was run on virtual environment, to run code please run - pip install -r requirements.txt to get all nessesary Python packedges.

------
------

