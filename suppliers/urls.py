from django.urls import path
from . import views

urlpatterns = [
    path('suppliers', views.viewsupplier, name="viewsupplier"),
    path('addsupplier', views.addsupplier, name="addsupplier"),
    path('updatesupplier', views.updatesupplier, name="updatesupplier")
]
