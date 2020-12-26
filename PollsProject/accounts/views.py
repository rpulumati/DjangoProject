from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        firtName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        userName = request.POST['userName']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        # Validate password and confirmation password are same
        if password == confirmPassword:
            user = User.objects.create_user(username=userName, email=email, password=password, first_name=firtName,
                                            last_name=lastName)
            user.save()
            messages.info(request, f"{userName} created successfully")
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            messages.info(request, "confirmation password didn't match")
            return HttpResponseRedirect(reverse('accounts:register'))

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        print(userName)
        print(password)
        user = auth.authenticate(username=userName, password=password)

        if user is not None:
            print("user loged in")
            auth.login(request, user)
            messages.info(request, f"login successful for {user}")
            return HttpResponseRedirect(reverse('polls:home'))

        else:
            messages.info(request, f"login failed for {user}")
            return HttpResponseRedirect(reverse('accounts:login'))

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
