# Generated by Django 4.1 on 2022-09-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0010_medians'),
    ]

    operations = [
        migrations.AddField(
            model_name='medians',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
