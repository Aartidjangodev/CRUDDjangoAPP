from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20,default="")

    gender=models.CharField(max_length=20,default="")
    hobbies = models.CharField(max_length=100, default="")
    countryid= models.IntegerField( default=0)

# mvt model{database} view[function]and Template [html]
#run the command
#python manage.py makemigrations
#python manage.py migrate
class Country(models.Model):
    country_name=models.CharField(max_length=50, default="")
    # mvt model{database} view[function]and Template [html]
    # run the command
    # python manage.py makemigrations
    # python manage.py migrate
