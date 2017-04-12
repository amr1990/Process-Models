from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
import requests
import json
import sys

from models import Inventory, UserProfile

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response
from forms import UserForm
from django.template import RequestContext
from models import Bank, Inventory


URL = "https://api.guildwars2.com/v2/"
url_services = {
    "token": "?access_token=",
    "professions": "professions/",
    "account": "account/",
    "inventory": "inventory",
    "character": "characters/",
    "items": "items/",
    "achievements": "achievements",
    "daily": "/daily",
}


@csrf_exempt
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'registration/register.html',
            {'user_form': user_form, 'registered': registered},
            context)



def homepage(request):
    context = RequestContext(request)
    return render_to_response("homepage.html", context)


@property
def getProfession():
    url = URL + url_services["professions"] + self.profession
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


def getInventory(DetailView, api):
    model = Inventory
    url = URL + url_services["character"] + "Unvintuh Hamsahaha/" + url_services[
        "inventory"] + url_services["token"] + api
    req_inventory = requests.get(url)
    data_inventory = json.loads(req_inventory.text)
    return_response_inventory = []

    for bag in data_inventory["bags"]:
        for item in bag["inventory"]:
            if item:
                url_items = URL + url_services["items"] + str(item["id"])
                req_items = requests.get(url_items)
                data_items = json.loads(req_items.text)
                itemname = data_items["name"]
                return_response_inventory.append((itemname, item["count"]))

    model.setitem(return_response_inventory)

    return return_response_inventory


def getDailyAchievement(request):
    context = RequestContext(request)
    token = "?id="
    URL_daily = URL + url_services["achievements"] + url_services["daily"]
    req_daily = requests.get(URL_daily)
    data_daily = json.loads(req_daily.text)
    dailies = []
    return_response = []
    dailies.append(data_daily["pve"])
    dailies.append(data_daily["pvp"])
    dailies.append(data_daily["wvw"])
    dailies.append(data_daily["fractals"])

    for i in dailies:
        for j in i:
            URL_achi = URL + url_services["achievements"] + token + str(j["id"])
            #print URL_achi
            req_achi = requests.get(URL_achi)
            data_achi = json.loads(req_achi.text)
            return_response.append((data_achi["name"], data_achi["requirement"]))

    return render_to_response(
        'daily.html',
        {'achievements': return_response},
        context)

@login_required
def getCharacterList(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.filter(user=user).get()
        api = profile.apikey
    URL_char = URL + url_services["character"] + url_services["token"] + str(api)
    req_char = requests.get(URL_char)
    data_char = json.loads(req_char.text)

    return render_to_response(
        'characters.html',
        {'characters': data_char},
        context)

