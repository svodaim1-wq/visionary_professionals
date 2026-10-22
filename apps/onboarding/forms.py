from django import forms
from .models import Carrier, PODSubmission

class CarrierOnboardingForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = [
            "full_legal_name", "company_name", "ein",
            "mc_number", "dot_number", "phone", "email",
            "fleet_type", "cargo_insurance", "authority_active",
            "rate_lock_accepted", "rate_lock_months",
            "w9_document", "coi_document", "authority_document", "banking_details",
        ]
        labels = {
            "full_legal_name": "Full Legal Name",
            "company_name": "Company Name (LLC / DBA)",
            "ein": "EIN / Tax ID",
            "mc_number": "MC Number",
            "dot_number": "DOT Number",
            "phone": "Phone Number",
            "email": "Email Address",
            "fleet_type": "Equipment Type",
            "cargo_insurance": "Cargo Insurance Coverage (e.g. $100,000)",
            "authority_active": "I have active MC authority",
            "rate_lock_accepted": "I accept the 12-month rate lock agreement",
            "rate_lock_months": "Rate Lock Period (months)",
            "w9_document": "Signed W-9 (Upload)",
            "coi_document": "Certificate of Insurance - COI (Upload)",
            "authority_document": "MC Authority Letter (Upload)",
            "banking_details": "Voided Check / Direct Deposit Form (Upload)",
        }
        widgets = {
            "authority_active": forms.CheckboxInput(),
            "rate_lock_accepted": forms.CheckboxInput(),
            "w9_document": forms.ClearableFileInput(),
            "coi_document": forms.ClearableFileInput(),
            "authority_document": forms.ClearableFileInput(),
            "banking_details": forms.ClearableFileInput(),
        }

class PODSubmissionForm(forms.ModelForm):
    class Meta:
        model = PODSubmission
        fields = ["load_reference", "pod_document"]
        widgets = {
            "pod_document": forms.ClearableFileInput(),
        }
