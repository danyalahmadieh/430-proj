from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	is_patients = models.BooleanField(default=False)
	is_doctors = models.BooleanField(default=False)
class Patients(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        p_name = models.CharField(max_length=30)
        p_email = models.EmailField
        p_dob = models.DateTimeField
        p_phone = models.CharField(max_length=15)
class Doctors(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        d_yoe = models.IntegerField
        d_specialty = models.CharField(max_length=20)
        d_availability = models.CharField(max_length=7)
        d_starthours = models.TimeField
        d_starthours = models.TimeField