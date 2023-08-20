from django.contrib import admin
from django.urls import path
from GeoTour import views
from . import views
urlpatterns = [
   path("",views.login, name='GeoTour'),
   path("login",views.login, name="Login"),
   path("profile",views.profile, name="Profile"),
   path("index",views.index, name='GeoTour'), 
   path("about",views.about, name='About'),
   path("service",views.service, name='Service'),
   path("register",views.register, name='Register'),
   path("detail",views.detail, name='Details'),
   path("logout",views.logout, name="Logout"),
]

