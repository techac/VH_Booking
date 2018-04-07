from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import myregistrationform,PostForm
from .models import Post
# Create your views here.
def signup_view(request):
    if(request.method=='POST'):
        form=myregistrationform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')
    else:
        form=myregistrationform()
    return render(request,"signup.html",{'form':form})

@login_required(login_url="/accounts/login/")
def index(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/waiting')
    else:
        form=PostForm()
    return render(request,"index.html",{'form':form})


def login_view(request):
    if(request.method=='POST'):
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            print(user)
            # return HttpResponseRedirect('/accounts/signup/')

            return HttpResponseRedirect('/index')
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{'form':form})

def logout_view(request):
    if(request.method=='POST'):
        logout(request)
        return HttpResponseRedirect('/index')

def base(request):
    return render(request,"base.html",{})

def waiting(request):
        return render(request,"waiting.html",{})


def list(request):
    query_set =Post.objects.all()
    context={
        "object_set":query_set,
    }
    return render(request,"list.html",context)