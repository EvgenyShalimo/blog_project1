from django.dispatch import receiver
from BlogApp.blog.models import Users
from django.db.models.signals import post_save


@receiver(post_save,sender=Users)
def post_save_user(**kwargs):
    if created:
        print('Пользователь создан')
