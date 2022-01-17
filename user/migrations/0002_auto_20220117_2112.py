# Generated by Django 3.2 on 2022-01-17 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='build_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '男性'), ('female', '女性'), ('xgender', '中間')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='self_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
