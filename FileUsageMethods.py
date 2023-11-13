import json
import os
from pathlib import Path


def importNotes(note):
    with open("notes.json", "w", encoding="utf-8") as fh:
        try:
            fh.write(json.dumps(note, ensure_ascii=False))
            print("Записи успешно сохранены.")
        except :
            print("Ошибка записи!")


def loadNotes():
    file = Path("notes.json")
    file.touch(exist_ok=True)
    if os.stat("notes.json").st_size == 0:
        return None
    with open("notes.json", "r", encoding="utf-8") as fh:
        try:
            notes = json.load(fh)
            print("Записи успешно загружены.")
        except:
            print("Ошибка")
        return notes
