from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.ProtectView.as_view(), name='index'),
    path('', views.create_customer, name='create_customer'),
    path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer_details/<str:pk>/', views.CustomerDetails.as_view(), name='customer_details'),
    path('customer_edit/<str:pk>/', views.customer_edit.as_view(),name= 'customer_edit'),
    path('customer_delete/<str:pk>/', views.customer_delete.as_view(), name='customer_delete'),
    # path('customer_edit/<str:pk>/', views.cuEdit, name='customer_edit'),
    # path('customer_delete/<str:pk>/', views.cuDelete, name='customer_delete')
    

]
