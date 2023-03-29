# Generated by Django 4.0.10 on 2023-03-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTP_Notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='active',
            field=models.BooleanField(default=True, help_text="this is the user's active status for the otp verification", verbose_name='Active'),
        ),
    ]
