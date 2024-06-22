# Generated by Django 4.2.8 on 2023-12-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0057_alter_course_studentname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="SchoolName",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="sslc",
        ),
        migrations.AddField(
            model_name="student",
            name="sslc",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="sslcmark",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
