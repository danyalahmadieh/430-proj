from django.contrib import admin

from django.contrib import admin
from .models import User,Patients,Doctors

admin.site.register(User)
admin.site.register(Patients)
admin.site.register(Doctors)