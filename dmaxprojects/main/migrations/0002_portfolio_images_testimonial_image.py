# Generated by Django 4.1.4 on 2023-01-01 14:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(null=True, upload_to='portfolios/'), null=True, size=None),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(null=True, upload_to='testimonials/'),
        ),
    ]
