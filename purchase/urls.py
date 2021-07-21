from django.urls import path, include
from django.urls import path
from . import views

app_name = 'purchase'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.select_supplier, name='supplier_select'),
    path('create/<str:pk>', views.purchase_create, name='create'),
    path('list', views.purchase_list, name='list')

]
