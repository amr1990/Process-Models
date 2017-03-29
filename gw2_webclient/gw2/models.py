from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Profession(models.Model):
    name = models.TextField(primary_key=True)
    skillid = models.ForeignKey(ProfessionSkill)
    especializations = models.TextField()
    weapontypesid = models.ForeignKey(Weapon)

class Weapon(models.Model):


class ProfessionSkill(models.Model):

class WeaponSkill(models.Model):


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    charid = models.ForeignKey(Character)
    bankid = models.ForeignKey(Bank)
    gameid = models.ForeignKey(Game)
    tpid = models.ForeignKey(TradingPost)
    achievementid = models.ForeignKey(Achievement)

class Achievement(models.Model):

class TradingPost(models.Model):

class Character(models.Model):
    name = models.TextField(primary_key=True)


class Bank(models.Model):

class Game(models.Model):

