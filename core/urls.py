from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', homePage, name='home'),
    path('about/', aboutPage, name='about'),
    path('research/', researchPage, name='research'),
    path('contact/', contactPage, name='contact'),
    path('vision/', visionPage, name='vision'),
    path('news/', newstPage, name='news'),
]