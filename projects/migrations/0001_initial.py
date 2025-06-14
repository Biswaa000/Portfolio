# Generated by Django 5.2.1 on 2025-06-02 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the project', max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('slug', models.SlugField(blank=True, help_text='URL-friendly version of the title (auto-generated)', max_length=100, unique=True)),
                ('short_description', models.CharField(help_text='Brief description (max 200 chars)', max_length=200)),
                ('description', models.TextField(help_text='Detailed description of the project')),
                ('github_url', models.URLField(blank=True, help_text='URL to GitHub repository', null=True)),
                ('live_url', models.URLField(blank=True, help_text='URL to live demo', null=True)),
                ('is_featured', models.BooleanField(default=False, help_text='Feature this project prominently')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='Higher numbers appear first')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-display_order', '-created_at'],
            },
        ),
    ]
