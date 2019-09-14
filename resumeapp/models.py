from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    first_name=models.CharField(max_length=100 , null=False ,verbose_name="First Name" , help_text="Enter Your First Name")
    last_name=models.CharField(max_length=100 , null=False,verbose_name="Last Name" , help_text="Enter Your Last Name")
    address=models.CharField(max_length=200 , null=False , help_text="Enter Your Address")
    contact_number=models.CharField(max_length=100 , null=False ,verbose_name="Contact Number" , help_text="Enter Your Mobile Number")
    email=models.EmailField(null=False)
    description=models.TextField(null=False)
    facebook=models.CharField(max_length=100 , null=False)
    twitter=models.CharField(max_length=100 , null=False)
    linkedin=models.CharField(max_length=100 , null=False)
    pinterest=models.CharField(max_length=100 , null=False  )
    image=models.ImageField(null=False , help_text="Please Upload 500x500 px Image")

    def __str__(self):
        return "About Me"

    class Meta:
        verbose_name = "About Me"


class Experience(models.Model):
    company_name=models.CharField(max_length=200, null=False)
    position=models.CharField(max_length=100, null=False)
    description=models.TextField(null=False)
    join = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.company_name    

class Education(models.Model):
    school_name=models.CharField(max_length=200, null=False)
    degree=models.CharField(max_length=100 )
    department=models.CharField(max_length=100 )
    gpa=models.CharField(max_length=100 )
    join = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.school_name   

class Skill(models.Model):
    skill=models.CharField(max_length=100, null=False)


    def __str__(self):
        return self.skill   

class Interest(models.Model):
    interest=models.TextField( null=False)


    def __str__(self):
        return self.interest   

class Award(models.Model):
    awards=models.CharField(max_length=100, null=False)


    def __str__(self):
        return self.awards   