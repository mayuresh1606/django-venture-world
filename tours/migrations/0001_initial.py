# Generated by Django 3.2.5 on 2021-07-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Night',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('night', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('starts_from', models.IntegerField()),
                ('days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.day')),
                ('nights', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.night')),
                ('package_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.packagetype')),
            ],
        ),
    ]
