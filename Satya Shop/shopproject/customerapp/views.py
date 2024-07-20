from django.shortcuts import render

# Create your views here.
def customerlogin(request):
    return render(request, "customerlogin.html")