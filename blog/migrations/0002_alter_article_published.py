# Generated by Django 5.1.1 on 2024-10-07 16:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
