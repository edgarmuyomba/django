# Generated by Django 4.2.4 on 2023-08-15 06:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdded', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('text', models.TextField()),
            ],
            options={
                'ordering': ['-dateAdded'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('tags', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-dateAdded',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]
