from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('usertype/',views.usertype, name="usertype"),
    #path('public/',views.public, name="public"),
    #path('official/',views.official,name="official"),
    path('form/',views.register,name="form"),
    path('login/',views.login_public,name="login"),
    path('login_official/',views.login_official,name="officialhome"),
    path('officialhome/',views.login_official,name="officialhome"),
    path('logout/', views.logOut, name = 'logout'),
    path('home/',views.gotohome,name="home"),
    path('water/',views.gotocwater,name="water"),
    path('elec/',views.gotocelec,name="elec"),
    path('road/',views.gotocroads,name="roads"),
    path('complaints/',views.file_water,name="complaints"),
    path('blog/', views.blog, name = "blog"),
    path('viewcomplaints/', views.complaints, name = 'viewcomplaints'),
    path('view_solved_complaints/', views.solvedcomplaints, name = 'viewsolvedcomplaints'),
    path('success/', views.success, name = "success"),
    path('changestatus/<int:id>', views.changestatus, name = 'changestatus'),
    path('official/Profile/', views.officialProfile, name = 'officialProfile'),


]

