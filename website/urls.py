from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('site/<slug:guess>', views.HomeView.as_view(), name='site_home'),

]
