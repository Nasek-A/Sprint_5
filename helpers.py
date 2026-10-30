import random
import string

def generate_email():
    """Генерирует email для регистрации."""
    number = random.randint(10000, 99999)
    return f"student_qa_{number}@yandex.ru"


def generate_password(length=8):
    """Генерирует пароль заданной длины."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))