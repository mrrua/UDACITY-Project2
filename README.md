# UDACITY-Project2
Tournament SQL README
Version: 1.0
Date: 04/09/2015
Created By: Adam Rua

CONTENTS OF THIS FILE:
-------------------------------------
 * Introduction
 * Requirements
 * Installation of Python
 * How to run the Python Project script

INTRODUCTION
-------------------------------------
 This README is for use with Project 1 of UDACITY Full Stack Web Developer Nanodegree and will show the reader how to install Python if needed, as well as how to download, unzip, and run the Python script for Project 1.

REQUIREMENTS
-------------------------------------
 A. You will need Python installed (instructions for its installation can be found below. 
 B. You will need some means of standing up a database. In this project we are using PostgreSQL and a file is included to create the table structure needed for the python project to run.

INSTALLATION OF PYTHON
-------------------------------------
 We will be using Python v2.7.9 for this Project so please ensure you have it installed. If you already do - you can skip this step. If you are not sure, or want to reinstall please continue.
 
 1. Navigate to the Python webpage via your browser. The link is: http://python.org/downloads
 2. Select Python v2.7.9 and click to download whichever version you'd like (specifically around 32 vs 64 bit options due to your preference / machine). 
 3. After download is complete - launch the installer.
 4. During the wizard ensure you select ALL options to be installed (including adding Python to PATH).
 5. You're all set installing Python.
 
HOW TO RUN THE PYTHON PROJECT SCRIPT
-------------------------------------
 Now that you have Python running on your machine. Let continue by running our Project!
 
 1. Launch your DB tool. In our case we will be using PostgreSQL.
 2. Create a new database. In our example we used the name 'tournament'.
 3. After creating the new database, connect to said database.
 4. Import the database tables in the 'tournament.sql' file. (You can use the import comment, '\i <filename>' in PSQL, or just copy and paste the commands in the file.)
 5. Now that you have the database tables loaded, ensure you have also downloaded the 'tournament.py' and 'tournament_test.py' files into the same directory.
 6. Run the 'tournament_test.py' python program. You can do this by running the command: 'python tournament_test.py'.
 7. You have launched and run the tests for Project 2!
 
