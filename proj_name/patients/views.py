from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import HttpResponse
from Proj.models import User
from .forms import PatientSignUpForm
from django.contrib.auth import login

class SignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Patients'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home for patients')