from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from Proj.models import Patients, User

class PatientSignUpForm(UserCreationForm):
    p_name = forms.CharField(label= "Name:")
    p_email = forms.EmailField(label= "Email:")
    p_dob = forms.DateTimeField(label= "Date of Birth (YYYY-MM-DD):")
    p_phone = forms.CharField(label= "Phone #: ")

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patients = True
        user.save()
        patient = Patients.objects.create(user=user)
        patient.p_email = self.cleaned_data.get('p_email')
        patient.p_name = self.cleaned_data.get('p_name')
        patient.p_dob = self.cleaned_data.get('p_dob')
        patient.p_phone = self.cleaned_data.get('p_phone')
        patient.save()
        return user
          