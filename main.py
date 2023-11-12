from DictOfTheNotes import DictOfTheNotes
from FileUsageMethods import importNotes, loadNotes
from Note import Note
from TextError import TextError
from TitleLengthError import TitleLengthError
from TitleNameError import TitleNameError


# Метод принимает на вход длину длину словаря, определяет окончание сообщения зависящее
# от количества заметок загружженных из файла
def mess_quantity_notes(length: int) -> str:
    if length == 1:
        return 'заметка'
    elif 1 < length < 5:
        return 'заметки'
    else:
        return 'заметок'


# Метод запускает приложение 'Зметки' и загружает заметки из файла notes.json
def start_app() -> dict:
    print("Запущено приложение 'Заметки'.")
    load_notes = loadNotes()
    if load_notes is None:
        print("Список заметок пуст.")
    else:
        print_notes(load_notes, False)
        return load_notes


# Метод делает выгрузку словаря записок из файла и добавляет новую запись
def add_notes(dictionary: dict, notes_to_add: dict) -> dict:
    dictionary.update(notes_to_add)
    return dictionary


# Метод принимает на вход значение даты/времени для поиска и также индекс даты/времени
# возвращает найденные заметки.
def search_notes(value: str, index: int) -> dict:
    load_notes = loadNotes()
    temp_list = list(filter(lambda x: x.get("date").split()[index] == value, load_notes.values()))
    result = {}
    for i in temp_list:
        for item in load_notes.items():
            if i == item[1]:
                result[item[0]] = item[1]
    if len(result) == 0:
        print("Записей на эту дату нет!")
    else:
        print_notes(result)
    return result


# Метод принимает на вход словарь с заметками и необязательный аргумент True/False, выводит в консоль
# сообщение о количестве заметок и если нужно показывает список заметок
def print_notes(notes_dict: dict, show=True) -> None:
    print(f"Найдено {len(notes_dict)} {mess_quantity_notes(len(notes_dict))}:")
    if show:
        for item in notes_dict.items():
            print(f"{item[0]}: {item[1]}")

# Метод делает поисковой запрос по дате и возвращает заметку,
# если записей не одна делает уточнение по времени
def make_search_request() -> dict:
    while True:
        date = input("Для поиска введите дату заметки в формате дд-мм-гггг "
                     "или введите 0 для выхода из системы поиска: ")
        if date == '0':
            raise TextError()
        notes_found_by_date = search_notes(date, 0)
        if len(notes_found_by_date) == 1:
            return notes_found_by_date
        elif len(notes_found_by_date) == 0:
            continue
        else:
            while True:
                note_time = input("Среди них есть нужная?\nВведите время последнего изменения в формате чч:мм:сс "
                                  "или введите 0 для выхода из системы поиска: ")
                if note_time == '0':
                    raise TextError()
                notes_found_by_time = search_notes(note_time, 1)
                if len(notes_found_by_time) == 0:
                    print_notes(notes_found_by_date)
                    continue
                return notes_found_by_time


# Метод выводит в консоль меню программы
def menu() -> None:
    print("Добавить заметку введите - 1")
    print("Изменить заметку введите - 2")
    print("Удалить заметку введите - 3")
    print("Сделать выборку введите - 4")
    print("Для выхода из приложения введите - 0")


user_notes = start_app()
while True:
    menu()
    command = input("Введите номер команды: ")
    if command == '1':
        try:
            d = DictOfTheNotes()
            note = d.create_note()
            d.added_note(note.get_note_dict())
            importNotes(add_notes(user_notes, d.get_notes()))
        except TitleNameError:
            print("Заголовок не может быть пустой строкой!")
        except TitleLengthError:
            print("Слишком длинное название заголовка!")
        except TextError:
            print("Текст заметки не может быть пустым!")

    elif command == '2':
        try:
            note_for_change = make_search_request()
            while True:
                edit_command = input("Для изменения заголовка введите - 1\n"
                                     "Для изменения поля заметки введите - 2\n"
                                     "Для выхода введите - 0\n")
                if edit_command == '1':
                    print(notes.get('title'))
                    break
                elif edit_command == '0':
                    break
                else:
                    print("Неопознанная команда, попробуйте еще раз.")
        except TextError:
            print("Попробуйте еще раз")
    elif command == '0':
        break
    else:
        print("Неопознанная команда, попробуйте еще раз.")
# n = d.create_note()
# n1 = d.create_note()
# d.added_note(n.get_note_dict())
# d.added_note(n1.get_note_dict())
#
# print(d.get_notes())
# importNotes(d.get_notes())
# print(loadNotes())
#
# print(d.search_note("12-11-2023"))
# except TitleNameError:
#     print("Заголовок должен быть строкой!")
# except Exception:
#     print("Общая ошибка при создании заметки")
