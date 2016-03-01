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
	$ pip install -r requirements.txt<br />
	(this will install all the required libraries needed for this project)<br />
* Let's go ahead and make sure your database is up to date:<br />
	$ python manage.py migrate<br />
* Let's start the builtin webserver in django<br />
	$ python manage.py runserver --insecure<br />
* in your browser type:<br />
	http://127.0.0.1:8000<br />

# Questions You May Have

Q:  Where are the tests?<br />
A:  I didn't write any.  While I can write functional and unit tests, this app is so standard Django (extensively tested) that I felt no need.<br />
<br />
Q:  Did you use TDD?<br />
A:  No...see above.<br />
<br />
Q:  Are you blind?  it's ugly<br />
A:  No.  Fully functional physically but thanks for asking.  I chose not to go overboard in making it pretty.  I've put in enough css/jquery ui/ajax, I think anyway, to make it  clear I know how to control and develop an interface.  I'm not a graphic designer and I wasn't going to spend money on some template<br />
<br />
Q:  Why did you use pure css?<br />
A:  I thought about skeleton and/or min but pure is small and as functional as I needed.  I don't believe in excess junk laying around<br />
<br />
Q:  Where's the angular<br />
A:  2 reasons:  1) Too much for a demo project.  Yes, I know it and use it daily. 2) Django's template markup and Angular are identical and given the nature of the project, I didn't think it would prove anything to modify django's template markup to allow for angualar<br />
<br />
Q:  Some things are missing like forgotten password<br />
A:  Sure.  No problem.  There are many things I would add to this project if it were a live system but it's not. It's a demo on my ability to not just understand and issue but to execute in an organized, thoughtful, extensible way.




