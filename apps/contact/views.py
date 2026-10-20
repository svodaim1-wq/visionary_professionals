from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, DispatchSpecialistForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. We'll be in touch soon.")
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})

def dispatch_specialist(request):
    if request.method == "POST":
        form = DispatchSpecialistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! A dispatch specialist will contact you shortly.")
            return redirect("home")
    else:
        form = DispatchSpecialistForm()
    return render(request, "pages/pricing.html", {"specialist_form": form})
