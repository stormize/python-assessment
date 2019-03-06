from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from django.contrib.auth.decorators import login_required
import json
import requests
from django.contrib.auth.models import User
# Create your views here.
1478963

@login_required(login_url='/signin/')
def app(request):
     url="http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1"
     r=requests.get(url)
     r=r.json()[0]
     return render(request,'app/app.html',{'content':r['content'],'title':r['title']})

def profile(request):
     data ={
     'firstname' : User.objects.filter(username=request.user.username).exclude(first_name='').values_list('first_name', flat=True)[0],
     'lastname' : User.objects.filter(username=request.user.username).exclude(last_name='').values_list('last_name', flat=True)[0],
     'email' :  User.objects.filter(username=request.user.username).exclude(email='').values_list('email', flat=True)[0],
     'ip' : request.META['REMOTE_ADDR'],
     'browser' : request.META['HTTP_USER_AGENT'],
     'os':request.META['OS']
     }
     
     return render(request,'app/profile.html',data)
