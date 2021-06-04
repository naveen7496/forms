 
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponse("Successfully Logged in")
        else:
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password Validation
        if password == password2:
            # check username
            if User.objects.filter(username=username):
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email,
                                                    password=password)
                    user.save()
                    return redirect('login')

        else:
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


