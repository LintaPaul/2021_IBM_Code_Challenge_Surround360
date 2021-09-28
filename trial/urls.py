from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('usertype/',views.usertype, name="usertype"),
    path('public/',views.public, name="public"),
    path('official/',views.official,name="official"),
]

