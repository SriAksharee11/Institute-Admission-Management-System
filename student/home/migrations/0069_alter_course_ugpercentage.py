# Generated by Django 4.2.8 on 2023-12-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0068_alter_course_ugpercentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="ugpercentage",
            field=models.FloatField(default="", max_length=3),
        ),
    ]
