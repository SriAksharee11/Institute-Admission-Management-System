# Generated by Django 4.2.7 on 2023-11-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0023_rename_coursename_course_studentname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=15)),
            ],
        ),
    ]
