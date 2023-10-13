from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from Users.models import CustomUser

# Create your models here.
# class Company(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
#     name=models.CharField(max_length=200,null=True)
#     position=models.CharField(max_length=200,null=True)
#     description=models.CharField(max_length=2000,null=True)
#     salary=models.IntegerField(null=True)
#     experience=models.IntegerField(null=True)
#     Location=models.CharField(max_length=2000,null=True)

#     def __str__(self):
#         return self.name


# class Candidates(models.Model):
#     category=(
#         ('Male','male'),
#         ('Female','female'),
#         ('Other','other'),
#     )

#     name=models.CharField(max_length=200,null=True)
#     dob=models.DateField(null=True)
#     gender= models.CharField(max_length=200,null=True,choices=category)
#     mobile= models.CharField(max_length=200,null=True)
#     email= models.CharField(max_length=200,null=True)
#     resume=models.FileField(null=True)
#     company=models.ManyToManyField(Company,blank=True)

#     def __str__(self):
#         return self.name



class Job(models.Model):
    # rec=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    type=models.CharField(null=True,max_length=200)
    title=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    Location=models.CharField(max_length=2000,null=True)
    vacancy=models.IntegerField(null=True)
    skills=models.CharField(max_length=2000,null=True)
    
    def __str__(self):
        return self.title
    
# class Apply(models.Model):
#     # ... other fields ...
#     is_applied = models.BooleanField(default=False)

class Apply(models.Model):
    # rec=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    resume=models.FileField(null=True)
    jobtitle=models.CharField(max_length=200,null=True)
    
    # job=models.ForeignKey(Job,on_delete=models.CASCADE,null=True)
    # jobseeker=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    # phone=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.email
    