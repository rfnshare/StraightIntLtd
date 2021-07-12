from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ProtectView.as_view(), name='index'),

]
