# Generated by Django 4.2.7 on 2023-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0028_alter_student_hscmark_alter_student_hscschool"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="studentname",
            field=models.CharField(default="", max_length=122),
        ),
    ]
