from datetime import datetime

from DictOfTheNotes import DictOfTheNotes
from FileUsageMethods import importNotes, loadNotes
from ServiceMethods import add_notes, make_search_request
from TextError import TextError
from TitleLengthError import TitleLengthError
from TitleNameError import TitleNameError
from UserOutException import UserOutException


# Метод выводит в консоль меню программы
def menu() -> None:
    print("Создать заметку введите - 1")
    print("Изменить заметку введите - 2")
    print("Удалить заметку введите - 3")
    print("Сделать выборку введите - 4")
    print("Показать все заметки - 5")
    print("Для выхода из приложения введите - 0")


# Метод выполняет команду пользователя по созданию заметки
def user_command_create_note() -> None:
    try:
        d = DictOfTheNotes()
        note = d.create_note()
        d.added_note(note.get_note_dict())
        importNotes(add_notes(loadNotes(), d.get_notes()))

    except TitleNameError:
        raise TitleNameError
    except TitleLengthError:
        raise TitleLengthError
    except TextError:
        raise TextError


def user_command_changed_note():
    try:
        note_for_change = make_search_request()
        while True:
            edit_command = input("Для изменения заголовка введите - 1\n"
                                 "Для изменения поля заметки введите - 2\n"
                                 "Для выхода введите - 0\n")
            if edit_command == '1':
                try:
                    value_for_change = input("Введите новый заголовок:\n")
                    if value_for_change.replace(' ', '') == '':
                        raise TitleNameError("Заголовок не может быть пустой строкой!")
                    if len(value_for_change) > 50:
                        raise TitleLengthError("Слишком длинное название заголовка!")
                    for i in note_for_change:
                        for j in note_for_change[i]:
                            note_for_change[i]['title'] = value_for_change
                            note_for_change[i]['date'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    importNotes(add_notes(loadNotes(), note_for_change))
                    print(note_for_change)
                    break
                except TitleNameError:
                    print("Заголовок не может быть пустой строкой! Попробуйте еще раз.")
                except TitleLengthError:
                    print("Слишком длинное название заголовка! Попробуйте еще раз.")

            elif edit_command == '2':
                try:
                    value_for_change = input("Введите новый текст заметки:\n")
                    if value_for_change.replace(' ', '') == '':
                        raise TextError("Текст заметки не может быть пустым!")
                    for i in note_for_change:
                        for j in note_for_change[i]:
                            note_for_change[i]['text'] = value_for_change
                            note_for_change[i]['date'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    importNotes(add_notes(loadNotes(), note_for_change))
                    print(note_for_change)
                    break
                except TextError:
                    print("Текст заметки не может быть пустым! Попробуйте еще раз.")

            elif edit_command == '0':
                break
            else:
                print("Неопознанная команда, попробуйте еще раз.")
    except:
        raise UserOutException
