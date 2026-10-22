from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("onboarding", "0004_carrier_rate_lock_accepted_carrier_rate_lock_months_and_more"),
    ]

    operations = [
        migrations.RenameField(model_name="carrier", old_name="id_number", new_name="ein"),
        migrations.RenameField(model_name="carrier", old_name="git_insurance", new_name="cargo_insurance"),
        migrations.RenameField(model_name="carrier", old_name="has_prdp", new_name="authority_active"),
        migrations.RenameField(model_name="carrier", old_name="cipc_document", new_name="w9_document"),
        migrations.RenameField(model_name="carrier", old_name="git_document", new_name="coi_document"),
        migrations.RenameField(model_name="carrier", old_name="prdp_document", new_name="authority_document"),
        migrations.RemoveField(model_name="carrier", name="cipc_registration"),
    ]
