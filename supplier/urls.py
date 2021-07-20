from django.urls import path
from . import views
app_name = 'supplier'

urlpatterns = [
    path('', views.supplier_list, name='list'),
    path('supplier_create/', views.supplier_create, name='create')
]