from django.urls import path
from.import views

urlpatterns = [
     path('', views.home, name="home"),
     path('about.html', views.about, name="about"),
     path('contact.html', views.contact, name="contact"),
     path('register.html', views.register, name="register"),
     path('login.html', views.login, name='login'),
     path('second.html', views.second, name='second'),
     path('second/', views.second, name='second'),
     path('register2/', views.register2, name='register2.html')
]