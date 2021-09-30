from django.contrib import admin


# Register your models here.
from .models import Official,Public,Complaints,Tourist

admin.site.register(Official)
admin.site.register(Public)
admin.site.register(Complaints)
admin.site.register(Tourist)