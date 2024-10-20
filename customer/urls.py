from django.urls import path
from . import views

urlpatterns = [
    path('customers', views.viewcustomer, name="viewcustomer"),
    path('addcustomer', views.addcustomer, name="addcustomer"),
    path('updatecustomer', views.updatecustomer, name="updatecustomer")
]
