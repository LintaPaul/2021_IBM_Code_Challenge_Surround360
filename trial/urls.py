from django.urls import path
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    #path('usertype/',views.usertype, name="usertype"),
    #path('public/',views.public, name="public"),
    #path('official/',views.official,name="official"),
    path('form/',views.gotoregister,name="form"),
    path('register/',views.register,name="register"),
    path('login/',views.login_public,name="login"),
    path('officialhome/',views.login_official,name="officialhome"),
    path('logout/', views.logOut, name = 'logout'),
    path('home/',views.gotohome,name="home"),
    path('water/',views.gotocwater,name="water"),
    path('elec/',views.gotocelec,name="elec"),
    path('road/',views.gotocroads,name="roads"),
    path('cwater/',views.file_water,name="cwater"),
    path('celec/',views.file_elec,name="celec"),
    path('croad/',views.file_road,name="croad"),
    path('blog/', views.blog, name = "blog"),
    path('viewcomplaints/', views.complaints, name = 'viewcomplaints'),
    path('view_solved_complaints/', views.solvedcomplaints, name = 'viewsolvedcomplaints'),
    path('success/', views.success, name = "success"),
    path('changestatus/<int:id>', views.changestatus, name = 'changestatus'),
    path('official/Profile/', views.officialProfile, name = 'officialProfile'),
    path('postadd/',views.addpost,name="postadd"),
    path('search/', views.gotosearch, name = "search"),
    path('neighbourhood/search/', views.search, name = "neighbourhoodSearch"),
    path('backhome/',views.gobackdashboard, name="backhome"),
    path('backofhome/',views.gobackofficial,name="backofhome"),
    path('contact/<str:name>', views.contact, name = "contact"),
]

