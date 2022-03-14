from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/create/', views.CreateProductView.as_view(), name='create_product'),
    path('product/list/', views.ListProductView.as_view(), name='list_product'),
    path('product/<int:pk>', views.DetailProductView.as_view(), name='detail_product'),
]
