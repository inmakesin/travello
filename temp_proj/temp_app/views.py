from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Place, Team


# Create your views here.
def home(request, username=None):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    if User.objects.filter(username=username).exists():
        messages.info(request, "Username Taken")
        return redirect('register')

    return render(request, "index.html", {'result': obj, 'result1': obj1})
