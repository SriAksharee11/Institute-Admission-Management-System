from django.contrib import admin
from django.urls import path,include
from home import views
from .views import Contact

urlpatterns = [
    path('',views.index, name="home"),
    #dummy1
    path("contact",views.contact, name='contact'),
    path('register', views.registerPage, name='register'),
    path('blog', views.blog, name='blog'),
    
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('course',views.course,name="course"),
    path('course.html',views.course,name="course"),
    path('next.html',views.course,name="course"),

    path('student',views.student,name="student"),
    path('chat.html',views.student,name="student"),
   
]





