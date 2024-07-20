from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Customer

# Create your views here.
def customerlogin(request):
    return render(request, "customerlogin.html")

def customerregister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile completion view
    else:
        form = RegistrationForm()
    return render(request, 'customerreg.html', {'form': form})
