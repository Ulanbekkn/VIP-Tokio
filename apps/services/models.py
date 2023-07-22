from django.db import models


class BasicService(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основная услуга'
        verbose_name_plural = 'Основные услуги'


class AdditionalService(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class Massage(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массажи'


class Extreme(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экстрим'
        verbose_name_plural = 'Экстримы'


class SadoMazo(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Садо Мазо'
        verbose_name_plural = 'Садо Мазо'


class Striptease(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стриптиз'
        verbose_name_plural = 'Стриптизы'


class PackagePrice(models.Model):
    apartments_1h = models.PositiveIntegerField(blank=True)
    apartments_2h = models.PositiveIntegerField(blank=True)
    apartments_night = models.PositiveIntegerField(blank=True)
    departure_1h = models.PositiveIntegerField(blank=True)
    departure_2h = models.PositiveIntegerField(blank=True)
    departure_night = models.PositiveIntegerField(blank=True)
    # model = models.OneToOneField(Model, on_delete=models.CASCADE, related_name='price')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Пакет цен'
        verbose_name_plural = ' Пакеты цен'
