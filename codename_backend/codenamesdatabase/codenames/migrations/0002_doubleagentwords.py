# Generated by Django 3.1.8 on 2021-10-18 02:21

import codenames.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubleAgentWords',
            fields=[
                ('doubleagent_words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubleagentWords', to='codenames.game')),
            ],
        ),
    ]
