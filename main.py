
from ServiceMethods import start_app, verify_notes_dict
from TextError import TextError
from TitleLengthError import TitleLengthError
from TitleNameError import TitleNameError
from UserCommand import user_command_create_note, menu, user_command_changed_note, user_command_show_notes, \
    user_command_delete_note, user_command_select_notes
from UserOutException import UserOutException

try:
    start_app()
except FileNotFoundError:
    print("Проблема чтения файла")

while True:
    menu()
    command = input("Введите номер команды: ")
    if command == '1':
        try:
            user_command_create_note()
        except TitleNameError:
            print("Заголовок не может быть пустой строкой!")
        except TitleLengthError:
            print("Слишком длинное название заголовка!")
        except TextError:
            print("Текст заметки не может быть пустым!")

    elif command == '2':
        if verify_notes_dict():
            print("У вас нет ни одной заметки. Попробуйте сначала создать заметку!")
        else:
            try:
                user_command_changed_note()
            except UserOutException:
                print("Не удалось выполнить операцию, попробуйте еще раз.")
    elif command == '3':
        if verify_notes_dict():
            print("У вас нет ни одной заметки. Попробуйте сначала создать заметку!")
        else:
            try:
                user_command_delete_note()
            except:
                print("Не удалось выполнить операцию, попробуйте еще раз.")
    elif command == '4':
        if verify_notes_dict():
            print("У вас нет ни одной заметки. Попробуйте сначала создать заметку!")
        else:
            try:
                user_command_select_notes()
            except:
                print("Не удалось выполнить операцию, попробуйте еще раз.")
    elif command == '5':
        if verify_notes_dict():
            print("У вас нет ни одной заметки. Попробуйте сначала создать заметку!")
        else:
            try:
                user_command_show_notes()
            except:
                print("Проблема чтения файла")
    elif command == '0':
        break
    else:
        print("Неопознанная команда, попробуйте еще раз.")
