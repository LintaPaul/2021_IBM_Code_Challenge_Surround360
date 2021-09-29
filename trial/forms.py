from django import forms
from .models import Public,Complaints
USER_CHOICES= [
    ('public', 'Public'),
    ('official', 'Official'),
    ]
class Usertype(forms.Form):
    usertype= forms.CharField(label='Select your user type', widget=forms.Select(choices=USER_CHOICES))

class Newuser(forms.ModelForm):
    class Meta:
        model=Public
        fields=["name","phoneno","region",]
        labels={'name':"Name",'phoneno':"PhoneNumber",'region':"Region"}
        
class Loggeduser(forms.Form):
    name=forms.CharField(label="name")
    phoneno=forms.CharField(label="phoneno")

class Complaints(forms.ModelForm):
    class Meta:
        model=Complaints
        fields=["region","dept","category","complaint","status"]
        labels={'region':"Region",'dept':"Department",'category':"Sub Category",'complaint':"Complaint",'status':"status"}
        