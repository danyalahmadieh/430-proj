from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Proj.models import User, Doctors
from Proj.decorators import patient_required
from .forms import PatientSignUpForm,DoctorChoiceField
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
        return redirect('home')

@login_required
@patient_required
def viewdoctors(request):
    doctor_list = DoctorChoiceField
    context = {
        'all_doctors':Doctors.objects.all(),
	'doctor_list':doctor_list,
    }
    return render (request,'book.html',context)

@login_required
@patient_required
def selectdoctor(request,doc):
   
    return render (request,'book.html',context)