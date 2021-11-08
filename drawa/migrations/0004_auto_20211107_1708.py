# Generated by Django 3.2.8 on 2021-11-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawa', '0003_auto_20211107_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='is_online',
        ),
        migrations.AddField(
            model_name='draw',
            name='can_delivery',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='draw',
            name='is_direct',
            field=models.BooleanField(default=True),
        ),
    ]