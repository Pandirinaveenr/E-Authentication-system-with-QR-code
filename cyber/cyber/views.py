from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 
from user.models import *

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, "index.html")

def adminslogin(request):
    return render (request, 'adminlogin.html')

def adminsloginaction(request):
    if request.method == 'POST':
        uname=request.POST['admin']
        passwd=request.POST['admin']
        if uname =='admin' and passwd =='admin':
            return render(request,"admin/adminenter.html")
        else:
            messages.error(request,"Invalid Credentials")
            return render(request,"adminlogin.html")
    return render(request, "admin/adminenter.html")

def adminhome(request):
    return render(request, "admin/adminenter.html")

def ShowUsers(request):
    hsp=usermodel.objects.all()
    return render(request, 'admin/usersdata.html',{"data":hsp})

def adminlogout(request):
    return render(request, "adminlogin.html")

def deleteuser(request):
    return render(request, 'admin/deleteuser.html')

def deleteuser1(request):
    id=request.POST['name']
    usermodel.objects.filter(name=id).delete()
    return ShowUsers(request)

def updateuser1(request):
    return render(request, 'admin/update.html')

def updateuser(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phonenumber']
        images=request.POST['image']
        user=usermodel.objects.filter(name=name).update(email=email, password=password, phone=phone, images=images)
        return ShowUsers(request)

def adduser(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phonenumber']
        images=request.POST['image']
        user=usermodel(email=email, password=password, name=name, phone=phone, images=images)
        user.save()
        messages.success(request,"User Added Successfully")
        return render(request, 'admin/adduser.html')
    else:
        return render(request, 'admin/adduser.html')
