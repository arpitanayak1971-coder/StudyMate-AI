
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
