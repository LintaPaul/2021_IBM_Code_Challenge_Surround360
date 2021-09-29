from django.contrib import admin


# Register your models here.
from .models import Official,Public

admin.site.register(Official)
admin.site.register(Public)