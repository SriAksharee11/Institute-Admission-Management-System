# Generated by Django 4.2.7 on 2023-11-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_contact_sslc"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="hscpercentile",
            field=models.IntegerField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="hscshoolName",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
