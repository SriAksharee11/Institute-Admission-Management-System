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
    #hscschoolname = models.CharField(max_length=100, null=True)
    #JeeAppNo=models.CharField(max_length=109)
    #hscpercentile = models.IntegerField(max_length=60, default="" ,null=False)
    Address1 = models.TextField( default="")
    Address2 = models.TextField( default="")
    SchoolName = models.CharField(max_length=122, default="")
    #Percentage = models.CharField(max_length=12, default="")
    file = models.FileField( default="")
    file1 = models.FileField( default="")
    Aadhar = models.CharField(max_length=12, default="")
    desc = models.TextField( default="")
    # date = models.DateField(default=datetime.today())
    #image=models.ImageField(upload_to="images/", null=True, verbose_name="", default="")
    sslc = models.CharField(max_length=100, null=True, blank=True)
    


    def __str__(self):
        return self.name
    


class Course(models.Model):  
    studentname = models.CharField(max_length=122,null=True)
    email=models.EmailField(max_length=254)
    hscpercentage = models.CharField(max_length=10)
    #group=models.CharField(max_length=10)
    #course = models.CharField(max_length=100,null=True)
    #pgcourse=models.CharField(max_length=10)
    #category=models.CharField(max_length=100)
    #ugmark=models.CharField(max_length=3)
    category = models.CharField(max_length=2, choices=[('ug', 'UG'), ('pg', 'PG')])
    selected_course = models.CharField(max_length=255)


    def __str__(self):
        return self.studentname
    
class Student(models.Model):  
    Username = models.CharField(max_length=15,default="")
    email=models.EmailField(max_length=50)
    hscschool=models.CharField(max_length=100,default="")
    hscmark=models.FloatField(max_length=3,default="")
    
    def __str__(self):
        return self.Username 

  
    
#class RankList(models.Model):
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #rank = models.IntegerField()
       
    #def __str__(self):
        #return self.student 

     


class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()     
    hscpercentile = models.IntegerField(max_length=5)

