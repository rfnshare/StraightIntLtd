from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.CustomerCreateView.as_view(), name='create_customer'),
    path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer_details/<str:pk>/', views.CustomerDetailsView.as_view(), name='customer_details'),
    path('customer_edit/<str:pk>/', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer_delete/<str:pk>/delete', views.CustomerDeleteView.as_view(), name='customer_delete'),
]
