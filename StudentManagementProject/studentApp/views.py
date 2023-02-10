from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache, cache_control

from studentApp.models import City, Course, Student


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request,"register.html",{'data':''})


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def regdata_fun(request):
    UserName = request.POST['txtUserName']
    Email = request.POST['txtEmail']
    Password = request.POST['txtPassword']

    if User.objects.filter(Q(username=UserName) | Q(email=Email)).exists():
        return render(request, "register.html",{'data':'USerName and Email is already exists'})

    else:
        u1 = User.objects.create_superuser(username=UserName,email=Email,password=Password)
        u1.save()
        return redirect('log')



@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def login_fun(request):
    return render(request, "loging.html",{'data':''})


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logdata_fun(request):
    UserName = request.POST['txtUserName']
    Password = request.POST['txtPassword']
    user1 = authenticate(username = UserName,password = Password)  # authenticate:it will return user object when username and  password present in user table else it will return none.

    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request, "loging.html",{'data':'USer is not a superuser'})
    else:
        return render(request, "loging.html",{'data':'Enter proper user name and password'})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'City_Data':city,'Course_Data':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def readdata_fun(request):
    s1 = Student()
    s1.Name = request.POST['txtName']
    s1.Age = request.POST['txtAge']
    s1.Phno = request.POST['txtPhno']
    s1.City = City.objects.get(city_name = request.POST['ddlCity'])
    s1.Course = Course.objects.get(course_name = request.POST['ddlCourse'])
    s1.save()
    return redirect('add')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display_fun(request):
    s1 = Student.objects.all()
    return render(request,'display.html',{'data':s1})



@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()

    if request.method == 'POST':
        s1.Name = request.POST['txtName']
        s1.Age = request.POST['txtAge']
        s1.Phno = request.POST['txtPhno']
        s1.City = City.objects.get(city_name=request.POST['ddlCity'])
        s1.Course = Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')

    return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')