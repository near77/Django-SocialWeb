# Generated by Django 2.0.3 on 2018-06-18 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofilemodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileModel',
        ),
    ]
