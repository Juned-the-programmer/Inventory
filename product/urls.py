from django.urls import path
from . import views

urlpatterns = [
    path('addproduct', views.addproduct, name="addproduct"),
    path('viewproducts', views.viewproducts, name="viewproducts"),
    path('updateproduct', views.updateproduct, name="updateproduct")
]
