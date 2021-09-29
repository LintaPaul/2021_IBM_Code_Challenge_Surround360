from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('usertype/',views.usertype, name="usertype"),
    path('public/',views.public, name="public"),
    path('official/',views.official,name="official"),
    path('form/',views.register,name="form"),
    path('login/',views.login_public,name="login"),
    path('home/',views.gotohome,name="home"),
<<<<<<< HEAD
    path('water/',views.gotocwater,name="water"),
    path('c_water/',views.file_water,name="c_water")
=======
    path('blog/', views.blog, name = "blog")
>>>>>>> 553312b60342296fcab40a7cd006271b93e01492
]

