from src.study_planner import StudyPlanner
from src.notes import NoteManager
from src.task_manager import TaskManager
from src.text_processor import TextProcessor
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

#day 7 IMproving app

def notes_menu(note_manager):
    while True:
        print("\n------ NOTES ------")
        print("1. Add Note in it")
        print("2. View Notes of it ")
        print("3. Delete Note in it")
        print("4. Back")

        choice = input("Enter your choice: ")

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
            notes = note_manager.get_notes()

            if not notes:
                print("\nNo notes available.")
            else:
                print("\n------ YOUR NOTES ------")

                for note in notes:
                    print(f"\nID: {note['id']}")
                    print(f"Subject: {note['subject']}")
                    print(f"Topic: {note['topic']}")
                    print(f"Content: {note['content']}")

        elif choice == "3":
            try:
                note_id = int(input("Enter note ID: "))

                if note_manager.delete_note(note_id):
                    print("\nNote deleted successfully!")
                else:
                    print("\nNote not found.")

            except ValueError:
                print("\nPlease enter a valid number.")

        elif choice == "4":
            break

        else:
            print("\nInvalid choice!")


def task_menu(task_manager):
    while True:
        print("\n------ STUDY TASKS ------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            task_manager.add_task(task)

        elif choice == "2":
            task_manager.show_tasks()

        elif choice == "3":
            try:
                task_number = int(input("Enter task number: "))
                task_manager.complete_task(task_number)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def main():
    note_manager = NoteManager()
    task_manager = TaskManager()
    planner= StudyPlanner()
    processor=TextProcessor()

    while True:
        print("\n============================== ")
        print("        STUDYMATE AI")
        print("============================== ")
        print("1. Notes")
        print("2. Study Tasks")
        print("3. Study Planner")
        print("4. Text Processor")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            notes_menu(note_manager)

        elif choice == "2":
            task_menu(task_manager)

        elif choice == "3":
            subject = input("Enter subject: ")

            hours = get_positive_number(
                "How many hours can you study? "
            )

            print(planner.create_plan(subject, hours))

        elif choice == "4":
            text = input("Enter text to analyze: ")

            print("\n------ TEXT ANALYSIS ------")

            print(f"Word count: {processor.word_count(text)}")
            print(f"Character count: {processor.character_count(text)}")
            print(f"Common words: {processor.most_common_words(text)}")
        elif choice == "5":
            print("\nThank you for using StudyMate AI !")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
