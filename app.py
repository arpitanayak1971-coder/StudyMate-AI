from src.improvement_tracker import ImprovementTracker
from src.improvement_history import ImprovementHistory
from src.improvement_comparison import ImprovementComparison

from src.monthly_performance_rating import MonthlyPerformanceRating
from src.study_planner import StudyPlanner
from src.notes import NoteManager
from src.analytics import NoteAnalytics
from src.visualizer import StudyVisualizer
from src.task_manager import TaskManager
from src.text_processor import TextProcessor
from src.progress import StudyProgress
from src.session_tracker import StudySessionTracker
from src.study_goals import StudyGoalTracker
from src.data_preprocessor import StudyDataPreprocessor
from src.weekly_analytics import WeeklyStudyAnalytics
from src.monthly_report import MonthlyStudyReport
from src.monthly_analytics import MonthlyStudyAnalytics
from src.monthly_goal_report import MonthlyGoalReport
from src.monthly_goals import MonthlyGoalTracker
from src.monthly_goal_insights import MonthlyGoalInsights

#day 30
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



def study_sessions_menu(session_tracker, visualizer):
    while True:
        print("\n------ STUDY SESSIONS ------")
        print("1. Record Study Session")
        print("2. View Study Sessions")
        print("3. Study Time Analytics")
        print("4. Visualize Study Time")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            subject = input("Enter subject: ").strip()
            topic = input("Enter topic: ").strip()

            try:
                duration = get_positive_number(
                    "Enter study duration in minutes: "
                )

                session = session_tracker.add_session(
                    subject, topic, duration
                )

                print(
                    f"Session {session['id']} saved successfully!"
                )

            except ValueError as error:
                print(f"Could not save session: {error}")

        elif choice == "2":
            sessions = session_tracker.get_sessions()

            if not sessions:
                print("No study sessions recorded yet.")
            else:
                for session in sessions:
                    print(
                        f"ID: {session['id']} | "
                        f"Subject: {session['subject']} | "
                        f"Topic: {session['topic']} | "
                        f"Duration: {session['duration_minutes']} minutes | "
                        f"Date: {session['date']}"
                    )

        elif choice == "3":
            total = session_tracker.total_study_minutes()
            print(f"Total study time: {total:g} minutes")
            print("Study time by subject:")

            subject_totals = session_tracker.study_time_by_subject()

            if not subject_totals:
                print("No study data available.")
            else:
                for subject, minutes in subject_totals.items():
                    print(f"- {subject}: {minutes:g} minutes")

        elif choice == "4":
            subject_totals = session_tracker.study_time_by_subject()
            visualizer.plot_study_time_by_subject(subject_totals)


        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")



def study_goals_menu(goal_tracker):
    while True:
        print("\n------ STUDY GOALS ------")
        print("1. Set Daily Study Goal")
        print("2. View Today's Progress")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                minutes = get_positive_number(
                    "Enter daily study goal in minutes: "
                )
                goal_tracker.set_daily_goal(minutes)
                print(f"Daily goal set to {minutes:g} minutes.")
            except ValueError as error:
                print(f"Could not set goal: {error}")

        elif choice == "2":
            progress = goal_tracker.get_goal_progress()
            print(f"Daily goal: {progress['goal_minutes']:g} minutes")
            print(f"Studied today: {progress['studied_minutes']:g} minutes")
            print(f"Remaining: {progress['remaining_minutes']:g} minutes")
            print(
                f"Completion: "
                f"{progress['completion_percentage']:.2f}%"
            )

            if progress["goal_achieved"]:
                print("Congratulations! Daily goal achieved.")
            else:
                print("Keep going—you can still reach your goal.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")



def weekly_analytics_menu():
    import json
    from pathlib import Path

    print("\n------ WEEKLY STUDY ANALYTICS ------")

    session_path = Path("data/sessions.json")
    if session_path.exists():
        with session_path.open("r", encoding="utf-8") as file:
            sessions = json.load(file)
    else:
        sessions = []

    clean_data = StudyDataPreprocessor().preprocess_sessions(sessions)
    analytics = WeeklyStudyAnalytics(clean_data)
    daily_totals = analytics.daily_study_minutes()

    for day, minutes in daily_totals.items():
        print(f"{day}: {minutes:g} minutes")

    print(f"\nWeekly total: {analytics.total_weekly_minutes():g} minutes")
    print(f"Daily average: {analytics.average_daily_minutes():.2f} minutes")

    productive_day = analytics.most_productive_day()
    if productive_day is None:
        print("Most productive day: No study sessions this week.")
    else:
        print(f"Most productive day: {productive_day}")





