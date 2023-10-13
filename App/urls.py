from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from JobPortal import settings
from . import views

urlpatterns = [
    
   path('home/',views.home,name="home"),
   path('login/',views.login_request,name="login"),
   path('signup/',views.signup,name='signup'),
   path('cres/',views.cres,name="cres"),
   path('register/',views.register,name="register"),
   path('logout/', views.logout_, name="logout"),
   path('joblist/',views.joblist,name="joblist"),
   
   
   
   
   path('jobdash/',views.jobdash,name="jobdash"),
   path('profile/',views.profile,name="profile"),
   path('resume/',views.resume,name="resume"),
   path('apply/',views.apply,name="apply"),
   
   
    path('employdash/',views.employdash,name="employdash"),
    path('jobpost/',views.jobpost,name="jobpost"),
    path('company/',views.company,name="company"),
    path('ats/',views.ats,name="ats"),
    path('crt/',views.crt,name="crt"),
    path('jobl/',views.jobl,name="jobl"),
    
    # path('jobdetail/<int:id>',views.jobdetails,name="jobdetail"),
    path('apply/',views.apply,name="apply"),

]
