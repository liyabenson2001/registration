from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Registration,Login

# Create your views here.
def register(request):
    uform = UserCreationForm(request.POST)
    if request.method == "POST":
        if uform.is_valid():
            uname = uform.cleaned_data.get('username')
            pwd = uform.cleaned_data.get('password1')
            email = uform.cleaned_data.get('email')
            user1 = User.objects.create_user(username=uname, password=pwd, email=email)
            user1.save()
            user = authenticate(request, username=uname, password=pwd)
            login(request, user)
            return redirect('/app3/login/')
    else:
        uform = UserCreationForm()
    return render(request,'signup.html',{'form':uform})

def login0(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app3/home/')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request, 'login.html')

def show(request):
    return render(request,'welcome.html', {'username': request.user.username})
