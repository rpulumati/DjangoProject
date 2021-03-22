# DjangoProject
Sample Polls Project developed in Python Django framework.

Title: Polls Project

Introduction: Intention of this project is to get my hands on Django framework

Technologies: Python 3.9, Django 3.1.3, CSS, HTML, Postgresql

Setup:
Initial thing to do is clone the repository using below commands,

$ git clone https://github.com/rpulumati/DjangoProject.git
$ cd polls-project


Create a virtual environment to install dependencies and active the environment:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate

Then install the dependencies:
(env)$ pip install -r requirements.txt  (pip is pythons package manager)

After installing dependencies:
(env)$ cd project
(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/PollsProject

Features:
 Sample project 
        User Registration
        User Login 
        Create polls question, perform poll, and view results
        User Logout
        
 Basic Django scaffolding (commands, statics, etc.)
