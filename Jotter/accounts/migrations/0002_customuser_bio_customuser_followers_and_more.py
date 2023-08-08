# Generated by Django 4.2.4 on 2023-08-08 02:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profilePic',
            field=models.ImageField(blank=True, upload_to='profilePics'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='socialLinks',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='topics',
            field=models.ManyToManyField(blank=True, to='blog.topic'),
        ),
    ]
