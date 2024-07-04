import json
from datetime import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at
        }

class NotesApp:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, "w") as f:
            json.dump([note.to_dict() for note in self.notes], f, indent=2)

    def create_note(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)
        self.save_notes()
        print(f"Заметка с ID {id} создана.")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created_at}")

    def read_note(self, id):
        for note in self.notes:
            if note.id == id:
                print(f"ID: {note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Текст: {note.body}")
                print(f"Дата создания: {note.created_at}")
                return
        print(f"Заметка с ID {id} не найдена.")

    def edit_note(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.body = body
                note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print(f"Заметка с ID {id} отредактирована.")
                return
        print(f"Заметка с ID {id} не найдена.")

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_notes()
        print(f"Заметка с ID {id} удалена.")

    def filter_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.created_at.startswith(date)]
        for note in filtered_notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created_at}")

def main():
    app = NotesApp()

    while True:
        print("\n1. Создать заметку")
        print("2. Список заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Фильтр по дате")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            app.create_note(title, body)
        elif choice == "2":
            app.list_notes()
        elif choice == "3":
            id = int(input("Введите ID заметки: "))
            app.read_note(id)
        elif choice == "4":
            id = int(input("Введите ID заметки: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новый текст заметки: ")
            app.edit_note(id, title, body)
        elif choice == "5":
            id = int(input("Введите ID заметки: "))
            app.delete_note(id)
        elif choice == "6":
            date = input("Введите дату в формате YYYY-MM-DD: ")
            app.filter_by_date(date)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()