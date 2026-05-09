from django.shortcuts import render
from .models import Language_courses, FAQ,BannerVideo,Graduate,Destination,Courses,CEO,COO

# Create your views here.

def home(request):
    banner=BannerVideo.objects.first()
    graduates = Graduate.objects.all()
    context = {
        'banner': banner,
        'graduates': graduates
    }
    return render(request, 'home.html', context)


def about(request):
    coo = COO.objects.first()
    ceo = CEO.objects.first()
    context = {
        'coo': coo,
        'ceo': ceo
    }
    return render(request, 'about.html',context)


def Study_in_india(request):
    graduate = Graduate.objects.filter(studied_at='India')
    destination = Destination.objects.filter(country='India')
    context = {
        'graduates': graduate,
        'destinations': destination

    }
    return render(request, 'Study_in_india.html', context)


def Study_in_abroad(request):
    languages = Language_courses.objects.all()
    graduate = Graduate.objects.filter(studied_at='Abroad')
    destination = Destination.objects.filter(country='Abroad')
    courses = Courses.objects.filter(country='Abroad')
    
    context = {
        'languages': languages,
        'graduates': graduate,
        'destinations': destination,
        'courses': courses
    }
    return render(request, 'Study_in_abroad.html',context)


def faq(request):
    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'faq.html', context)


def contact(request):
    return render(request, 'contact.html')