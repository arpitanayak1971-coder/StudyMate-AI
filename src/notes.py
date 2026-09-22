class NoteManager:
    def __init__(self):
        self.notes = []
        self.next_id = 1

    def add_note(self, subject, topic, content):
        note = {
            "id": self.next_id,
            "subject": subject,
            "topic": topic,
            "content": content
        }

        self.notes.append(note)
        self.next_id += 1

        return note

    def get_notes(self):
        return self.notes

    def delete_note(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                return True

        return False