from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User,Patients,Doctors,Meeting
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Meeting)
admin.site.register(User,UserAdmin)