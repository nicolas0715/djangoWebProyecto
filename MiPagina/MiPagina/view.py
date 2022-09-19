from django.shortcuts import render
from Farmacia.views import *


def homepage(request):
    return render(request, "homepage.html")
