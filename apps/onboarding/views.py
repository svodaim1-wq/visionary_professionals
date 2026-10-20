from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CarrierOnboardingForm, PODSubmissionForm
from .models import Carrier

def carrier_onboarding(request):
    if request.method == "POST":
        form = CarrierOnboardingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Application submitted. A dispatch specialist will contact you within 24 hours.")
            return redirect("home")
    else:
        form = CarrierOnboardingForm()
    return render(request, "onboarding/carrier_form.html", {"form": form})

def pod_submission(request):
    if request.method == "POST":
        form = PODSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "POD submitted successfully. Status: Submitted.")
            return redirect("pod_submission")
    else:
        form = PODSubmissionForm()
    return render(request, "onboarding/pod_submission.html", {"form": form})
