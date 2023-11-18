from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('contact_us/', contact_us, name='contact_us'),
    path('credits/', credits, name='credits'),
]
