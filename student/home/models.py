from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models 
# Create your models here.
#imagefile=image
#Image=Contact
#

#dummy
#class Post(models.Model):
#  title = models.TextField()
#    cover = models.ImageField(upload_to='images/')

#   def __str__(self):
#        return self.title

#dummy1
# class Contact(models.Model):
    # name = models.CharField(max_length=122, default="")
    # image=models.ImageField(upload_to="images/", null=True, verbose_name="", default="")
#    
# 
    # def __str__(self):
        # return self.name
#dummy1

class Contact(models.Model):
    name = models.CharField(max_length=122, default="")
    father = models.CharField(max_length=122, default="")
    mother = models.CharField(max_length=122, default="")
    email = models.CharField(max_length=122, default="")
    phone = models.CharField(max_length=12,default="")
    phone1 = models.CharField(max_length=12, default="")
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=9, choices=GENDER_CHOICES)
    RELIGION_CHOICES = [
        ('christianity', 'Christianity'),
        ('islam', 'Islam'),
        ('hinduism', 'Hinduism'),
        ('buddhism', 'Buddhism'),
        ('other', 'Other'),
    ]

    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
    #hscschoolname = models.CharField(max_length=100, null=True)
    #JeeAppNo=models.CharField(max_length=109)
    #hscpercentile = models.IntegerField(max_length=60, default="" ,null=False)
    Address1 = models.TextField( default="")
    Address2 = models.TextField( default="")
    #SchoolName = models.CharField(max_length=122, default="")
    #Percentage = models.CharField(max_length=12, default="")
    file = models.FileField( default="")
    file1 = models.FileField( default="")
    Aadhar = models.CharField(max_length=12, default="")
    desc = models.TextField( default="")
    # date = models.DateField(default=datetime.today())
    #image=models.ImageField(upload_to="images/", null=True, verbose_name="", default="")
    #sslc = models.CharField(max_length=100, null=True, blank=True)
    


    def __str__(self):
        return self.name
    


class Course(models.Model):  
    studentname = models.CharField(max_length=122,null=False)
    hscpercentage = models.CharField(max_length=10)
    ugpercentage=models.FloatField(max_length=3,null=True)
    #group=models.CharField(max_length=10)
    course = models.CharField(max_length=100)



    def __str__(self):
        return self.studentname
    
class Student(models.Model):  
    Username = models.CharField(max_length=15,default="")
    email=models.EmailField(max_length=50)
    sslc=models.CharField(max_length=100)
    sslcmark=models.FloatField()
    hscschool=models.CharField(max_length=100,default="")
    hscmark=models.IntegerField(max_length=3,default="")
    marksheet=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.Username 

  
    
class RankList(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rank = models.IntegerField()
       
    def __str__(self):
        return self.Username 

     


class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()     
    hscpercentile = models.IntegerField(max_length=5)

