import numpy as np
from src.study_planner import StudyPlanner
from src.notes import NoteManager
from src.analytics import NoteAnalytics
from src.visualizer import StudyVisualizer
from src.task_manager import TaskManager
from src.text_processor import TextProcessor

#day 15
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
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Note Statistics")
        print("5. Delete Note")
        print("6. Back")
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
            stats = note_manager.get_statistics()

            print("\n------ NOTE STATISTICS ------")
            print(f"Total notes: {stats['total_notes']}")

            print("\nNotes by subject:")

            if stats["subjects"]:
                for subject, count in stats["subjects"].items():
                    print(f"- {subject}: {count}")
            else:
                print("No subjects available.")

            print("\nNotes by topic:")

            if stats["topics"]:
                for topic, count in stats["topics"].items():
                    print(f"- {topic}: {count}")
            else:
                print("No topics available.")
        elif choice == "5":
            try:
                note_id = int(input("Enter note ID: "))

                if note_manager.delete_note(note_id):
                    print("\nNote deleted successfully!")
                else:
                    print("\nNote not found.")

            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == "6":
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
    planner = StudyPlanner()
    analytics = NoteAnalytics(note_manager.get_notes())
    processor=TextProcessor()
    visualizer = StudyVisualizer()

    while True:
        print("\n============================== ")
        print("        STUDYMATE AI")
        print("============================== ")
        print("1. Notes")
        print("2. Study Tasks")
        print("3. Study Planner")
        print("4. Text Analyzer")
        print("5. Note Analytics")
        print("6. Note visualization")
        print("7.Exit")

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

            meaningful_words = processor.remove_stop_words(text)

            print(f"Meaningful words: {len(meaningful_words)}")
            print(f"Common meaningful words: {processor.most_common_words(text)}")
            print(f"Keywords: {processor.extract_keywords(text)}")
            print(f"Estimated reading time: {processor.estimate_reading_time(text)} minutes")
        elif choice == "5":
            print("\n------ NOTE ANALYTICS ------")

            analytics = NoteAnalytics(note_manager.get_notes())

            print(f"Total notes: {analytics.total_notes()}")
            print(f"Notes by subject: {analytics.notes_by_subject()}")
            print(f"Notes by topic: {analytics.notes_by_topic()}")
        elif choice == "6":
            print("\n------ NOTE VISUALIZATION ------")
            print("1. Notes by Subject")
            print("2. Notes by Topic")
            print("3. Back")

            visualization_choice = input("Enter your choice: ")

            analytics = NoteAnalytics(note_manager.get_notes())

            if visualization_choice == "1":
                subject_data = analytics.notes_by_subject()
                visualizer.plot_notes_by_subject(subject_data)

            elif visualization_choice == "2":
                topic_data = analytics.notes_by_topic()
                visualizer.plot_notes_by_topic(topic_data)

            elif visualization_choice == "3":
                pass

            else:
                print("Invalid choice.")
        elif choice=="7":
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
