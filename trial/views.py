from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Public
from .forms import Usertype,Newuser
def index(request):  
  return render(request,'index.html')  

def public(request):
  return render(request,'login_Public.html')

def official(request):
  return render(request,'login_Official.html')

def usertype(request):
  type_sel="nill"
  if request.method == "POST":
    mytype=Usertype(request.POST)

    if mytype.is_valid():
      type_sel=mytype.cleaned_data['usertype']
      if type_sel=="Public":
        return HttpResponseRedirect('/trial/public/')
      elif type_sel=="Official":
        return HttpResponseRedirect('/trial/official/')
    else:
      mytype=Usertype()
    return HttpResponseRedirect('/trial/index/')
def gotoregister(request):
  return render(request, 'register_public.html')

def register(request):
  if request.method=="POST":
    form=Newuser(request.POST)
    if form.is_valid():
      form.save()
    else:
      form=Newuser()
  return render(request,'register_public.html')


