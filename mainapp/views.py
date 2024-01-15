from django.shortcuts import render, redirect

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
        return redirect('main')
    else:
        return render(request, 'register.html')

def second(request):
    return render(request, 'second.html')
