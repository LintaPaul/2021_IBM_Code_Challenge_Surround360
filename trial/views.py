from django.shortcuts import render,get_object_or_404  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Public
from .forms import Usertype,Newuser,Loggeduser,Complaintform
from .models import Public, Official, Complaints, Tourist
from .forms import Usertype,Newuser,Loggeduser, LoggedOfficial,BlogPost
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
  return HttpResponseRedirect('/trial/login/')
  
def gotocwater(request):
  luser=request.session.get('user')
  return render(request, 'complaints_water.html',{'user':luser})

def gotocelec(request):
  luser=request.session.get('user')
  return render(request, 'complaints_elec.html',{'user':luser})

def gotocroads(request):
  luser=request.session.get('user')
  return render(request, 'complaints_road.html',{'user':luser})

def gotosearch(request):
  return render(request, 'search.html')

def officialLanding(request):
  return render(request, 'landing_official.html')

def register(request):
  if request.method=="POST":
    form=Newuser(request.POST)
    if form.is_valid():
      form.save()
    else:
      form=Newuser()
  return render(request,'login_Public.html')

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
        try:
          scomp=Complaints.objects.filter(sender=name,status='S').count()
          uncomp=Complaints.objects.filter(sender=name,status='US').count()
        except Complaints.DoesNotExist:
          scomp= None
        return render(request,'dashboard_public.html',{'user': user_object,'solved':scomp,'unsolved':uncomp})
      else:
        messages.success(request,'Invalid Login')
        return HttpResponseRedirect('/trial/index/')
    else:
        mydetails=Loggeduser()
  return HttpResponseRedirect('/trial/index/')

def file_water(request):
    if request.method=="POST":
      form=Complaintform(request.POST,initial={'status':"US"})
      print(form)
      if form.is_valid():
        form.save()
        messages.success(request,"Complaint filed")
      else:
        form=Complaintform()
      
    return HttpResponseRedirect('/trial/water/')

def file_elec(request):
    if request.method=="POST":
      form=Complaintform(request.POST,initial={'status':"US"})
      print(form)
      if form.is_valid():
        form.save()
        messages.success(request,"Complaint filed")
      else:
        form=Complaintform()
      
    return HttpResponseRedirect('/trial/elec/')

def file_road(request):
    if request.method=="POST":
      form=Complaintform(request.POST,initial={'status':"US"})
      print(form)
      if form.is_valid():
        form.save()
        messages.success(request,"Complaint filed")
      else:
        form=Complaintform()
      
    return HttpResponseRedirect('/trial/road/')
  
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
    region = o.region
    context = {
      'complaints': Complaints.objects.filter(dept = dept, category = subdept, region = region)
    }
    
  return render(request, 'view_complaints.html', context)

def solvedcomplaints(request):
  off = request.session.get('eid')
  official_obj = Official.objects.filter(empid = off)
  for o in official_obj:
    dept = o.department
    subdept = o.subdept
    region = o.region
    context = {
      'complaints': Complaints.objects.filter(dept = dept, category = subdept, region = region)
    }
    
  return render(request, 'view_solved_complaints.html', context)

def success(request):
  return render(request, 'success.html')

def officialProfile(request):
  off = request.session.get('eid')
  official_obj = Official.objects.filter(empid = off)
  for o in official_obj:
    name = o.name
    d = o.department
    subd = o.subdept
    score = o.score
  
  if d == 'W':
    dept = 'Water'
  elif d == 'E':
    dept = 'Electricity'
  else:
    dept = 'Roads'
  
  if subd == 'WL':
    subdept = 'Water Leaks'
  elif subd == 'SL':
    subdept = "Shortage of Supply"
  elif subd == 'PF':
    subdept = "Power failure"
  elif subd == 'LB':
    subdept = "Line damage"
  elif subd == 'RD':
    subdept = "Road damage"
  elif subd == 'TR':
    subdept = "Tarring required"
  else:
    subdept = 'Unspecified'
  return render(request, 'officialprofile.html', {'name':name, 'dept':dept, 'subdept':subdept, 'score':score})

def changestatus(request, id):
  off = request.session.get('eid')
  score = Official.objects.get(empid = off).score
  Official.objects.filter(empid = off).update(score = score+1)
  Complaints.objects.filter(id = id).update(status = 'S')
  return HttpResponseRedirect('/trial/viewcomplaints/')

def addpost(request):
  if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           messages.success(request,"Blog posted!!! Thank you")
           return HttpResponseRedirect('/trial/success/')
        else:
          form=BlogPost()
  return HttpResponseRedirect('/trial/blog/')

def search(request):
  value = request.POST.get('location')
  # location_obj = tourist.objects.filter(location = value)
  context = {
    'blogs' : Tourist.objects.filter(location__icontains = value),
  }
  return render(request, 'blogView_new.html', context)
  