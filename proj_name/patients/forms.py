from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from Proj.models import Patients, User

class PatientSignUpForm(UserCreationForm):
    p_name = forms.CharField()
    p_email = forms.EmailField()
    p_dob = forms.DateTimeField()
    p_phone = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patients.objects.create(user=user)
        patient.p_email.add(*self.cleaned_data.get('p_email'))
        patient.p_name.add(*self.cleaned_data.get('p_name'))
        patient.p_dob.add(*self.cleaned_data.get('p_dob'))
        patient.p_phone.add(*self.cleaned_data.get('p_phone'))
        return user