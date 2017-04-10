from django.contrib.auth.models import User
from django.shortcuts import render
import requests
import json

from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response
from forms import UserForm
from django.template import RequestContext
from models import Bank, Inventory



def homepage(request):
    context = RequestContext(request)
    return render_to_response("base.html", context)

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



'''class GwClient(object):
    URL = "https://api.guildwars2.com/v2/"
    url_services = {
        "professions": "professions/"
    }

    def __init__(self, professionname, apikey):
        super(GwClient, self).__init__()
        self.profession = professionname
        self.apikey = apikey


    @property
    def getProfession(self):
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
'''

if __name__ == "__main__":
    api = None
    #client = GwClient("Mesmer", api)