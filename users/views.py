from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Profile
from quiz.models import Score
# Create your views here.
def register(request):
    if(request.method=="POST"):
        form=RegisterForm(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Welcome {username},your account is created')
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

def dashboard(request,id):
    user=User.objects.get(id=id)
    profile=Profile.objects.get(user=user)
    return render(request,'users/dashboard.html',{'profile':profile})

def about_me(request,id):
    profile=Profile.objects.get(id=id)
    return render(request,'users/about_me.html',{'profile':profile})

def score(request,id):
    profile=Profile.objects.get(user=id)
    score=Score.objects.filter(user=id)
    return render(request,'users/score.html',{'score':score,'profile':profile})