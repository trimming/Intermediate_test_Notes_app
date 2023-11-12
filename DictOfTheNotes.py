from Note import Note


class DictOfTheNotes:
    def __init__(self):
        self.__notes = dict()

    def update_dict(self, dictionary):
        self.__notes.update(dictionary)

    def added_note(self, note):
        self.__notes[id(note)] = note

    def get_notes(self):
        return self.__notes

    @staticmethod
    def create_note():
        title = input("Введите заголовок заметки: \n")
        text = input("Введите текст записи: \n")
        return Note(title, text)
