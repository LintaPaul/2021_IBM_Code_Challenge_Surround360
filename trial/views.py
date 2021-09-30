from django.shortcuts import render,get_object_or_404  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Public
from .forms import Usertype,Newuser,Loggeduser,Complaints
from .models import Public, Official, Complaints
from .forms import Usertype,Newuser,Loggeduser, LoggedOfficial
from django.contrib import messages
from django.contrib.auth import logout

def index(request):  
  return render(request,'index.html')  

def public(request):
  return render(request,'login_Public.html')

def official(request):
  return render(request,'login_Official.html')

def logOut(request):
  logout(request)
  return HttpResponseRedirect('/trial/index/')


def gotoregister(request):
  return render(request, 'register_public.html')

def gotohome(request):
  return render(request, 'dashboard_public.html')
  
def gotocwater(request):
  luser=request.session.get('user')
  return render(request, 'complaints_water.html',{'user':luser})

def gotocelec(request):
  luser=request.session.get('user')
  return render(request, 'complaints_elec.html',{'user':luser})

def gotocroads(request):
  luser=request.session.get('user')
  return render(request, 'complaints_road.html',{'user':luser})


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
        request.session['user']=name
        return render(request,'dashboard_public.html',{'user': user_object})
      else:
        messages.success(request,'Invalid Login')
        return HttpResponseRedirect('/trial/index/')
    else:
        mydetails=Loggeduser()
  return HttpResponseRedirect('/trial/index/')

def file_water(request):
    if request.method=="POST":
      form=Complaints(request.POST)
      if form.is_valid():
        form.save()
      else:
        form=Complaints()
      messages.success(request,"Complaint filed")
    return HttpResponseRedirect('/trial/water/')


  
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
      try:
        official_object = Official.objects.filter(name = name, empid=eid )
      except Official.DoesNotExist:
        official_object = None
      if official_object:
        # messages.success(request, 'Login Successfull!')
        request.session['eid'] = eid
        return render(request,'landing_official.html',{'user': official_object})
      else:
        messages.warning(request, f'Invalid Login')
        return HttpResponseRedirect('/trial/index/')
    else:
      details = LoggedOfficial()
  return HttpResponseRedirect('/trial/index/')
    
def complaints(request):
  off = request.session.get('eid')
  official_obj = Official.objects.filter(empid = off)
  for o in official_obj:
    dept = o.department
    subdept = o.subdept
    context = {
      'complaints': Complaints.objects.filter(dept = dept, category = subdept)
    }
    
  return render(request, 'view_complaints.html', context)

