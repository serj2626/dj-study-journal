import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from management_app.service import get_path_for_avatar_student


class CustomUser(AbstractUser):
    '''
    Модель пользователя
    '''
    user_type_data = ((1, "Админ"), (2, "Преподаватель"), (3, "Студент"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10)


class Student(models.Model):
    '''
    Модель студента
    '''

    GENDER = ((1, "Мужчина"), (2, "Женщина"), (3, "Не указано"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True)
    gender = models.CharField(
        max_length=255, verbose_name="Пол", choices=GENDER, default=3)
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to=get_path_for_avatar_student, default="media/students/avatar_student.jpg")
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(
        max_length=255, verbose_name="Телефон", blank=True, null=True)
    course = models.ForeignKey(
        'Course', on_delete=models.DO_NOTHING, verbose_name="Курс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f'Студент {self.user.username}'


class AdminHOD(models.Model):
    '''
    Модель администратора
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    phone = models.CharField(
        max_length=255, verbose_name="Телефон", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Администратор {self.user.username}'

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Teacher(models.Model):
    '''
    Модель преподавателя
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    phone = models.CharField(
        max_length=255, verbose_name="Телефон", blank=True, null=True)
    address = models.TextField(verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Персонал {self.user.username}'

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"


class Course(models.Model):
    '''
    Модель курса
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_name = models.CharField(
        max_length=255, verbose_name="Название курса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Курс {self.course_name}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Subject(models.Model):
    '''
    Модель предмета
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_name = models.CharField(
        max_length=255, verbose_name="Название предмета")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=1, verbose_name="Курс")
    teacher = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Преподаватель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Предмет {self.subject_name}'

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Attendance(models.Model):
    '''
    Модель посещаемости
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.ForeignKey(
        Subject, on_delete=models.DO_NOTHING, verbose_name="Предмет")
    attendance_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата посещения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Посещаемость {self.attendance_date}'

    class Meta:
        verbose_name = "Посещаемость"
        verbose_name_plural = "Посещаемость"


class AttendanceReport(models.Model):
    '''
    Модель отчета посещаемости
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        Student, on_delete=models.DO_NOTHING, verbose_name="Студент")
    attendance = models.ForeignKey(
        Attendance, on_delete=models.CASCADE, verbose_name="Посещаемость")
    status = models.BooleanField(default=False, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Отчет посещаемости {self.attendance.attendance_date}'

    class Meta:
        verbose_name = "Отчет посещаемости"
        verbose_name_plural = "Отчеты посещаемости"


class LeaveReportStudent(models.Model):
    '''
    Модель отчета о выходе студента
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент")
    leave_date = models.CharField(max_length=255, verbose_name="Дата выхода")
    leave_message = models.TextField(verbose_name="Сообщение")
    leave_status = models.BooleanField(default=False, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Отчет о выходе {self.student.user.username}'

    class Meta:
        verbose_name = "Отчет о выходе"
        verbose_name_plural = "Отчеты о выходе"


class LeaveReportTeacher(models.Model):
    '''
    Модель отчета о выходе преподавателя
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    leave_date = models.CharField(max_length=255, verbose_name="Дата выхода")
    leave_message = models.TextField(verbose_name="Сообщение")
    leave_status = models.BooleanField(default=False, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Отчет о выходе {self.teacher.user.username}'

    class Meta:
        verbose_name = "Отчет о выходе преподавателя"
        verbose_name_plural = "Отчеты о выходе преподавателя"


class FeedBackStudent(models.Model):
    '''
    Модель обратной связи студента
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент")
    theme = models.CharField(
        max_length=255, verbose_name="Тема", blank=True, null=True)
    feedback = models.TextField(verbose_name="Отзыв")
    feedback_reply = models.TextField(
        verbose_name="Ответ", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Обратная связь студента {self.student.user.username}'

    class Meta:
        verbose_name = "Обратная связь студента"
        verbose_name_plural = "Обратная связь студента"


class FeedBackTeacher(models.Model):
    '''
    Модель обратной связи преподавателя
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    theme = models.CharField(
        max_length=255, verbose_name="Тема", blank=True, null=True)
    feedback = models.TextField(verbose_name="Отзыв")
    feedback_reply = models.TextField(
        verbose_name="Ответ", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Обратная связь преподавателя {self.teacher.user.username}'

    class Meta:
        verbose_name = "Обратная связь преподавателя"
        verbose_name_plural = "Обратная связь преподавателя"


class NotificationStudent(models.Model):
    '''
    Модель уведомления студента
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Студент")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Уведомление студента {self.student.user.username}'

    class Meta:
        verbose_name = "Уведомление студента"
        verbose_name_plural = "Уведомления студента"


class NotificationTeacher(models.Model):
    '''
    Модель уведомления сотрудника
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher_id = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Сотрудник")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'Уведомление сотрудника {self.teacher.user.username}'

    class Meta:
        verbose_name = "Уведомление сотрудника"
        verbose_name_plural = "Уведомления сотрудника"



class SessionYearModel(models.Model):
    '''Модель сессии студентов'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_start_year = models.DateField(verbose_name="Начало сессии")
    session_end_year = models.DateField(verbose_name="Конец сессии")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", blank=True, null=True)

    def __str__(self):
        return f'Сессия для группы {self.course.course_name} {self.session_start_year} - {self.session_end_year}'

    class Meta:
        verbose_name = "Сессия"
        verbose_name_plural = "Сессии"


class RaitingStar(models.Model):
    '''Модель рейтинга'''
    raiting = models.IntegerField(verbose_name="Рейтинг")

    def __str__(self):
        return f'{self.raiting}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class RaitingTeacher(models.Model):
    '''Модель рейтинга преподавателя'''

    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель", related_name="teacher")
    raiting = models.ForeignKey(
        RaitingStar, on_delete=models.CASCADE, verbose_name="Рейтинг")
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return f'{self.teacher.user.username} - {self.raiting.raiting}'

    class Meta:
        verbose_name = "Рейтинг преподавателя"
        verbose_name_plural = "Рейтинги преподавателя"



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(user=instance)
        if instance.user_type == 2:
            Teacher.objects.create(user=instance, address="")
        if instance.user_type == 3:
            Student.objects.create(user=instance, course_id=Course.objects.get(
                id=1), session_start_year="2024-01-01", session_end_year="2024-01-01", address="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.AdminHOD.save()
    if instance.user_type == 2:
        instance.Teacher.save()
    if instance.user_type == 3:
        instance.Student.save()