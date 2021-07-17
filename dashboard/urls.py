from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('profile_update/<str:pk>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('profile_update/<str:pk>', views.profile_update, name='profile_update')
]
