from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User,Patients,Doctors

admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(User,UserAdmin)