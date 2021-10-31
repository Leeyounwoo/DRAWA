# Generated by Django 3.2.8 on 2021-10-31 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_online', models.BooleanField()),
                ('nation', models.TextField(blank=True, null=True)),
                ('location_si', models.TextField(blank=True, null=True)),
                ('location_gu', models.TextField(blank=True, null=True)),
                ('location_dong', models.TextField(blank=True, null=True)),
                ('location_detail', models.TextField(blank=True, null=True)),
                ('homepage_url', models.TextField()),
                ('community_url', models.TextField()),
                ('tel', models.TextField(blank=True, null=True)),
                ('selected_store', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('brand', models.TextField()),
                ('collection', models.TextField()),
                ('relesed_date', models.DateField()),
                ('image_url', models.TextField()),
                ('price', models.IntegerField()),
                ('description_url', models.TextField()),
                ('wishlist', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawa.product')),
                ('reservation', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawa.store')),
            ],
        ),
    ]
