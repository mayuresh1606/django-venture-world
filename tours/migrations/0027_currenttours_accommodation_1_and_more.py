# Generated by Django 4.0.2 on 2022-02-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0026_currenttours_tour_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='currenttours',
            name='accommodation_1',
            field=models.CharField(default=False, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currenttours',
            name='accommodation_2',
            field=models.CharField(default=False, max_length=1024),
            preserve_default=False,
        ),
    ]