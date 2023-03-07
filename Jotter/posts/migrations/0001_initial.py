# Generated by Django 4.0.6 on 2023-03-05 07:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('followers', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('tags', models.CharField(max_length=50)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.topic')),
            ],
        ),
    ]