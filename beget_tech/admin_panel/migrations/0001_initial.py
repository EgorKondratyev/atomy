# Generated by Django 4.1.5 on 2023-01-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_sentence', models.CharField(max_length=255, verbose_name='Тип предложения')),
                ('sentence', models.TextField(verbose_name='Предложение')),
                ('language', models.BooleanField(verbose_name='Язык предложения')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото предложения')),
            ],
            options={
                'db_table': 'sentences',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True, verbose_name='ID пользователя телеграм')),
                ('language', models.BooleanField(verbose_name='Язык пользователя')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО')),
                ('sex', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пол')),
                ('birth_date', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дата рождения')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мобильный телефон')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Почтовый индекс')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Электронная почта')),
                ('purpose_registration', models.TextField(blank=True, null=True, verbose_name='Цель регистрации')),
                ('register_status', models.BooleanField(default=False, null=True, verbose_name='Статус регистрации')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]