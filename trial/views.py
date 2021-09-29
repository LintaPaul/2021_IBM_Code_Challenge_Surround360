from django.shortcuts import render,get_object_or_404  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Public, Official
from .forms import Usertype,Newuser,Loggeduser, LoggedOfficial
from django.contrib import messages

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

def gotohome(request):
  return render(request, 'dashboard_public.html')

def officialLanding(request):
  return render(request, 'landing_official.html')

def register(request):
  if request.method=="POST":
    form=Newuser(request.POST)
    if form.is_valid():
      form.save()
    else:
      form=Newuser()
  return render(request,'register_public.html')

def login_public(request):
  phno=0
  name="nill"
  if request.method=="POST":
    mydetails=Loggeduser(request.POST)
    if mydetails.is_valid():
      name=mydetails.cleaned_data['name']
      phno=mydetails.cleaned_data['phoneno']
      try:
        user_object = Public.objects.filter(name=name,phoneno=phno)
      except Public.DoesNotExist:
        user_object = None
      if user_object:
        messages.success(request,'Login successfull!!!')
        return render(request,'dashboard_public.html',{'user': user_object})
      else:
        messages.success(request,'Invalid Login')
        return HttpResponseRedirect('/trial/public/')
    else:
        mydetails=Loggeduser()
  return HttpResponseRedirect('/trial/public/')
  
def blog(request):
  return render(request, 'blog.html')

def login_official(request):
  name = 'nil'
  eid = 'nil'
  if request.method == 'POST':
    details = LoggedOfficial(request.POST)
    if details.is_valid():
      name = details.cleaned_data['name']
      eid = details.cleaned_data['eid']
      print(name, eid)
      try:
        official_object = Official.objects.filter(empid = eid, name = name)
      except Official.DoesNotExist:
        official_object = None
      if official_object is not None:
        messages.success(request, 'Login Successfull!')
        return HttpResponseRedirect('/trial/officialhome/')
      else:
        messages.warning(request, 'Invalid Login')
        return HttpResponseRedirect('/trial/official/')
    else:
      details = LoggedOfficial()
  return HttpResponseRedirect('/trial/official/')
    


