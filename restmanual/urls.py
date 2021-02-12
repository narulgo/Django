from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('<int:pk>', views.product_detail),
    path('content', views.ProductList.as_view()),
    path('content/<int:pk>', views.ProductDetail.as_view())
]