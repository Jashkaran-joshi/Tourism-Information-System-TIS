from django.shortcuts import render
from .models import Destination, Testimonial, Slide

# Create your views here.

def index(request):
    destinations = Destination.objects.all()
    testimonials = Testimonial.objects.all()
    slides = Slide.objects.all()
    return render(request, 'index.html', {
        'destinations': destinations,
        'testimonials': testimonials,
        'slides': slides
    })
