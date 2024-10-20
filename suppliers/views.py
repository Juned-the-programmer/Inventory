from django.shortcuts import render

# Create your views here.
def addsupplier(request):
    return render(request, "suppliers/addsupplier.html")

def viewsupplier(request):
    return render(request, "suppliers/viewsupplier.html")

def updatesupplier(request):
    return render(request, "suppliers/updatesupplier.html")