from src.notes import NoteManager


def display_notes(note_manager):
    notes = note_manager.get_notes()

    if not notes:
        print("\nNo notes available.")
        return

    print("\n========== YOUR NOTES ==========")

    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Subject: {note['subject']}")
        print(f"Topic: {note['topic']}")
        print(f"Content: {note['content']}")


def main():
    note_manager = NoteManager()

    while True:
        print("\n========== STUDYMATE AI ==========")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            subject = input("Enter subject: ")
            topic = input("Enter topic: ")
            content = input("Enter note content: ")

            note = note_manager.add_note(
                subject,
                topic,
                content
            )

            print(f"\nNote {note['id']} added successfully!")

        elif choice == "2":
            display_notes(note_manager)

        elif choice == "3":
            try:
                note_id = int(input("Enter note ID to delete: "))

                if note_manager.delete_note(note_id):
                    print("\nNote deleted successfully!")
                else:
                    print("\nNote not found.")

            except ValueError:
                print("\nPlease enter a valid number.")

        elif choice == "4":
            print("\nThank you for using StudyMate AI!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main() #main function 
