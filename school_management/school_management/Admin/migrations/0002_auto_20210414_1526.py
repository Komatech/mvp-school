# Generated by Django 3.1.7 on 2021-04-14 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fees',
            old_name='amountDue',
            new_name='amount_due',
        ),
        migrations.RenameField(
            model_name='fees',
            old_name='amountPayed',
            new_name='amount_payed',
        ),
        migrations.RenameField(
            model_name='fees',
            old_name='className',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='attendanceScore',
            new_name='attendance_score',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='examScore',
            new_name='exam_score',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='testScore',
            new_name='test_score',
        ),
    ]