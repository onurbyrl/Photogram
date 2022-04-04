from django.shortcuts import render
from users.forms import SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def home(request):

    return render(request, 'index.html', {})

def register(request):
    registered = False

    if request.method == 'POST':
        registration_form = SignUpForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            return render(request, 'auth/register.html', {
                'registration_form': registration_form
            })
        
    else:
        registration_form = SignUpForm()

    return render(request, 'auth/register.html', {
        'registration_form': registration_form,
        'registered': registered
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('users:home'))

        else:
            print("bir hata oluştu")
            return HttpResponse('bir hata oluştu')

    else:
        return render(request, 'auth/login.html', {})
    

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('users:home'))