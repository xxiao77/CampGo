# Generated by Django 3.0.2 on 2020-02-11 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_auto_20200207_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campsite',
            name='users',
        ),
        migrations.AddField(
            model_name='campsite',
            name='favlist',
            field=models.ManyToManyField(related_name='favoritor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campsite',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
