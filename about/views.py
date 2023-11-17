from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):

    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_request = CollaborateForm(data=request.POST)
        if collaborate_request.is_valid():
            collaborate_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )

    collaborate_request = CollaborateForm()

    return render (
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_request": collaborate_request,
        }
    )