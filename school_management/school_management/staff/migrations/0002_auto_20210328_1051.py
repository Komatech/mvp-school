# Generated by Django 3.1.7 on 2021-03-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffprofile',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='staffprofile',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
