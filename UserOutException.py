class UserOutException(Exception):
    """Класс исключения при выходе пользователя из раздела меню"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"

    def __repr__(self):
        return f"{self.message}"
