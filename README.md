# Britecore sample

This is a sample application created for BriteCore<br />
Dennis De St Jeor<br />
2016

# Requirements

* Python 2.7.5

# Installation

* Create a python virtual environment using virtualenv
* Create working directory for your project.  On the Mac I <br />
	$ cd ~/<br />
	$ mkdir workspace<br />
	$ cd workspace<br />
	$ git clone --recursive https://github.com/DrCubby/bcdsj.git bcdsj<br />
	$ cd bcdsj<br />
	$ git checkout develop<br />
	$ git branch <br />
	(this should show that you are now working on the develop branch of the bcdsj repository)<br />
	$ git pull origin develop<br />
	(this will make sure you have the most recent version of the app)<br />
* make sure you are in your virutal environment created for thie application then:<br />
	$ pip install -r requirements.txt
	(this will install all the required libraries needed for this project)
* Let's go ahead and make sure your database is up to date:
	$ python manage.py migrate
* Let's start the builtin webserver in django
	$ python manage.py runserver
* in your browser type:
	http://127.0.0.1:8000



