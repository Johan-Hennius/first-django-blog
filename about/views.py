from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_request = CollaborateForm()

    return render (
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_request": collaborate_request,
        }
    )