from datetime import datetime

from TextError import TextError
from TitleLengthError import TitleLengthError
from TitleNameError import TitleNameError


class Note:

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @classmethod
    def verify_title(cls, title):
        if title.replace(' ', '') == '':
            raise TitleNameError("Заголовок не может быть пустой строкой!")
        if len(title) > 50:
            raise TitleLengthError("Слишком длинное название заголовка!")

    @classmethod
    def verify_text(cls, text):
        if text.replace(' ', '') == '':
            raise TextError("Текст заметки не может быть пустым!")

    @property
    def title(self):
        return self.__title

    @property
    def text(self):
        return self.__text

    @property
    def date(self):
        return self.__date

    @text.setter
    def text(self, text):
        self.verify_title(text)
        self.__text = text

    @title.setter
    def title(self, title):
        self.verify_title(title)
        self.__title = title

    @date.setter
    def date(self, date):
        self.__date = date

    @text.deleter
    def text(self):
        del self.__text

    @title.deleter
    def title(self):
        del self.__title

    def __repr__(self):
        return f"'title': {self.__title}, 'text': {self.__text}, 'date': {self.__date}"


    def get_note_dict(self):
        return {'title': self.__title, 'text': self.__text, 'date': self.__date}
