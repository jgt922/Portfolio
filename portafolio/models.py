from email.mime import image
from nturl2path import url2pathname
from turtle import title
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portafolio/images/")
    url = URLField(blank=True)
    
