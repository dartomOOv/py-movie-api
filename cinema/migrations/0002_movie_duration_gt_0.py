# Generated by Django 5.1.1 on 2024-09-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='movie',
            constraint=models.CheckConstraint(condition=models.Q(('duration__gt', 0)), name='duration_gt_0'),
        ),
    ]
