# Generated by Django 4.1 on 2022-09-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0006_rename_foot_length_sport_aerobic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='neck_size',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
