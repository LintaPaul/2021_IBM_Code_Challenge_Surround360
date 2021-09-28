from django import forms
USER_CHOICES= [
    ('public', 'Public'),
    ('official', 'Official'),
    ]
class Usertype(forms.Form):
    usertype= forms.CharField(label='Select your user type', widget=forms.Select(choices=USER_CHOICES))
