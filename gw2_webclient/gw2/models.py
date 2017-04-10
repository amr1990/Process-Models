from __future__ import unicode_literals

from django.db import models


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


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    charid = models.ForeignKey(Character)
    bankid = models.ForeignKey(Bank)
    gameid = models.ForeignKey(Game)
    tpid = models.ForeignKey(TradingPost)
    achievementid = models.ForeignKey(Achievement)

class Achievement(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        abstract = True

class Daily(Achievement):


    class Meta(Achievement.Meta):
        db_table = 'daily_achievement'


class General(Achievement):

    class Meta(Achievement.Meta):
        db_table = 'genera_achievement'


class TradingPost(models.Model):

class Character(models.Model):
    name = models.TextField(primary_key=True)
    
class Game(models.Model):


'''

class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField()

class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField()


