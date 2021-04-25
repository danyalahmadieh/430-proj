from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import DateInput
from datetime import datetime

from Proj.models import Patients, User, Doctors

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

class DoctorChoiceField(forms.Form):

    doctor = forms.ModelChoiceField(
        queryset=Doctors.objects.values_list("d_name", flat=True),
        empty_label=None
    )
    dates = forms.DateField(label = ('Date'), widget = forms.DateInput(attrs={'placeholder': 'YYYY/MM/DD', 'class': 'date',}))
    def clean_doctor(self):
        doctor = self.cleaned_data['doctor']
        return doctor

    def clean_dates(self):
        date1= self.cleaned_data['dates']
        x = datetime.compare(date1,datetime.now())
        if x<0:
            raise ValidationError("Invalid Date")
        x = date1.weekday()
        if x>4:
            raise ValidationError("You Have Chosen a Weekend")
        return self.cleaned_data['dates']

    def clean(self):
    	super().clean()
    	cc_myself = self.cleaned_data.get("cc_myself")