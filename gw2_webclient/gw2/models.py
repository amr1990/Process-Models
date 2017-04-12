from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

import json


# Create your models here.

'''class Profession(models.Model):
    name = models.TextField(primary_key=True)
    skill = models.ForeignKey(ProfessionSkill)
    especializations = models.TextField()
    weapontypes = models.ForeignKey(Weapon)

class Weapon(models.Model):
    name = models.TextField(primary_key=True)
    skills = models.ForeignKey(WeaponSkill)

class Skill(models.Model):
    name = models.TextField(primary_key=True)

class ProfessionSkill(Skill):

class WeaponSkill(Skill):



class TradingPost(models.Model):


    
class Game(models.Model):


class Player(models.Model):
    charid = models.ForeignKey(Character)
    bankid = models.ForeignKey(Bank)
    gameid = models.ForeignKey(Game)
    tpid = models.ForeignKey(TradingPost)
    achievementid = models.ForeignKey(Achievement)



'''
class Inventory(models.Model):
    item = models.TextField(null=False)

    def setitems(self, x):
        self.item = json.dumps(x)

    def __unicode__(self):
        return self.item


class Character(models.Model):
    name = models.TextField()
    race = models.TextField()
    gender = models.TextField()
    profession = models.TextField
    level = models.IntegerField()
    guild = models.TextField(blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    apikey = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username


class Bank(models.Model):
    item = models.TextField()

    def __unicode__(self):
        return self.item