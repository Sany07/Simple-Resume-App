# Generated by Django 2.2.5 on 2019-09-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0003_auto_20190913_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='end',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='join',
        ),
        migrations.AddField(
            model_name='experience',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='join',
            field=models.DateField(blank=True, null=True),
        ),
    ]
