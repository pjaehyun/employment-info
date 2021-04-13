# Generated by Django 3.1.7 on 2021-04-13 11:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210413_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bvbv',
        ),
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='_user_followings_+', to=settings.AUTH_USER_MODEL),
        ),
    ]