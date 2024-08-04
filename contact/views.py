from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactUs

# Create your views here.

def contact(request):
    if request.method == "POST":
        contact_form = ContactUs(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                """Message received!
                We will respond to you within 3 working days.""")

    contact_form = ContactUs()

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form},
    )
