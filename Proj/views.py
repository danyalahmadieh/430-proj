from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import patient_required
from django.contrib.auth.forms import UserCreationForm
from .models import User

def mainpage(request):
        return render(request,'homepage.html')
@login_required
def common_view(request):
    if patient_required:
        return render(request,'home(p).html')
    else:
        return render(request,'home(d).html')