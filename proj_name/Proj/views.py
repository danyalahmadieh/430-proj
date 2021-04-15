from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	form = UserCreationForm()
	return render(request, 'index.html',{'form':form})

def home(request):
    return render(request, 'home.html')