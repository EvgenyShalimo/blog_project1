from django.db import models

class Users(models.Model):
    name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('фамилия', max_length=50)
    email = models.EmailField('Ваш e-mail адрекс', max_length=50)
    city = models.CharField('Город', max_length=50)
    pol = models.CharField('Пол', max_length=50)
    date = models.DateTimeField('Дата регистрации')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


