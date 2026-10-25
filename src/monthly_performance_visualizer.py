import matplotlib.pyplot as plt
from datetime import datetime
from src.monthly_performance_history import MonthlyPerformanceHistory


class MonthlyPerformanceVisualizer:
    def __init__(self):
        self.history_manager = MonthlyPerformanceHistory()

    def plot_performance_trend(self):
        history = self.history_manager.get_history()

        if not history:
            print("No monthly performance history available.")
            return

        # Sort monthly records chronologically
        history = sorted(
            history,
            key=lambda record: datetime.strptime(
                f"{record['month']} {record['year']}",
                "%B %Y"
            )
        )

        months = [
            f"{record['month'][:3]} {record['year']}"
            for record in history
        ]

        scores = [
            record["overall_score"]
            for record in history
        ]

        plt.figure(figsize=(10, 5))
        plt.plot(months, scores, marker="o", linewidth=2)

        plt.title("Monthly Study Performance Trend")
        plt.xlabel("Month")
        plt.ylabel("Performance Score")
        plt.ylim(0, 100)
        plt.grid(True, linestyle="--", alpha=0.5)

        for index, score in enumerate(scores):
            plt.annotate(
                f"{score:.1f}",
                (index, score),
                textcoords="offset points",
                xytext=(0, 10),
                ha="center"
            )

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
