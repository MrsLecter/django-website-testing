from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def profiles(request):
    return render(request, 'users/profiles.html')


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        try:
            # check if user exist
            user = User.objects.get(username=username)
        except:
            messages.error(request, '[username] not exist')
            return redirect('')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # create session for user
            login(request, user)
            return redirect('profiles')
        else:
             messages.error(request, 'username or password is incorrect')
             return redirect('')
    return render(request, 'profiles/login_registry.html')

def logoutPage(request):
    logout(request)
    messages.error(request, 'user is logout successfully')
    return redirect('')