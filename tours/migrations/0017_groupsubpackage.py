# Generated by Django 3.2.5 on 2021-08-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0016_auto_20210808_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSubPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_sub_package', models.CharField(default=False, max_length=255)),
            ],
        ),
    ]
