from __future__ import unicode_literals

#from django.db import models
import requests
import json

# Create your models here.

class Profession(object):
    profession = ""
    URL = "https://api.guildwars2.com/v2/professions/"

    def __init__(self, professionname):
        self.profession = professionname

    @property
    def getprofession(self):
        url = Profession.URL + self.profession
        req = requests.get(url)

        return_response = {}
        data = json.loads(req.text)

        return_response["name"] = {}
        return_response["name"] = data["name"]
        return_response["training"] = {}
        return_response["training"] = data["training"]
        return_response["training"] = data["training"]
        return_response["weapons"] = {}
        return_response["weapons"] = data["weapons"]
        '''return_response["weapons"]["axe"] = data["weapons"]["Axe"]
        return_response["weapons"]["Dagger"] = data["weapons"]["Dagger"]
        return_response["weapons"]["Mace"] = data["weapons"]["Mace"]
        return_response["weapons"]["Pistol"] = data["weapons"]["Pistol"]
        return_response["weapons"]["Sword"] = data["weapons"]["Sword"]
        return_response["weapons"]["Scepter"] = data["weapons"]["Scepter"]
        return_response["weapons"]["Focus"] = data["weapons"]["Focus"]
        return_response["weapons"]["Shield"] = data["weapons"]["Shield"]
        return_response["weapons"]["Torch"] = data["weapons"]["Torch"]
        return_response["weapons"]["Warhorn"] = data["weapons"]["Warhorn"]
        return_response["weapons"]["Greatsword"] = data["weapons"]["Greatsword"]
        return_response["weapons"]["Hammer"] = data["weapons"]["Hammer"]
        return_response["weapons"]["Longbow"] = data["weapons"]["Longbow"]
        return_response["weapons"]["Rifle"] = data["weapons"]["Rifle"]
        return_response["weapons"]["Shortbow"] = data["weapons"]["Shortbow"]
        return_response["weapons"]["Staff"] = data["weapons"]["Staff"]
        return_response["weapons"]["Speargun"] = data["weapons"]["Speargun"]
        return_response["weapons"]["Spear"] = data["weapons"]["Spear"]
        return_response["weapons"]["Trident"] = data["weapons"]["Trident"]'''

        return return_response
