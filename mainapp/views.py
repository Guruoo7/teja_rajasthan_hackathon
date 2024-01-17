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

def user_details(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        ssi_id = request.POST.get('ssi_id')
        aadhar = request.POST.get('aadhar')
        phone = request.POST.get('phone')
        complaint_name = request.POST.get('complaintname')
        police_name = request.POST.get('policename')
        dateOfComplaint = request.POST.get('date')
        dateOfCrime = request.POST.get('dateofcrime')
        fir_no = request.POST.get('firnumber')
        status = request.POST.get('casestatus')
        district = request.POST.get('district')
        police_station_name = request.POST.get('stationname')
        comp_add = request.POST.get('complaintaddr')
        comp_desc = request.POST.get('complaintdesc')

        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["rajasthan_hackathon"]
        users_collection = db["users"]

        user_data = {
            "username" : username,
            "ssi_id" : ssi_id,
            "aadhar" : aadhar,
            "phone" : phone,
            "complaint_name" : complaint_name,
            "police_name" : police_name,
            "Complaint_Date" : dateOfComplaint,
            "Crime_Date" : dateOfCrime,
            "FIR_NO" : fir_no,
            "status" : status,
            "District" : district,
            "Police_Station_Name" : police_station_name,
            "complaint_address" : comp_add,
            "comp_desc" : comp_desc 
        }   
        
        users_collection.insert_one(user_data)
        print("j")
        return redirect('second.html')  
    else:
        return render(request, 'user_details.html')

def login(request):
    if request.method == 'POST':
        return redirect('user_details')
    else:
        return render(request, 'login.html')

def second(request):
    return render(request, 'second.html')

def register(request):

    if request.method == 'POST':
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # password = request.POST.get('password')

        # if not (username and email and password):
        #     print("abs")
        #     return render(request, 'register.html', {'error_message': 'Please fill in all fields.'})
        
        # client = pymongo.MongoClient("mongodb://localhost:27017/")
        # db = client["rajasthan_hackathon"]
        # users_collection = db["users"]

        # user_data = {
        #     'username': username,
        #     'email': email,
        #     'password': password
        # }

        # users_collection.insert_one(user_data)
        # print("j")
        return redirect('login') 
    else:
        print("g")
        return render(request, 'register.html')

def success(request):
    return render(request, "home.html")