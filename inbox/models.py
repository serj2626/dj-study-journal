from django.db import models
from management_app.models import CustomUser


def get_path_for_file_message(instance, filename):
    return f"message/{instance.chat.id}/{filename}"


class Chat(models.Model):
    '''
    Модель чата
    '''
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                               verbose_name="Отправитель", related_name='sender')
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='receiver', verbose_name="Получатель")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"

    def __str__(self):
        return f"Чат между {self.sender} - {self.receiver}"


class Message(models.Model):
    '''
    Модель сообщения
    '''
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, verbose_name="Чат")
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                               verbose_name="Отправитель", related_name='m_sender')
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='m_receiver', verbose_name="Получатель")
    text = models.TextField(verbose_name="Текст")
    file = models.FileField(upload_to=get_path_for_file_message, max_length=100,
                            verbose_name="Файл", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение от {self.sender} - {self.receiver}"
