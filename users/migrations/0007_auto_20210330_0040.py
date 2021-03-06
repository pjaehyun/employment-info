# Generated by Django 3.1.7 on 2021-03-29 15:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210325_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='att_field',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.AttentionField'),
        ),
        migrations.AlterField(
            model_name='user',
            name='att_language',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.AttentionLanguage'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='_user_followings_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
