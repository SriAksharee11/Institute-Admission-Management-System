# Generated by Django 4.2.7 on 2023-11-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0024_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
