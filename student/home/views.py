from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from datetime import datetime
from home.models import Contact,Course,Student

from django.contrib import messages
from django.core.mail import send_mail
from userlogin import settings


#dummy
#from django.views.generic import ListView
from home.models import Contact,Course
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import  Destination


#from django.views.generic import ListView, CreateView # new
#from django.urls import reverse_lazy # new

# from home.forms import ImageForm # new

#dummy


#password for test user is 1234$sahil
# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method=="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
                
        context = {'form':form}
        return render(request, 'register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            # check if user has entered correct credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request,user)
                return redirect("/")

            else:  
                # No backend authenticated the credentials
                messages.info(request, 'Username OR password is incorrect')
                return render(request,'login.html')
            

        return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

#dummy1
#def send_email(request):
   # if request.method == 'POST':
   ###     form = Contact(request.POST)
    #    if form.is_valid():
    #        email = form.cleaned_data['masowndar45@gmail.com']
     #       subject = form.cleaned_data['hello']
      #      message = form.cleaned_data['haaii hello']
       #     
        #    email = 'sowndarmoorthy@gmail.com'  # Replace with your email address
         #   recipient_list = [email]
#
 #           send_mail(subject, message, email, recipient_list, fail_silently=False)
#
 #           return HttpResponse('Email sent successfully.')
  #  else:
   #     form = Contact()

    #return render(request, 'email.html', {'form': form})
#def contact(request):
#    if request.method=="POST":
#        name=request.POST.get('name')
#        image=request.POST.get('image')
#        contact=Contact(name=name,image=image)
#        contact.save()
#        messages.success(request, 'Your message has been sent!')
#    return render(request,"contact.html")

#def contact(request):
#    lastimage=Contact.objects.last()
#    image=lastimage.image

#    form=ImageForm(request.POST or None, request.FILES or None)
#    if form.is_valid():
#        form.save()

#    context={'image':image, 'form':form}

#    return render(request, 'contact.html', context)

# def contact(request):
    # if request.method =='POST':
        # form=ImageForm(request.POST, request.FILES)
        # if form.is_valid():
            # form.save()
            # img_obj=form.instance
            # return render(request, 'contact.html', {'form':form, 'img_obj':img_obj})
    # else:
        # form= ImageForm()
    # return render(request, 'contact.html', {'form':form})

def blog(request):

    dests = Destination.objects.all()

    return render(request,"blog.html", {'dests' : dests})

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        
        email = request.POST.get('email')

        phone = request.POST.get('phone')
        phone1 = request.POST.get('phone1')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')        
        #sslc= request.POST.get('sslc')   # ... other fields ...

        #hscschoolname = request.POST.get('hscschoolname')
        #hscpercentile = request.POST.get('hscpercentile')
        Address1 = request.POST.get('Address1')
        Address2 = request.POST.get('Address2')
       # SchoolName = request.POST.get('SchoolName')
        #Percentage = request.POST.get('Percentage')
        file = request.POST.get('file')
        #JeeAppNo=request.POST.get('jeeappno')
        #file1 = request.FILES["file1"]
        Aadhar = request.POST.get('Aadhar')
        desc = request.POST.get('desc') 
        document = Contact.objects.create(name=name,father=father,mother=mother,email=email, phone=phone, phone1=phone1,Address1=Address1, Address2=Address2,file=file,Aadhar=Aadhar, desc=desc,gender=gender,religion=religion)#JeeAppNo=JeeAppNo)
        document.save()
        messages.success(request, 'Your message has been sent!,Go To apply')
    return render(request, "contact.html")

def student(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        email=request.POST.get('email')
        sslc=request.POST.get('sslc')
        sslcmark=request.POST.get('sslcmark')
        hscschool=request.POST.get('hscschool')
        hscmark=request.POST.get('hscmark')
        marksheet=request.POST.get('marksheet')
        rank = Student.objects.order_by('-hscmark')

        if int(hscmark)>500:
            print('your mark eligible for admission')
            #sub='Kongu enginieering college'
            #msg='your application was successfully sumbited wait for the result'
            send_mail(
                    'Kongu Enginieering college',
                     f"dear {Username} ,your {hscmark}. is eligible for this admission",
                     settings.EMAIL_HOST_USER,
                     [email],
                     fail_silently=False,
                
                    
            ),
            #messages.success1(request,'Mail sent Successfully')
        
        document=Student.objects.create(Username=Username,email=email,hscschool=hscschool,hscmark=hscmark,sslc=sslc,sslcmark=sslcmark,marksheet=marksheet)
        document.save()
        #messages.success(request, 'Your message has been sent!, Next Step Register Course')

    return render(request,"chat.html")   



def course(request):
    if request.method == "POST":
        studentname = request.POST.get('studentname')
        hscpercentage = request.POST.get('hscpercentage')
        email=request.POST.get('email')
        ugpercentage=request.POST.get('ugpercemtage')
        
        #group=request.POST.get('group')
        course= request.POST.get('course')
        if int(hscpercentage)>90:
            print('')
            #sub='Kongu enginieering college'
            #msg='your application was successfully sumbited wait for the result'
            send_mail(
                    'Kongu Enginieering college',
                     f"Dear {studentname},\n\nYou have successfully selected the course: {course}.\n\nHSC Percentage: {hscpercentage}%\n\nThank you for your selection!",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                
                    
            ),
        document=Course.objects.create(studentname=studentname,hscpercentage=hscpercentage,course=course,ugpercentage=ugpercentage)
        document.save()


    return render(request,"course.html")    


#dummy1

#dummy
#class HomePageView(ListView):
#    model = Post
#    template_name = 'index.html'


#class HomePageView(ListView):
#    model = Post
#    template_name = 'index.html'

#class CreatePostView(CreateView): # new
#    model = Post
#    form_class = PostForm
#    template_name = 'post.html'
#    success_url = reverse_lazy('index')
#dummy


    # Other fields in your model...