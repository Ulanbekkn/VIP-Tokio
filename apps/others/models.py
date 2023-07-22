from django.db import models


class Support(models.Model):  # Техподдержка
    name = models.CharField('Имя', max_length=20, unique=True)
    mail = models.EmailField('Почта', max_length=50, unique=True)
    subject = models.CharField('Тема', max_length=20)
    message = models.TextField('Сообщение')

    def __str__(self):
        return f'User: {self.name} Subject: {self.subject}'

    class Meta:
        verbose_name = 'Техподдержка'
        verbose_name_plural = 'Техподдержка'


class MiniBlog(models.Model):  # Мини блог
    title = models.CharField('Название', max_length=30)
    image = models.ImageField('Фотография', blank=True, null=True)
    description = models.TextField('Текст')
    # user = models.ForeignKey('User', verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мини блог'
        verbose_name_plural = 'Мини блог'


class AboutUs(models.Model):  # О нас
    text = models.TextField('Текст')

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'



