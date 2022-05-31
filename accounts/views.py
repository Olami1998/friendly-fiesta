#from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(repuest):
    return HttpResponse("<p> signup here <p/>")

def login(request):
    return HttpResponse("<b> login here <b/>")

#templates/accounts/index.html
#templates/home/index.html


#static/home/style.css, toggle.js, background-image.jpeg