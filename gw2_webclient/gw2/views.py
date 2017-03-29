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

    @property
    def getAchievements(self):
        url = GwClient.URL  +  GwClient.url_services["achievements"]
        yolo = []
        req = requests.get(url)

        return_response = {}
        data = json.loads(req.text)
        return_response["ids"] = data

        for id in data[0:20]:
            return_response_achievements = {}
            url_id = GwClient.URL + GwClient.url_services["achievements"] + str(id)
            #print id
            req_achievements = requests.get(url_id)
            data_achievements = json.loads(req_achievements.text)
            return_response_achievements["name"] = {}
            return_response_achievements["name"] = data_achievements["name"]
            #print return_response_achievements["name"]

            return_response_achievements["description"] = {}
            return_response_achievements["description"] = data_achievements["description"]

            return_response_achievements["requirement"] = {}
            return_response_achievements["requirement"] = data_achievements["requirement"]

            return_response_achievements["type"] = {}
            return_response_achievements["type"] = data_achievements["type"]
            #print return_response_achievements
            yolo.append(return_response_achievements)


        return yolo


if __name__ == "__main__":
    api = None
    client = GwClient("Mesmer", api)
    print client.getprofession