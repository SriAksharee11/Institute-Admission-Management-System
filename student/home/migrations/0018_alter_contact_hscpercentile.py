# Generated by Django 4.2.7 on 2023-11-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0017_contact_hscpercentile_contact_hscschoolname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="hscpercentile",
            field=models.IntegerField(default="", max_length=60),
        ),
    ]
