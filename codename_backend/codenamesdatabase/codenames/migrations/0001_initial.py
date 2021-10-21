# Generated by Django 3.1.8 on 2021-10-18 17:03

import codenames.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_key', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=12)),
                ('team', models.CharField(choices=[('R', 'Red'), ('B', 'Blue')], max_length=1)),
                ('task', models.CharField(choices=[('S', 'Spymaster'), ('O', 'Operator')], max_length=1)),
                ('connected_room_key', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='codenames.room')),
            ],
        ),
        migrations.CreateModel(
            name='RedWords',
            fields=[
                ('red_words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redWords', to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='RedTeam',
            fields=[
                ('red_team_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('red_team_score', models.IntegerField(default=0)),
                ('connected_room_key', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='codenames.room')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redTeamInfo', to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('operative_screen_name', models.CharField(max_length=12)),
                ('team', models.CharField(choices=[('R', 'Red'), ('B', 'Blue')], max_length=1)),
                ('role', models.CharField(choices=[('S', 'Spymaster'), ('O', 'Operative')], max_length=1)),
                ('room', models.CharField(max_length=5)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='codenames.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info_id', to='codenames.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='GuessedWords',
            fields=[
                ('guessed_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='GameWords',
            fields=[
                ('word_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('guessed', models.BooleanField(default=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('category', models.CharField(max_length=2, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameWords', to='codenames.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='connected_room_key',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='codenames.room'),
        ),
        migrations.CreateModel(
            name='DoubleAgentWords',
            fields=[
                ('doubleagent_words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doubleAgentWords', to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='BystanderWords',
            fields=[
                ('bystander_words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bystanderWords', to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='BlueWords',
            fields=[
                ('blue_words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blueWords', to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='BlueTeam',
            fields=[
                ('blue_team_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('blue_team_score', models.IntegerField(default=0)),
                ('connected_room_key', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='codenames.room')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blue_team_info', to='codenames.game')),
            ],
        ),
        migrations.CreateModel(
            name='AssassinWords',
            fields=[
                ('assassin_words_id', models.CharField(blank=True, default=codenames.models.words_number_default_function, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64, verbose_name=64)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assassinWords', to='codenames.game')),
            ],
        ),
    ]
