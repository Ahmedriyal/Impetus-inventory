from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, CreateUserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, auth

User = get_user_model()


# ------ User Sign Up View ------
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # form.save()
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email is already used")
                    return redirect('register')

                elif User.objects.filter(username=username).exists():
                    messages.error(request, "Username exist")
                    return redirect('register')

                else:
                    user = User.objects.create_user(username=username, email=email, password=password1, is_employee = True)
                    user.save()
                    username = form.cleaned_data.get('username')
                    group = Group.objects.get(name='Employee')
                    user.groups.add(group)
                    auth.login(request, user)

                    # messages.info(request, "User successfully created")
                    return redirect('dashboard')
            
            else:
                messages.error(request, "Password not matching")
                return redirect('register')
    else:
        form = CreateUserForm()
    context = {
        'form': form
        }
    return render(request, 'users/register.html', context)


# ------ User Login View ------
def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Wrong username or password")
    
    context = {'form': forms}
    return render(request, 'users/login.html', context)


# ------ User Logout View ------
def logout_page(request):
    logout(request)
    return redirect('login')
