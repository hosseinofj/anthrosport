# Generated by Django 4.1 on 2022-10-27 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0017_medians_max_medians_min_medians_stage_1_max_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medians',
            old_name='value',
            new_name='Average_value',
        ),
    ]
