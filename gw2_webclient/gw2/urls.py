from django.conf.urls import url
import views
from django.views.generic import DetailView, ListView, UpdateView
from models import Bank, Inventory



urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]