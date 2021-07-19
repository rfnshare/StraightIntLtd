from django.urls import path

from . import views

app_name = 'sell'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ProtectView.as_view(), name='index'),
    path('create_sell/', views.InvoiceCreateView.as_view(), name='create'),
    path('sell_list/', views.InvoiceListView.as_view(), name='list'),
    path('pdf/<str:pk>', views.some_view, name='pdf'),
]
