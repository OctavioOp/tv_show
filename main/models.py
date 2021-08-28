from __future__ import unicode_literals
from django.core.checks import messages
from django.db import models
from django.db.models.base import Model
from datetime import date, datetime
import re

from django.db.models.fields import CharField, DateTimeField, EmailField
from django.urls.resolvers import URLPattern

# Create your models here.


class TvManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Show name should be at least 2 characters"
        '''elif len(postData['title']) > 2:
            incoming_title= postData['title']
            if tv_show.objects.get(title=incoming_title):
                errors['title']= 'Title already exist'''
            
            
        if len(postData['network']) < 3:
            errors['network'] = "Show network should be at least 2 characters"
        if len(postData['desc']) != 0:
            if len(postData['desc']) < 10:
                errors['desc'] = "Show description should be at least 10 characters"
        try:
            if datetime.strptime(postData['date_show'], "%Y-%m-%d").date() > datetime.today().date():
             errors['date_show'] = 'invalid date, try to use an older date'
        except:
            errors['date_show'] = 'Set a valid date'
        

        return errors


class tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    desc = models.TextField()
    zelda = models.CharField(
        max_length=500, default='https://media2.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif?cid=ecf05e47mnvcxnlgry2pnecdjoe54nzctn9h5naumw04xddv&rid=giphy.gif&ct=g')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = TvManager()

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        NUM_REGEX = re.compile('[0-9]')
        if len(postData['name']) < 2:
            errors['name'] = 'name needs more than 3 letters'
        if NUM_REGEX.match(postData['name']):
            errors['name'] = 'only letters are allowed'
        if len(postData['password']) < 8:
            errors['password'] = 'Password has 8 characters'
        if postData['password'] != postData['password_confirm']:
            errors['password']= "Passwords doesn't match"
        return errors


class User(models.Model):
    name = CharField(max_length=255)
    email = EmailField()
    password = CharField(max_length=255)
    avatar = CharField(default='https://www.amongusavatarcreator.com/assets/img/main/icon.png',max_length=255)
    birthdat = DateTimeField(default='2000-11-02')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = UserManager()