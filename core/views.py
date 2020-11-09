from django.shortcuts import render
from .models import *

# Create your views here.

def homePage(request):
    greet = Greeting.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    links = Social_Media_Link.objects.all()
    my_dict = {
        'greet':greet,
        'projects':projects,
        'events':events,
        'links':links,
    }
    return render(request, 'index.html', context=my_dict)

def aboutPage(request):
    greet = Greeting.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    links = Social_Media_Link.objects.all()
    researchs = Research.objects.all()
    about = About.objects.all()
    my_dict = {
        'greet':greet,
        'projects':projects,
        'events':events,
        'links':links,
        'researches':researchs,
        'about':about,
    }
    return render(request, 'about.html', context=my_dict)

def researchPage(request):
    greet = Greeting.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    links = Social_Media_Link.objects.all()
    researchs = Research.objects.all()
    my_dict = {
        'greet':greet,
        'projects':projects,
        'events':events,
        'links':links,
        'researches':researchs,
    }
    return render(request, 'research.html', context=my_dict)

def visionPage(request):
    greet = Greeting.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    links = Social_Media_Link.objects.all()
    researchs = Research.objects.all()
    vision = Vision.objects.all()

    my_dict = {
        'greet':greet,
        'projects':projects,
        'events':events,
        'links':links,
        'researches':researchs,
        'vision':vision,
    }
    return render(request, 'vision.html' , context=my_dict)

def contactPage(request):
    greet = Greeting.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    links = Social_Media_Link.objects.all()
    researchs = Research.objects.all()
    vision = Vision.objects.all()
    news = News.objects.all()
    contact = Contact.objects.all()
    my_dict = {
        'greet':greet,
        'projects':projects,
        'events':events,
        'links':links,
        'researches':researchs,
        'vision':vision,
        'news':news,
        'contact': contact,
    }
    return render(request, 'contact.html', context=my_dict)

def newstPage(request):
    greet = Greeting.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    links = Social_Media_Link.objects.all()
    researchs = Research.objects.all()
    vision = Vision.objects.all()
    news = News.objects.all()

    my_dict = {
        'greet':greet,
        'projects':projects,
        'events':events,
        'links':links,
        'researches':researchs,
        'vision':vision,
        'news':news,
    }
    return render(request, 'news.html', context=my_dict)