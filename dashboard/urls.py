from django.urls import path
from . import views

app_name = 'dashboard_home'
urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('login/', views.login, name='dashboard_login'),

]
