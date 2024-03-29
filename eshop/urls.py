from django.urls import path

from . import views

app_name = 'eshop'

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productDetail, name='prodCatdetail'),
]
