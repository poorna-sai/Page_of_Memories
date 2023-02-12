from django.db import models
from datetime import datetime
# Create your models here.
from ckeditor.fields import RichTextField


class Posts(models.Model):
	username = models.CharField(max_length = 100  , blank = True)
	date = models.DateTimeField(blank=True  , default=datetime.now )
	description = RichTextField()

class UserModel(models.Model):
	username = models.CharField(max_length = 100  , blank = True)
	email  = models.EmailField(max_length=70,blank=True,unique=True)
	profilepic = models.ImageField(upload_to = 'media/')
	forget_password_token = models.CharField(max_length=100 ,default = "vsdfjsd558dsdfsr5rr")


class PrivateDairy(models.Model):
	username = models.CharField(max_length = 100  , blank = True)
	date = models.DateTimeField(blank=True  , default=datetime.now )
	description = RichTextField()

