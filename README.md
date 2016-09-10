# Django custom users management app

This is a simple example of custom user app in Django Framework 1.9 + mailgun + Django Rest Framework

Through this app you can:

* Design your own User model
* Subscribe future users
* Create users
* Update users
* Delete users
* Watch user details (profile)
* Sign in
* Sign out
* Sent email verification
* Upload and set user profile picture 
* Create automatic slugs
* Expose users throgh API (Django Rest Framework)


## Running the project

#### Installation

* Install virtual environments. You can use [my instructions](https://itbinnacle.wordpress.com/2015/02/09/starting-with-virtuale-environments-virtualenv/)
* Install pip, django, mysql. You can use [my instructions](https://itbinnacle.wordpress.com/2015/01/29/starting-with-django-mysql-on-mac-osx/)
* Install project dependecies  
	```pip install -r requirements.txt```
* Change DB settings to your own settings  
	> DATABASES = {  
	>     &nbsp;&nbsp;&nbsp;'default': {  
	>         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'ENGINE': 'django.db.backends.mysql',   
	>         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'NAME': 'django_userprofiles',        
	>         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'USER': '\<your_user>',  
	>         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'PASSWORD': '\<your_password>',  
	>         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'HOST': 'localhost',       
	>  &nbsp;&nbsp;&nbsp;}  
	> }  

* Create the database 
	```mysql: create database django_userprofiles```
* Run DB migrations
	```python manage.py migrate ```


#### Run project 

* ```python manage.py runserver```

&nbsp;

> **You should use django admin interface to activate users**  
> 
> From console:   
> ```python manage.py createsuperuser```   
> 
> Activate your superuser through DB    
> ```mysql: update userprofiles_user set is_active  1```   
> 
> You can sign in in your browser   
> ``` localhost:8000/admin ```  
 

&nbsp;

> **You can find troubleshooting help in** [my blog](https://itbinnacle.wordpress.com/) 
