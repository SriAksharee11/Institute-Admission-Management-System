# Generated by Django 3.1.2 on 2021-03-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
        migrations.AddField(
            model_name='contact',
            name='Aadhar',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='contact',
            name='Address1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='Address2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='CollegeName',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='JeeAppNo',
            field=models.CharField(default='', max_length=12),
        ),
        #migrations.AddField(
         #   model_name='contact',
          #  name='JeePercentile',
         #   field=models.CharField(default='', max_length=12),
        #),
        #migrations.AddField(
            #model_name='contact',
            #name='JeeRank',
            #field=models.CharField(default='', max_length=12),
        #),
        #migrations.AddField(
            #model_name='contact',
            #name='MhtcetAppNo',
            #field=models.CharField(default='', max_length=12),
        #),
        #migrations.AddField(
           ## model_name='contact',
           # name='MhtcetPercentile',
            #field=models.CharField(default='', max_length=12),
        #),
        #migrations.AddField(
           # model_name='contact',
            #name='MhtcetRank',
            #field=models.CharField(default='', max_length=12),
        #),
        migrations.AddField(
            model_name='contact',
            name='Percentage',
            field=models.CharField(default='0.0', max_length=12),
        ),
        # migrations.AddField(
        #     model_name='contact',
        #     name='date',
        #     field=models.DateField(default=''),
        # ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='father',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='mother',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone1',
            field=models.CharField(default='', max_length=12),
        ),
    ]
