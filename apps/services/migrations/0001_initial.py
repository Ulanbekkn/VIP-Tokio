# Generated by Django 4.2 on 2023-06-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Дополнительная услуга',
                'verbose_name_plural': 'Дополнительные услуги',
            },
        ),
        migrations.CreateModel(
            name='BasicService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Основная услуга',
                'verbose_name_plural': 'Основные услуги',
            },
        ),
        migrations.CreateModel(
            name='Extreme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Экстрим',
                'verbose_name_plural': 'Экстримы',
            },
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Массаж',
                'verbose_name_plural': 'Массажи',
            },
        ),
        migrations.CreateModel(
            name='PackagePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartments_1h', models.PositiveIntegerField(blank=True)),
                ('apartments_2h', models.PositiveIntegerField(blank=True)),
                ('apartments_night', models.PositiveIntegerField(blank=True)),
                ('departure_1h', models.PositiveIntegerField(blank=True)),
                ('departure_2h', models.PositiveIntegerField(blank=True)),
                ('departure_night', models.PositiveIntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Пакет цен',
                'verbose_name_plural': ' Пакеты цен',
            },
        ),
        migrations.CreateModel(
            name='SadoMazo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Садо Мазо',
                'verbose_name_plural': 'Садо Мазо',
            },
        ),
        migrations.CreateModel(
            name='Striptease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Стриптиз',
                'verbose_name_plural': 'Стриптизы',
            },
        ),
    ]
