from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.middleware import csrf
from django.shortcuts import render, redirect ,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth,sessions
from django.contrib.auth import authenticate,login,logout,user_logged_in
#def signup(request):
#   if request.method == 'POST':
#      form = UserCreationForm(request.POST)
#      if form.is_valid():
#       form.save()
#      username = form.cleaned_data.get('username')
#      raw_password = form.cleaned_data.get('password1')
#      user = authenticate(username=username, password=raw_password)
#      login(request, user)
#      return redirect('home')
#   else:
#        form = UserCreationForm()
#        return render(request, 'login.html', {'form': form})
from django.urls import reverse


def user_create_success(request):
    return render_to_response('auth/create_success.html')


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        context["user"]=request.user
        if user is not None:
            if user.is_authenticated:
                print("1")
                login(request, user)
                if request.GET.get('next',None):
                    print("2")
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('article:articles'))
            else:
                print("3")
                context["error"] = "nieprawidlowe dane"
                return render(request,'auth/login.html',context)
        else:
            context["error"] = "nieprawidlowe dane"
            return render(request, 'auth/login.html', context)
    else:
        print("4")
        return render(request,'auth/login.html',context,)


def success(request):
    c = {}
    c['user'] = request.user
    return render(request,'auth/success.html',c)


def tes(request):
    return render_to_response('test.html')

def user_logout(request):
        auth.logout(request)
        return render_to_response('auth/logout.html')


def user_create(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_create_success'))
    else:
        form = UserCreationForm()
    return render(request,'auth/create.html',{'user': request.user,'form':form})

def test(request):
    print(request.user.is_authenticated)
    return render(request,'main.html')