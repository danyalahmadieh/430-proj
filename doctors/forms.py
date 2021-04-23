from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from Proj.models import  User, Doctors

class DoctorSignUpForm(UserCreationForm):
    d_name = forms.CharField(label= "Name:")
    d_email = forms.EmailField(label= "Email:")
    d_dob = forms.DateTimeField(label= "Date of Birth (YYYY-MM-DD):")
    d_yoe = forms.IntegerField(label = "Years of Experience: ")
    d_specialty = forms.CharField(label = "Specialty: ")
    d_availability = forms.CharField(label = "Availabilty (MWF): ")
    d_starthours = forms.TimeField(label ="Starting Hours: ")
    d_endhours = forms.TimeField(label ="Ending Hours: ")

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctors = True
        user.save()
        doctor = Doctors.objects.create(user=user)
        doctor.d_email = self.cleaned_data.get('d_email')
        doctor.d_name = self.cleaned_data.get('d_name')
        doctor.d_dob = self.cleaned_data.get('d_dob')
        doctor.d_specialty = self.cleaned_data.get('d_specialty')
        doctor.d_yoe = self.cleaned_data.get('d_yoe')
        doctor.save()
        return user
