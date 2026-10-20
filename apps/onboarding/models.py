from django.db import models

class Carrier(models.Model):
    full_legal_name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=20, default="")
    company_name = models.CharField(max_length=200, blank=True)
    cipc_registration = models.CharField(max_length=50, blank=True)
    mc_number = models.CharField(max_length=50, blank=True)
    dot_number = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    fleet_type = models.CharField(max_length=50, default="")
    git_insurance = models.CharField(max_length=50, blank=True)
    has_prdp = models.BooleanField(default=False)
    rate_lock_accepted = models.BooleanField(default=False)
    rate_lock_months = models.IntegerField(default=12)
    cipc_document = models.FileField(upload_to="documents/cipc/", blank=True, null=True)
    git_document = models.FileField(upload_to="documents/git/", blank=True, null=True)
    prdp_document = models.FileField(upload_to="documents/prdp/", blank=True, null=True)
    banking_details = models.FileField(upload_to="documents/banking/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_legal_name

class PODSubmission(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    load_reference = models.CharField(max_length=100)
    pod_document = models.FileField(upload_to="pods/")
    status = models.CharField(max_length=20, default="submitted")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"POD {self.load_reference} - {self.carrier.full_legal_name}"
