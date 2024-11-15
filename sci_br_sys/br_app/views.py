from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as auth_login ,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_user(request):

    logout(request)
    return render(request,"index.html")