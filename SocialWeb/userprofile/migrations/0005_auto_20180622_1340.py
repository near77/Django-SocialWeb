# Generated by Django 2.0.4 on 2018-06-22 05:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20180620_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, null=True, related_name='profile_follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, null=True, related_name='profile_follower', to=settings.AUTH_USER_MODEL),
        ),
    ]