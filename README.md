# musicforme - learn how to play an instrument by finding the best person to teach you

## General info
MusicForMe is a web based application created for users who want to find music teachers and for users who want to teach musical instruments.
There are two types of users: regular and teacher.
This application has an authentication system.

The regular user can: 
- see all the posts created by teachers;
- edit user details;

Additionally, a teacher can:
- create a post;
- edit a post;

## Technologies
- Python 3.8.2
- Django 3.1.3
- Bootstrap 4.3.1

## Project Setup

Get the source code locally: 

`git clone git@github.com:liviusighiartau/musicforme.git`

Create virtual environment:

`mkvirtualenv -p python3.8 <your_env_name>`

Install project requirements (make sure you are at the root of the project):

`pip install -r installation_requirements.txt`

Run the server (make sure you are at the Django root project):

`./manage.py runserver`