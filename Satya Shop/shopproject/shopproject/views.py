from django.http import HttpResponse
from django.shortcuts import redirect,render

def landingpage(request):
    return render(request, "landing.html")
def homepage(request):
    return render(request, "home.html")

def loginpage(request):
    return render(request, "login.html")

def signuppage(request):
    return render(request, "signup.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")