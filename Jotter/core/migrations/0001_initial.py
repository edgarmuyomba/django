# Generated by Django 4.0.6 on 2023-03-04 12:27

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
                ('followers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('text', models.CharField(max_length=155)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
        ),
    ]
