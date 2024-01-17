from django.urls import path
from .views import home, about, contact, register, login, second, register2

urlpatterns = [
    path('', home, name="home"),
    path('about.html', about, name="about"),
    path('contact.html', contact, name="contact"),
    path('register.html', register, name="register"),
    path('register/', register, name="register"),
    path('login.html', login, name='login'),
    path('second.html', second, name='second'),
    path('second/', second, name='second'),
    path('register2.html', register2, name="register2"),
    path('register2/', register2, name='register2'),  # Use register2 as a namespace
    path('register2/login/', login, name='register2_login'),  # Add a login URL under register2 namespace
]