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