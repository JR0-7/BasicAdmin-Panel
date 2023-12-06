from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

@never_cache
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  
        
        user = authenticate(request,username=username,password=password) 
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,('There Was An Error Loggin In, Try Again...'))
            return redirect('loginpage')
    else:
        return render(request,'login.html')


@never_cache
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,("You Were Logged Out!"))
    return redirect(loginpage)

@never_cache
def signpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.add_message(request,messages.WARNING,"Username Already Exist!")
            elif User.objects.filter(email=email):
                messages.add_message(request,messages.WARNING,"Email Already Exist!")
            else:
                password1 = make_password(password1,salt=None,hasher="pbkdf2_sha256")
                user = User(username=username,email=email,password=password1)
                #user = authenticate(request,username=username,password1=password2)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            messages.add_message(request,messages.WARNING,"Password not match")
    return render(request,'signup.html')
    


@never_cache
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("/useradmin")
        return render(request,"home.html")
    return redirect(loginpage)



