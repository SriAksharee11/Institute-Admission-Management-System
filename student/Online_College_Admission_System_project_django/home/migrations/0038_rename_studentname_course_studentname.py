# Generated by Django 4.2.7 on 2023-11-29 15:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0037_rename_studentname_course_studentname"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="Studentname",
            new_name="studentname",
        ),
    ]
