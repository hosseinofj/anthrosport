# Generated by Django 4.1 on 2022-10-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0014_remove_target_finger_ratio_2_4_target_finger_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medians',
            name='count',
            field=models.FloatField(default=0),
        ),
    ]
