# Generated by Django 3.2.7 on 2021-10-17 15:22

import codenames.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameWords',
            fields=[
                ('words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
