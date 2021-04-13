from django.urls import path
from django.contrib import admin
from . import views
from patients import views as p_views
urlpatterns = [
 path('', views.signup,name ='index'),
 path('signup/', p_views.SignUpView.as_view(), name='student_signup'),
]
