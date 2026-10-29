
import matplotlib.pyplot as plt
from src.improvement_history import ImprovementHistory


class ImprovementHistoryVisualizer:
    def __init__(self, history_manager=None):
        self.history_manager = (
            history_manager or ImprovementHistory()
        )

    def plot_completion_trend(self):
        history = self.history_manager.get_history()

        if not history:
            print("No history available to visualize.")
            return

        history = sorted(
            history,
            key=lambda record: record["date"]
        )

        dates = [record["date"] for record in history]
        percentages = [
            record["completion_percentage"]
            for record in history
        ]

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.plot(dates, percentages, marker="o")
        ax.set_title("Study Improvement Completion Trend")
        ax.set_xlabel("Snapshot Date")
        ax.set_ylabel("Completion Rate (%)")
        ax.set_ylim(0, 100)
        ax.tick_params(axis="x", rotation=30)

        for x, y in zip(dates, percentages):
            ax.annotate(
                f"{y:.1f}%",
                (x, y),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center"
            )

        fig.tight_layout()
        plt.show()
