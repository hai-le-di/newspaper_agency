# Newspaper Agency

Project for tracking redactors assigned to newspapers in a newspaper agency.

## Check it out!

[Newspaper agency project deployed to Render](https://newspaper-agency-jx6a.onrender.com/accounts/login/)

<br />
login: user <br />
password: test12345

## Installation

Python3 must be already installed

```shell
git clone link
cd newspaper_agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
create .env file with variables: DATABASE_URL, DJANGO_DEBUG, DJANGO_SECRET_KEY, PYTHON_VERSION, WEB_CONCURRENCY
python manage.py runserver # starts Django Server
``` 

## Features

* Authentication functionality for Redactor/User
* Managing newspapers & redactors directly from the website
* Powerful admin panel for advanced managing

## Demo


<img width="960" alt="homepage" src="https://user-images.githubusercontent.com/102927189/217591092-0131d4c1-3596-4523-8e3b-9618e9bafa19.png">

