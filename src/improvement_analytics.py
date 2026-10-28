import matplotlib.pyplot as plt


class ImprovementAnalytics:
    def __init__(self, tasks):
        self.tasks = tasks

    def get_summary(self):
        total = len(self.tasks)
        completed = sum(
            1 for task in self.tasks
            if task.get("completed", False)
        )
        pending = total - completed

        percentage = (
            completed / total * 100
            if total > 0 else 0
        )

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_percentage": round(percentage, 2)
        }

    def display_summary(self):
        summary = self.get_summary()

        print("\\n====== STUDY IMPROVEMENT ANALYTICS ======")
        print(f"Total Tasks: {summary['total']}")
        print(f"Completed Tasks: {summary['completed']}")
        print(f"Pending Tasks: {summary['pending']}")
        print(
            f"Completion Rate: "
            f"{summary['completion_percentage']:.2f}%"
        )
        print("=========================================")

        return summary

    def plot_progress(self):
        summary = self.get_summary()

        labels = ["Completed", "Pending"]
        values = [summary["completed"], summary["pending"]]

        plt.figure(figsize=(7, 5))
        plt.bar(labels, values)
        plt.title("Study Improvement Task Progress")
        plt.ylabel("Number of Tasks")
        plt.tight_layout()
        plt.show()
