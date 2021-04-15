from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from patients import views as p_views
urlpatterns = [
 path('signup/', p_views.SignUpView.as_view(), name='signup'),
path('',views.mainpage,name='home'),
path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='homepage.html'),name='logout'),
path('direct/',views.common_view,name='lg'),
path('book/',p_views.viewdoctors,name='book'),
]
