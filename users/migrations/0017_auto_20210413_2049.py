# Generated by Django 3.1.7 on 2021-04-13 11:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_user_followings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followings',
        ),
        migrations.AddField(
            model_name='user',
            name='bvbv',
            field=models.ManyToManyField(blank=True, related_name='_user_bvbv_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