def monthly_study_report_menu():
    import json
    from pathlib import Path

    print("\n------ MONTHLY STUDY REPORT ------")

    session_path = Path("data/sessions.json")

    if session_path.exists():
        with session_path.open("r", encoding="utf-8") as file:
            sessions = json.load(file)
    else:
        sessions = []

    clean_data = StudyDataPreprocessor().preprocess_sessions(sessions)
    analytics = MonthlyStudyAnalytics(clean_data)
    report = MonthlyStudyReport(analytics)
    report.generate_report()



def monthly_goal_menu():
    import json
    from pathlib import Path

    goal_tracker = MonthlyGoalTracker()

    while True:
        print("\n------ MONTHLY STUDY GOALS ------")
        print("1. Set Monthly Study Goal")
        print("2. View Goal vs Actual")
        print("3. View Goal Progress Chart")
        print("4. View Goal Achievement Insights")
        print("5. View Monthly Performance Rating")
        print("6. View Monthly Performance History")
        print("7. View Monthly Performance Trend")
        print("8. Performance Recommendations")
        print("9. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                minutes = get_positive_number(
                    "Enter monthly study goal in minutes: "
                )
                goal_tracker.set_monthly_goal(minutes)
                print(f"Monthly study goal set to {minutes:g} minutes.")
            except ValueError as error:
                print(f"Could not set goal: {error}")

        elif choice in ("2", "3", "4", "5"):
            session_path = Path("data/sessions.json")

            if session_path.exists():
                with session_path.open("r", encoding="utf-8") as file:
                    sessions = json.load(file)
            else:
                sessions = []

            clean_data = StudyDataPreprocessor().preprocess_sessions(sessions)
            analytics = MonthlyStudyAnalytics(clean_data)
            goal = goal_tracker.get_monthly_goal()
            actual = analytics.total_monthly_minutes()

            if choice == "2":
                report = MonthlyGoalReport(goal_tracker, analytics)
                report.generate_report()

            elif choice == "3":
                visualizer = StudyVisualizer()
                visualizer.plot_monthly_goal_vs_actual(goal, actual)

            elif choice == "4":
                insights = MonthlyGoalInsights()
                result = insights.analyze_progress(goal, actual)

                print("\n====== MONTHLY GOAL ACHIEVEMENT INSIGHTS ======")
                print(f"Goal: {goal:g} minutes")
                print(f"Actual Study Time: {actual:g} minutes")
                print(
                    f"Completion: {result['completion_percentage']:.2f}%"
                )
                print(
                    f"Remaining Study Time: "
                    f"{result['remaining_minutes']:g} minutes"
                )
                print(f"Progress Status: {result['status']}")
                print("================================================")

            elif choice == "5":
                session_count = analytics.total_monthly_sessions()
                performance = MonthlyPerformanceRating()
                result = performance.calculate_rating(
                    goal, actual, session_count
                )

                print("\n====== MONTHLY STUDY PERFORMANCE ======")
                print(f"Overall Score: {result['overall_score']}/100")
                print(f"Performance Rating: {result['rating']}")
                print(f"Goal Score: {result['goal_score']}/100")
                print(f"Study Time Score: {result['time_score']}/100")
                print(f"Session Score: {result['session_score']}/100")
                print("=======================================")

        elif choice == "6":
            from src.monthly_performance_history import MonthlyPerformanceHistory

            history_manager = MonthlyPerformanceHistory()
            history_manager.display_history()

            if len(history_manager.get_history()) >= 2:
                compare = input("Compare two months? (y/n): ").strip().lower()

                if compare == "y":
                    month1 = input("First month (e.g. October): ").strip()
                    year1 = int(input("First year: "))
                    month2 = input("Second month (e.g. November): ").strip()
                    year2 = int(input("Second year: "))

                    history_manager.compare_months(
                        month1, year1, month2, year2
                    )

        elif choice == "7":
            from src.monthly_performance_visualizer import MonthlyPerformanceVisualizer

            trend_visualizer = MonthlyPerformanceVisualizer()
            trend_visualizer.plot_performance_trend()

        elif choice == "8":
            import json
            from pathlib import Path
            from src.performance_recommendations import PerformanceRecommendations

            session_path = Path("data/sessions.json")
            if session_path.exists():
                with session_path.open("r", encoding="utf-8") as file:
                    sessions = json.load(file)
            else:
                sessions = []

            clean_data = StudyDataPreprocessor().preprocess_sessions(sessions)
            analytics = MonthlyStudyAnalytics(clean_data)
            goal = goal_tracker.get_monthly_goal()
            actual = analytics.total_monthly_minutes()
            session_count = analytics.total_monthly_sessions()

            performance = MonthlyPerformanceRating()
            result = performance.calculate_rating(goal, actual, session_count)

            engine = PerformanceRecommendations()
            insights = engine.generate_recommendations(result)

            print("\n====== PERFORMANCE RECOMMENDATIONS ======")
            print(f"Performance Rating: {insights['rating']}")
            print(f"Overall Score: {insights['overall_score']}/100")
            print(f"Summary: {insights['summary']}")
            print("\nRecommended Actions:")
            for number, recommendation in enumerate(
                insights["recommendations"], start=1
            ):
                print(f"{number}. {recommendation}")
            print("=========================================")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")

