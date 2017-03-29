from django.shortcuts import render

# Create your views here.


import requests
import json



class GwClient(object):
    URL = "https://api.guildwars2.com/v2/"
    url_services = {
        "professions": "professions/"
    }

    def __init__(self, professionname, apikey):
        super(GwClient, self).__init__()
        self.profession = professionname
        self.apikey = apikey


    @property
    def getprofession(self):
        url = GwClient.URL + GwClient.url_services["professions"] + self.profession
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

        return return_response


if __name__ == "__main__":
    api = None
    client = GwClient("Mesmer", api)
    print client.getprofession