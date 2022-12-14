# Generated by Django 4.1 on 2022-10-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportpredictor', '0016_alter_medians_count_alter_medians_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='medians',
            name='max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_1_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_1_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_2_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_2_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_3_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_3_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_4_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_4_min',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_5_max',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='medians',
            name='stage_5_min',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='medians',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]
