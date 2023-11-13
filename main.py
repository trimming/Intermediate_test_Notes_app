from FileUsageMethods import loadNotes
from ServiceMethods import start_app, print_notes
from TextError import TextError
from TitleLengthError import TitleLengthError
from TitleNameError import TitleNameError
from UserCommand import user_command_create_note, menu, user_command_changed_note
from UserOutException import UserOutException

start_app()
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
        try:
            user_command_changed_note()
        except UserOutException:
            print("Вы вышли из подраздела меню")
    elif command == '3':
        print()
    elif command == '5':
        print_notes(loadNotes())
    elif command == '0':
        break
    else:
        print("Неопознанная команда, попробуйте еще раз.")
