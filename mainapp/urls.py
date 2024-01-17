from django.urls import path
from .views import home, about, contact, user_details, login, second, register

urlpatterns = [
    path('', home, name="home"),
    path('about.html', about, name="about"),
    path('contact.html', contact, name="contact"),
    path('user_details.html', user_details, name="user_details"),
    path('user_details/', user_details, name="user_details"),
    path('user_details/second/', second, name="second"),
    path('login.html', login, name='login'),
    path('second.html', second, name='second'),
    path('second/', second, name='second'),
    path('register.html', register, name="register"),
    path('register/', register, name='register'),  # Use register2 as a namespace
    path('register/login/', login, name='register_login'),  # Add a login URL under register2 namespace
]