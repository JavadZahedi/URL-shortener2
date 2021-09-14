# Generated by Django 3.2.7 on 2021-09-14 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.URLField()),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('visits', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_visit', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
