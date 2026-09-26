import json
import os


class NoteManager:
    def __init__(self):
        self.file_path = "data/notes.json"
        self.notes = []
        self.next_id = 1

        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.notes = json.load(file)

            if self.notes:
                self.next_id = max(note["id"] for note in self.notes) + 1

    def save_notes(self):
        with open(self.file_path, "w") as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, subject, topic, content):
        note = {
            "id": self.next_id,
            "subject": subject,
            "topic": topic,
            "content": content
        }

        self.notes.append(note)
        self.next_id += 1

        self.save_notes()

        return note

    def get_notes(self):
        return self.notes

    def delete_note(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True

        return False