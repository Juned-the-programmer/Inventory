from django.shortcuts import render

# Create your views here.
def addcustomer(request):
    return render(request, "customer/addcustomer.html")

def viewcustomer(request):
    return render(request, "customer/viewcustomers.html")

def updatecustomer(request):
    return render(request, "customer/addcustomer.html")