# Generated by Django 4.2.8 on 2023-12-12 03:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0060_remove_course_course_remove_course_pgcourse_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="ugmark",
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
