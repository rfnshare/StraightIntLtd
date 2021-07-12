from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='home'),

]
