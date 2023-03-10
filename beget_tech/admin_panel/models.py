from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(verbose_name='ID пользователя телеграм', unique=True)
    username = models.CharField(max_length=255, verbose_name='Ссылка на аккаунт пользователя')
    language = models.BooleanField(verbose_name='Язык пользователя')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='Страна')
    full_name = models.CharField(max_length=255, blank=True, null=True,  verbose_name='ФИО')
    sex = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Пол')
    birth_date = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Мобильный телефон')
    postal_code = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Почтовый индекс')
    address = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Адрес')
    email = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Электронная почта')
    purpose_registration = models.TextField(blank=True, null=True,  verbose_name='Цель регистрации')
    register_status = models.BooleanField(default=False, null=True,  verbose_name='Статус регистрации')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'users'
        verbose_name = 'зарегистрированного пользователя'
        verbose_name_plural = 'Зарегистрированные пользователи'


class Sentences(models.Model):
    type_sentence = models.CharField(max_length=255, verbose_name='Тип предложения')
    sentence = models.TextField(verbose_name='Предложение')
    language = models.BooleanField(verbose_name='Язык предложения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото предложения', null=True, blank=True)
    video_id = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.type_sentence

    class Meta:
        db_table = 'sentences'
        verbose_name = 'Предложения и кнопки'
        verbose_name_plural = 'Предложения и кнопки'
