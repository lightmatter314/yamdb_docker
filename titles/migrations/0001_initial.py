# Generated by Django 3.0.5 on 2021-05-01 16:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг категории')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название жанра')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг жанра')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название произведения')),
                ('year', models.PositiveIntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(2021)], verbose_name='Год произведения')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='Рейтинг произведения')),
                ('description', models.TextField(verbose_name='Описание произведения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='titles.Category')),
                ('genre', models.ManyToManyField(related_name='genres', to='titles.Genre')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]