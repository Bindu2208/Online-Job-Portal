from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from App.models import Job
from Users.models import CustomUser
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
from django.shortcuts import  render, redirect
from .models import Apply, Job

def home(request):
    return render(request,'home.html')


def nav(request):
    return render(request,'navigation.html')


def login_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        
        role=request.POST.get("role")
        # print(email, password)

        user = authenticate(request, email=email, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            # print(user.role)
            print("Login Success")
            if role =='jobseeker':
                return redirect("jobdash")
            #kovuribindusree2003@gmailcom-2208
            else:
                return redirect("employdash")
            #User2@gmail.com - 2208
        else:
            # return redirect("employdash")
            print("Login Failed")
    return render(request,'login.html')

def joblist(request):
    return render(request,'joblist.html')

def logout_(request):
    logout(request)
    return redirect("login")

def signup(request):
    return render(request,'signup.html')

def cres(request):
    return render(request,'cres.html')

def register(request):
    error=""
    if  request.method=="POST":
        email = request.POST['email']
        name = request.POST['user']
        # phn_no = request.POST['phn_no']
        password = request.POST['pwd']
        role = request.POST['role']
        
        try:
            user = CustomUser.objects.create_user(email=email, name=name, password=password, role=role)
            user.save()
            error="no"
        except:
            error="yes"
        # return redirect("login")
    
    return render(request, "register.html",{'error':error})



def profile(request):
    return render(request,'jobseeker/profile.html')

def resume(request):
    return render(request,'jobseeker/resume.html')

def apply(request):
    return render(request,'jobseeker/apply.html')


def employdash(request):
    return render(request,'employer/employdash.html')

def ats(request):
    job=Apply.objects.all()
    return render(request,'employer/ats.html',{'job':job})

def company(request):
    return render(request,'employer/company.html')

def jobpost(request):
    error=""
    if  request.method=="POST":
        jobtitle=request.POST.get("jobtitle")
        jobtype=request.POST.get("jobtype")
        joblocation=request.POST.get("joblocation")
        jobdescription=request.POST.get("jobdescription")
        jobvacancy=request.POST.get("jobvacancy")
        jobexp=request.POST.get("jobexperience")
        jobsalary=request.POST.get("jobsalary")
        jobskills=request.POST.get("jobskills")
        try:
            user = Job.objects.create(title=jobtitle, type=jobtype, Location=joblocation, description=jobdescription, vacancy=jobvacancy, experience=jobexp, salary=jobsalary, skills=jobskills)
            user.save()
            error="no"
        except:
            error="yes"
        # m={"error":error}
    return render(request,'employer/postjob.html',{'error':error}   )

def crt(request):
    return render(request,'employer/crt.html')

def jobl(request):
    job=Job.objects.all()
    return render(request,'employer/jobl.html',{'job':job})

def jobdash(request):
    main=Job.objects.all()   
    return render(request,'jobseeker/jobdash.html',{'main':main})


def apply(request):
    error=""
    if  request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        resume=request.POST.get("resume")
        jobtitle=request.POST.get("jobtitle")
        try:
            user = Apply.objects.create(name=name, email=email, phone=phone, resume=resume, jobtitle=jobtitle)
            user.save()
            error="no"
            # redirect("jobdash")
        except:
            error="yes"
        # m={"error":error}
    return render(request,'jobseeker/apply.html',{'error':error})