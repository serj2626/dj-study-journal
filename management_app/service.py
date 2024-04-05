def get_path_for_avatar_student(instance, filename):
    return f'students/avatar/{instance.user.username}/{filename}'
