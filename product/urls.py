from django.urls import path

from . import views

app_name = 'product'
urlpatterns = [
    # path('', views.index, name='index'),
    path('create_product_category', views.create_product_category, name='create_category'),
    path('create_product', views.create_product, name='create'),
    path('product_list', views.product_list, name='list'),

]
