from FileUsageMethods import loadNotes


# Метод запускает приложение 'Зметки' и загружает заметки из файла notes.json
def start_app() -> dict:
    print("Запущено приложение 'Заметки'.")
    load_notes = loadNotes()
    if load_notes is None:
        print("Список заметок пуст.")
    else:
        print_notes(load_notes, False)
        return load_notes


# Метод принимает на вход длину длину словаря, определяет окончание сообщения зависящее
# от количества заметок загружженных из файла
def mess_quantity_notes(length: int) -> str:
    if length == 1:
        return 'заметка'
    elif 1 < length < 5:
        return 'заметки'
    else:
        return 'заметок'


# Метод принимает на вход словарь с заметками и необязательный аргумент True/False, выводит в консоль
# сообщение о количестве заметок и если нужно показывает список заметок
def print_notes(notes_dict: dict, show=True) -> None:
    print(f"Найдено {len(notes_dict)} {mess_quantity_notes(len(notes_dict))}:")
    if show:
        for item in notes_dict.items():
            print(f"{item[0]}: {item[1]}")


# Метод принимает на вход значение даты/времени для поиска и также индекс даты/времени
# возвращает найденные заметки.
def search_notes(value: str, index: int, mess: str) -> dict | None:
    load_notes = loadNotes()
    temp_list = list(filter(lambda x: x.get("date").split()[index] == value, load_notes.values()))
    result = {}
    for i in temp_list:
        for item in load_notes.items():
            if i == item[1]:
                result[item[0]] = item[1]
    if len(result) == 0:
        print(f"Записей на {mess} нет!")
    else:
        print_notes(result)
    return result


# Метод делает поисковой запрос по дате и возвращает заметку,
# если записей не одна делает уточнение по времени
def make_search_request() -> dict | None:
    while True:
        date = input("Для поиска введите дату заметки в формате дд-мм-гггг "
                     "или введите 0 для выхода из системы поиска: ")
        if date == '0':
            print("Вы вышли из подраздела меню")
            return None
        notes_found_by_date = search_notes(date, 0, 'эту дату')
        if len(notes_found_by_date) == 1:
            return notes_found_by_date
        elif len(notes_found_by_date) == 0:
            continue
        else:
            while True:
                note_time = input("Среди них есть нужная?\nВведите время последнего изменения в формате чч:мм:сс "
                                  "или введите 0 для выхода из системы поиска: ")
                if note_time == '0':
                    print("Вы вышли из подраздела меню")
                    return None
                notes_found_by_time = search_notes(note_time, 1, 'это время')
                if len(notes_found_by_time) == 0:
                    print_notes(notes_found_by_date)
                    continue
                return notes_found_by_time


# Метод делает выгрузку словаря записок из файла и добавляет новую запись
def add_notes(dictionary: dict, notes_to_add: dict) -> dict:
    if dictionary is None:
        return notes_to_add
    else:
        dictionary.update(notes_to_add)
        return dictionary


# Метод проверяет есть ли сохраненные заметки у пользователя
def verify_notes_dict() -> bool:
    load_notes = loadNotes()
    if load_notes is None:
        return True
    else:
        return False
