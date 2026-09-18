from django.shortcuts import render,redirect
from Tracker.form import User_Form,Job_Form
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Tracker.models import Job_detail,User_Model
from django.contrib.auth.models import User



# Create your views here.

def registration(request):
    registered=False
    if request.method=='POST':
        form=User_Form(request.POST)
        if form.is_valid():
            print('DONE')
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()
            User_Model.objects.create(
                user=user
            )
            registered=True
    else:
        form=User_Form()
    return render(request,'registration.html',{'form':form,'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print(user)
        print(User_Model.objects.all())
        if User_Model.objects.filter(user=user):
            print(user)
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'User is in-active'})
        else:
            return render(request,'login.html',{"error":"Invalid credentails"})

    return render(request,'login.html',{})


@login_required(login_url=user_login)
def home(request):

    form=Job_detail.objects.filter(user=request.user)
    return render(request,'home.html',{'form':form})

@login_required(login_url=user_login)
def user_logout(request):
    logout(request)
    return redirect(user_login)

@login_required(login_url=user_login)
def add_job(request):
    if request.method=='POST':
        company_name=request.POST['comapanyname']
        job_title=request.POST['jobtitle']
        desgination=request.POST['desgination']
        application_date=request.POST['applicationdate']
        status=request.POST['status']
        location=request.POST['location']
        salary=request.POST['salary']
        print(company_name)

        Job_detail.objects.create(
            user=request.user,
            company_name=company_name,
            job_title=job_title,
            location=location,
            application_date=application_date,
            status=status,
            salary=salary,
            desgination=desgination
        )
        print(company_name)
        return redirect('home')
    return render(request,'add_job.html')

@login_required(login_url=user_login)
def delete_(request,id):
    item=Job_detail.objects.get(id=id)
    item.delete()
    return redirect('home')


@login_required(login_url=user_login)
def edit(request,id):
    form=Job_detail.objects.get(id=id)

    if request.method=='POST':
        status=request.POST['status']
        Job_detail.objects.filter(id=id).update(status=status)
        return redirect('home')
    return render(request,'edit.html',{'form':form})
