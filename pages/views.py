from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_login = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user_login is not None:
            auth.login(request, user_login)
            return redirect('dashboard')

    return render(request, "pages/login.html")