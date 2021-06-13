from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    path('<slug:category_slug>/', views.shop, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
