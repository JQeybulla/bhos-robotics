# Generated by Django 3.1.3 on 2020-11-09 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201109_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greeting',
            name='about_department',
        ),
    ]