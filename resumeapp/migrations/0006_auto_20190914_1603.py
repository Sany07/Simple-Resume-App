# Generated by Django 2.2.5 on 2019-09-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0005_auto_20190914_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteconfiguration',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='last_name',
            field=models.CharField(default=' Md Ahasan Habib ', max_length=100),
            preserve_default=False,
        ),
    ]
