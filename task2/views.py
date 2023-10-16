from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password == password2:
            if Profile.objects.filter(email=email).exists():
                messages.info(request, "Email Exists")
                return redirect("/signup")
            elif Profile.objects.filter(name=username).exists():
                messages.info(request, "Username Exists")
                return redirect("/signup")
            else:
                user = Profile.objects.create(
                    name=username, password=password, email=email
                )
                user.save()
                return redirect("/")
        else:
            messages.info(request, "Password Not Matching")
            return redirect("/signup")
    else:
        return render(request, "task2/signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = Profile.objects.filter(name=username, password=password).exists()
        if user == True:
            user_login = Profile.objects.get(name=username)
            if user_login is not None:
                return render(request, "task2/profile.html", {"user_login": user_login})
            else:
                messages.info(request, "Invalid Credentials")
                print("")
                return redirect("/task2/login")

    return render(request, "task2/login.html")
