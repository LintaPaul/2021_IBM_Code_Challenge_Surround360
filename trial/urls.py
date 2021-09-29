from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('usertype/',views.usertype, name="usertype"),
    path('public/',views.public, name="public"),
    path('official/',views.official,name="official"),
    path('form/',views.register,name="form"),
    path('login/',views.login_public,name="login"),
    path('login_official/',views.login_official,name="login"),
    path('home/',views.gotohome,name="home"),
    path('blog/', views.blog, name = "blog"),
    path('officialhome/', views.officialLanding, name = "officialhome"),

]

