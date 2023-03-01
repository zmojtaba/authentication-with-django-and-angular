# athentication-with-django-and-angular
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
all user related task, consist of:
		1- registration
		2- login
		3- logout
		4- forget password
		5- email verification
this project consist of two main part: django & angular




## Technologies
Project is created with:
* django   version: 4
* postgres version: 15
* angular  version: 15

## setup
#### django
for django part you need to install postgresql, then if you want to send email with consol in settings.py uncomment EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' so you can see the email in your consol but if you want to use template for the email you need to set smtp setting for it( [here](https://www.abstractapi.com/guides/django-send-email#:~:text=In%20order%20to%20send%20emails,and%20generate%20an%20app%20password) you can find the settings).
for more privacy we use environ lib in djnago; therefor you can create .env file in the settings directory and put your secret key, postgres info and emial pass to it.
```
SECRET_KEY=

DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```
after this requirements lib should install:
```
pip install -r requirements.txt
```
now you can run the server go into project and:
```
python manage.py runserver
```

#### angular
go to front folder and run below to install angular dependency module
```
npm install
```
notice if you didn't install angular globaly first do it
```
npm install -g @angular/cli
```
after that go to root flolder and run :
```
ng serve
```

#### if you have url error check server port in environment.ts

