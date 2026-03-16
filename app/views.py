from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def Study_in_india(request):
    return render(request, 'Study_in_india.html')

def Study_in_abroad(request):
    return render(request, 'Study_in_abroad.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')