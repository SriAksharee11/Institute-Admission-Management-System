# Generated by Django 4.2.7 on 2023-11-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0035_alter_course_studentname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="Username",
            field=models.CharField(max_length=15),
        ),
    ]