def improvement_tracker_menu():

    tracker = ImprovementTracker()

    while True:
        print("\n------ STUDY IMPROVEMENT TRACKER ------")
        print("1. Add Improvement Task")
        print("2. View Improvement Tasks")
        print("3. Mark Task as Completed")
        print("4. View Progress Summary")
        print("5. View Improvement Analytics")
        print("6. Record Improvement Snapshot")
        print("7. View Improvement History Trend")
        print("8. Compare Latest Progress")
        print("9. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            description = input("Enter improvement task: ")
            try:
                task = tracker.add_task(description)
                print(f"Task added successfully. ID: {task['id']}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            tasks = tracker.get_tasks()

            if not tasks:
                print("No improvement tasks found.")
            else:
                print("\n------ IMPROVEMENT TASKS ------")
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(
                        f"{task['id']}. {task['description']} "
                        f"[{status}]"
                    )

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                if tracker.mark_completed(task_id):
                    print("Task marked as completed.")
                else:
                    print("Task ID not found.")
            except ValueError:
                print("Please enter a valid numeric task ID.")

        elif choice == "4":
            tasks = tracker.get_tasks()
            total = len(tasks)
            completed = sum(1 for task in tasks if task["completed"])
            pending = total - completed
            percentage = (completed / total * 100) if total else 0

            print("\n------ IMPROVEMENT PROGRESS ------")
            print(f"Total Tasks: {total}")
            print(f"Completed: {completed}")
            print(f"Pending: {pending}")
            print(f"Completion Rate: {percentage:.1f}%")

        elif choice == "5":
            from src.improvement_analytics import ImprovementAnalytics

            analytics = ImprovementAnalytics(tracker.get_tasks())
            analytics.display_summary()
            analytics.plot_progress()

        elif choice == "6":

            history = ImprovementHistory()
            snapshot = history.record_snapshot(tracker.get_tasks())

            print("\\nImprovement snapshot saved:")
            print(f"Date: {snapshot['date']}")
            print(f"Total Tasks: {snapshot['total']}")
            print(f"Completed: {snapshot['completed']}")
            print(f"Pending: {snapshot['pending']}")
            print(
                f"Completion Rate: "
                f"{snapshot['completion_percentage']:.2f}%"
            )

        elif choice == "7":


            history = ImprovementHistory()
            history.display_history()

            visualizer = ImprovementHistoryVisualizer(history)
            visualizer.plot_completion_trend()

        elif choice == "8":
            history = ImprovementHistory()
            records = history.get_history()

            comparison = ImprovementComparison(records)
            comparison.display_comparison()

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    note_manager = NoteManager()
    task_manager = TaskManager()
    planner = StudyPlanner()
    analytics = NoteAnalytics(note_manager.get_notes())
    processor=TextProcessor()
    visualizer = StudyVisualizer()
    session_tracker = StudySessionTracker()
    goal_tracker = StudyGoalTracker()
    tracker = ImprovementTracker()

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
        print("7. Study Progress")
        print("8. Study Sessions")
        print("9. Study Goals")
        print("10. Weekly Analytics")
        print("11. Monthly Study Report")
        print("12. Monthly Study Goals")
        print("13.Study Improvement Tracker")
        print("14. Exit")

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
        elif choice == "7":
            print("\n------ STUDY PROGRESS ------")

            progress = StudyProgress(task_manager.tasks)

            print(f"Total tasks: {progress.total_tasks()}")
            print(f"Completed tasks: {progress.completed_tasks()}")
            print(f"Pending tasks: {progress.pending_tasks()}")
            print(
                f"Completion: "
                f"{progress.completion_percentage():.2f}%"
            )

            print("\n1. View Progress Chart")
            print("2. Back")

            progress_choice = input("Enter your choice: ")

            if progress_choice == "1":
                completed = progress.completed_tasks()
                pending = progress.pending_tasks()

                visualizer.plot_task_progress(
                    completed,
                    pending
                )

            elif progress_choice == "2":
                pass

            else:
                print("Invalid choice.")
        elif choice == "8":
            study_sessions_menu(session_tracker, visualizer)

        elif choice == "9":
            study_goals_menu(goal_tracker)

        elif choice == "10":
            weekly_analytics_menu()

        elif choice == "11":
            monthly_study_report_menu()

        elif choice == "12":
            monthly_goal_menu()

        elif choice == "13":
            improvement_tracker_menu()
            break
        elif choice=="14":
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
