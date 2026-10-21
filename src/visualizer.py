
import matplotlib.pyplot as plt


class StudyVisualizer:

    def plot_notes_by_subject(self, subject_data):
        if not subject_data:
            print("No note data available for visualization.")
            return

        subjects = list(subject_data.keys())
        counts = list(subject_data.values())

        plt.figure(figsize=(8, 5))

        plt.bar(subjects, counts)

        plt.title("Notes by Subject")
        plt.xlabel("Subject")
        plt.ylabel("Number of Notes")

        plt.tight_layout()
        plt.show()

    def plot_notes_by_topic(self, topic_data):
        if not topic_data:
            print("No topic data available for visualization.")
            return

        topics = list(topic_data.keys())
        counts = list(topic_data.values())

        plt.figure(figsize=(8, 5))

        plt.bar(topics, counts)

        plt.title("Notes by Topic")
        plt.xlabel("Topic")
        plt.ylabel("Number of Notes")

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    def plot_task_progress(self, completed, pending):
        total = completed + pending

        if total == 0:
            print("No tasks available for visualization.")
            return

        labels = ["Completed", "Pending"]
        sizes = [completed, pending]

        plt.figure(figsize=(6, 6))

        plt.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Study Task Progress")
        plt.axis("equal")

        plt.show()

    def plot_study_time_by_subject(self, subject_data):
        if not subject_data:
            print("No study session data available for visualization.")
            return

        subjects = list(subject_data.keys())
        minutes = list(subject_data.values())

        plt.figure(figsize=(8, 5))
        plt.bar(subjects, minutes)
        plt.title("Study Time by Subject")
        plt.xlabel("Subject")
        plt.ylabel("Study Time (minutes)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_weekly_study_time(self, daily_totals):
        """Plot study minutes for each day of the week."""
        if not daily_totals:
            print("No weekly study data available for visualization.")
            return

        days = list(daily_totals.keys())
        minutes = list(daily_totals.values())

        if not any(minutes):
            print("No study time recorded for this week.")
            return

        plt.figure(figsize=(9, 5))
        plt.bar(days, minutes)

        plt.title("Weekly Study Time")
        plt.xlabel("Day")
        plt.ylabel("Study Time (minutes)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    def plot_goal_vs_actual(self, goal_minutes, actual_minutes):
        """Compare today's study time with the daily study goal."""
        if goal_minutes <= 0 or actual_minutes < 0:
            print("Goal must be positive and study time cannot be negative.")
            return

        labels = ["Daily Goal", "Actual Study Time"]
        values = [goal_minutes, actual_minutes]

        plt.figure(figsize=(7, 5))
        plt.bar(labels, values)

        plt.title("Daily Study Goal vs Actual Study Time")
        plt.ylabel("Study Time (minutes)")
        plt.tight_layout()
        plt.show()


    def plot_monthly_goal_vs_actual(self, goal_minutes, actual_minutes):
        """Compare monthly study time with the monthly study goal."""
        if goal_minutes <= 0 or actual_minutes < 0:
            print("Goal must be positive and study time cannot be negative.")
            return

        labels = ["Monthly Goal", "Actual Study Time"]
        values = [goal_minutes, actual_minutes]

        plt.figure(figsize=(7, 5))
        plt.bar(labels, values)
        plt.title("Monthly Study Goal vs Actual Study Time")
        plt.ylabel("Study Time (minutes)")
        plt.tight_layout()
        plt.show()

        percentage = (actual_minutes / goal_minutes) * 100
        print(f"Monthly goal completion: {percentage:.2f}%")

    def plot_monthly_study_time(self, subject_data):
        """Plot monthly study time for each subject."""
        if not subject_data:
            print("No monthly study data available for visualization.")
            return

        subjects = list(subject_data.keys())
        minutes = list(subject_data.values())

        if not any(minutes):
            print("No study time recorded for this month.")
            return

        plt.figure(figsize=(9, 5))
        plt.bar(subjects, minutes)

        plt.title("Monthly Study Time by Subject")
        plt.xlabel("Subject")
        plt.ylabel("Study Time (minutes)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
