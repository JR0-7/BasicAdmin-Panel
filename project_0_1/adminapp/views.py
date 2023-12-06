from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db.models import Q
# Create your views here.

@never_cache
def adminpage(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            search_word = request.POST.get('search-box', '')
            data = User.objects.filter(Q(username__icontains=search_word)| Q(email__icontains=search_word)).order_by('id').values()
        else:
            data = User.objects.all().order_by('id').values()
        context={'frm': data}
        return render(request, 'user_table.html', context=context)
    return redirect('tablepage')


    # data =User.objects.all().order_by("id").values()
    # context={'frm':data}
    # print(context)
    # return render(request,"user_table.html", context=context)
    

@never_cache
def editpage(request,id):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password2 = request.POST.get('password1')
        password1 = make_password(password2,salt=None,hasher="pbkdf2_sha256")

        if User.objects.exclude(id=id).filter(username=username).exists():
            messages.add_message(request,messages.WARNING,"Username Already Exist!")
        elif User.objects.exclude(id=id).filter(email=email).exists():
            messages.add_message(request,messages.WARNING,"Email Already Exist!")
        else:
            edit=User.objects.get(id=id)
            edit.username=username
            edit.email=email
            edit.password=password1
            edit.save()
            return redirect("tablepage")

    d = User.objects.get(id=id)
    context = {'d':d}
    return render(request,"edit.html",context )



def delete_record(request,id):
    # if request.user.is_authenticated:
    #     return redirect('adduser')
    delete_it = User.objects.get(id=id)
    delete_it.delete()
    messages.success(request,"Record Deleted Sucessfully...")
    return redirect("tablepage")

@never_cache
def adduser(request):
    # if request.user.is_authenticated:
    #     return redirect('adduser')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        
        if User.objects.filter(username=username):
            messages.add_message(request,messages.WARNING,"Username Already Exist!")
        elif User.objects.filter(email=email):
            messages.add_message(request,messages.WARNING,"Email Already Exist!")
        else:
            password1 = make_password(password1,salt=None,hasher="pbkdf2_sha256")
            user = User(username=username,email=email,password=password1)
            user.save()
            return redirect('loginpage')
    return render(request,'add_user.html')