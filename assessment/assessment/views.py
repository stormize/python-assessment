from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import signUpForm
from django.core.mail import send_mail
from django.contrib.auth.models import User

def signUp(request):
   if request.method =="POST":
      form = signUpForm(request.POST)
      if form.is_valid():
        
        user =form.save()
        login(request,user)
        return redirect("myapp:app")
   else:
      form= signUpForm()
      print("bloop")
   return render(request,"registeration/signup.html",{'form':form})

def signIn(request):
   if request.method=="POST":
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request,user)
         request.session['ip']=request.META['REMOTE_ADDR']
         request.session['os']=request.META['OS']
         request.session['browser']=request.META['HTTP_USER_AGENT']
         if 'next' in request.POST:
            return redirect(request.POST.get('next'))
         return redirect("welcome")
   else:
      form=AuthenticationForm()
   return render(request,"registeration/signin.html",{'form':form} )

def signOut(request):
   if request.method=="POST":
    logout(request)
    return redirect("myapp:app")
@login_required(login_url='/signin/')
def welcome (request):
   return render(request,"registeration/welcome.html")

   
