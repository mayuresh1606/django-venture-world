# Generated by Django 4.0.2 on 2022-02-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0027_currenttours_accommodation_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currenttours',
            name='accommodation_3',
            field=models.CharField(default=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='currenttours',
            name='accommodation_4',
            field=models.CharField(default=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='currenttours',
            name='accommodation_5',
            field=models.CharField(default=False, max_length=1024),
        ),
        migrations.AddField(
            model_name='currenttours',
            name='accommodation_6',
            field=models.CharField(default=False, max_length=1024),
        ),
    ]
