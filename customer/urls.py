from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.ProtectView.as_view(), name='index'),
    path('', views.create_customer, name='create_customer'),
    path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer_details/<str:pk>/', views.customerDetails, name='customer_details')

]
