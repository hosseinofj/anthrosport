# Generated by Django 4.1 on 2022-09-30 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0011_medians_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='back_size',
            new_name='neck',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='neck_size',
            new_name='waist',
        ),
    ]
