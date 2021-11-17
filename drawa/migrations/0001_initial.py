# Generated by Django 3.2.8 on 2021-11-17 02:08

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
                ('name', models.CharField(default=' ', max_length=50, null=True)),
                ('nation', models.TextField(blank=True, null=True)),
                ('instagram_url', models.TextField(blank=True, default='', null=True)),
                ('kakao_url', models.TextField(blank=True, default='', null=True)),
                ('nation_flag_url', models.TextField()),
                ('store_img_url', models.TextField(null=True)),
                ('select', models.ManyToManyField(blank=True, related_name='selected_stores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kor', models.TextField()),
                ('name_eng', models.TextField()),
                ('brand', models.TextField()),
                ('collection', models.TextField()),
                ('code', models.CharField(max_length=50)),
                ('relesed_date', models.DateField()),
                ('image_url', models.TextField()),
                ('price', models.IntegerField()),
                ('view_count', models.IntegerField(default=0)),
                ('wish', models.ManyToManyField(blank=True, null=True, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_delivery', models.BooleanField(default=True)),
                ('url', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('is_direct', models.BooleanField(default=True)),
                ('participate', models.ManyToManyField(blank=True, null=True, related_name='participated_draws', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawa.product')),
                ('reserve', models.ManyToManyField(blank=True, null=True, related_name='reserved_draws', to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drawa.store')),
            ],
        ),
    ]
