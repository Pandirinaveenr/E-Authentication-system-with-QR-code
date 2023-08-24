"""cyber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cyber import views as admins
from user import views as usr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admins.index, name='index'),
    path('home/',admins.home, name="home"),
    path('adminslogin', admins.adminslogin, name='adminslogin'),
    path('adminsloginaction/',admins.adminsloginaction,name='adminsloginaction'),
    path('adminhome/',admins.adminhome,name='adminhome'),
    path('adminlogout/', admins.adminlogout,name='adminlogout'),
    path('ShowUsers/',admins.ShowUsers,name='ShowUsers'),
    path('adduser/',admins.adduser,name='adduser'),
    path('deleteuser/',admins.deleteuser,name='deleteuser'),
    path('deleteuser1/',admins.deleteuser1,name='deleteuser1'),
    path('updateuser1/',admins.updateuser1,name='updateuser1'),
    path('updateuser/',admins.updateuser,name='updateuser'),
    
    path('userlogin/',usr.userlogin, name='userlogin'),
    path('register/',usr.register, name='register'),
    path('userregister/',usr.userregister, name='userregister'),
    path('userlogincheck/',usr.userlogincheck, name='userlogincheck'),
    path('userhome/',usr.userhome,name='userhome'),
    path('userlogout/', usr.userlogout,name='userlogout'),
    path('usrfd/',usr.usrfd,name='usrfd'),
    path('facedetect/',usr.facedetect,name='facedetect'),
    path('otpcheck/',usr.otpcheck,name='otpcheck'),
    path('otpverify/',usr.otpverify, name='otpverify'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)