class TitleLengthError(Exception):
    """Класс исключения при создания заголовка заметки, реагирует на длину заголовка более 30 символов"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"

    def __repr__(self):
        return f"{self.message}"
