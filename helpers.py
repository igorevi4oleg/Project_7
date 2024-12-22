import uuid

def generate_random_string(length=10):
    """Генерация случайной строки."""
    return str(uuid.uuid4())[:length]