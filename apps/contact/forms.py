from django import forms
from .models import ContactMessage, DispatchInquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]

class DispatchSpecialistForm(forms.ModelForm):
    class Meta:
        model = DispatchInquiry
        fields = ["name", "email", "phone", "mc_number", "dot_number", "equipment_type", "num_trucks", "time_in_business", "message"]
