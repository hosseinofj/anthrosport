# Generated by Django 4.1 on 2022-09-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0008_remove_target_dateofbirth_target_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='e_mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]