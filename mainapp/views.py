from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
from pymongo import MongoClient
from django.shortcuts import render
from .models import User
import pymongo

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        return redirect('second.html')  
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        return redirect('home')
    else:
        return render(request, 'login.html')

def second(request):
    return render(request, 'second.html')

def register2(request):
    # print("Sss")
    if request.method == 'POST':

        print("ssss")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (username and email and password):
            print("abs")
            return render(request, 'register2.html', {'error_message': 'Please fill in all fields.'})

        # Save user data to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["rajasthan_hackathon"]  # Update with your database name
        users_collection = db["users"]

        user_data = {
            'username': username,
            'email': email,
            'password': password
        }

        users_collection.insert_one(user_data)
        print("jesus")
        return redirect('register')  # Redirect to login page after successful registration
    else:
        return render(request, 'register2.html')

def success(request):
    return render(request, "home.html")