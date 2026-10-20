from django import forms
from .models import Carrier, PODSubmission

class CarrierOnboardingForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = [
            "full_legal_name", "id_number", "company_name", "cipc_registration",
            "mc_number", "dot_number", "phone", "email",
            "fleet_type", "git_insurance", "has_prdp",
            "rate_lock_accepted", "rate_lock_months",
            "cipc_document", "git_document", "prdp_document", "banking_details",
        ]
        widgets = {
            "has_prdp": forms.CheckboxInput(),
            "rate_lock_accepted": forms.CheckboxInput(),
            "cipc_document": forms.ClearableFileInput(),
            "git_document": forms.ClearableFileInput(),
            "prdp_document": forms.ClearableFileInput(),
            "banking_details": forms.ClearableFileInput(),
        }

class PODSubmissionForm(forms.ModelForm):
    class Meta:
        model = PODSubmission
        fields = ["load_reference", "pod_document"]
        widgets = {
            "pod_document": forms.ClearableFileInput(),
        }
