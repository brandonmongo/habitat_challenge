# Generated by Django 3.2.7 on 2021-09-17 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tender_results',
            old_name='Accepted',
            new_name='Accepted_Or_Rejected',
        ),
        migrations.RenameField(
            model_name='tender_results',
            old_name='Agent',
            new_name='Agent_Or_Applicant',
        ),
        migrations.RenameField(
            model_name='tender_results',
            old_name='RTM',
            new_name='RTM_Or_no_RTM',
        ),
    ]
