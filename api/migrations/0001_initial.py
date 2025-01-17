# Generated by Django 5.0.7 on 2024-07-13 04:41

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('youtube_video_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('caption', models.JSONField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
