from django.shortcuts import render

# Create your views here.
def addproduct(request):
    return render(request, "product/addproduct.html")

def viewproducts(request):
    return render(request, "product/viewproducts.html")

def updateproduct(request):
    return render(request, "product/updateproduct.html")