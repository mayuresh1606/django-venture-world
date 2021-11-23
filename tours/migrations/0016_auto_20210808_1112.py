# Generated by Django 3.2.5 on 2021-08-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0015_auto_20210806_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_1',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_1_cost_ac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_1_cost_non_ac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_1_days',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_1_nights',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_2',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_2_cost_ac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_2_cost_non_ac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_2_days',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_2_nights',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_3',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_3_cost_ac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_3_cost_non_ac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_3_days',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='educationaltour',
            name='transportation_3_nights',
            field=models.IntegerField(default=1),
        ),
    ]