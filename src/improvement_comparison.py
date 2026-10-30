
class ImprovementComparison:
    def __init__(self, history):
        self.history = history

    def compare_latest(self):
        if len(self.history) < 2:
            print("At least two snapshots are required for comparison.")
            return None

        previous = self.history[-2]
        latest = self.history[-1]

        comparison = {
            "completed_change": latest["completed"] - previous["completed"],
            "pending_change": latest["pending"] - previous["pending"],
            "completion_change": round(
                latest["completion_percentage"] -
                previous["completion_percentage"], 2
            )
        }

        return comparison

    def display_comparison(self):
        comparison = self.compare_latest()

        if comparison is None:
            return

        print("\n====== STUDY IMPROVEMENT COMPARISON ======")
        print(f"Completed Tasks Change: {comparison['completed_change']:+}")
        print(f"Pending Tasks Change: {comparison['pending_change']:+}")
        print(f"Completion Rate Change: {comparison['completion_change']:+.2f}%")

        if comparison["completion_change"] > 0:
            print("Result: Study progress has improved!")
        elif comparison["completion_change"] < 0:
            print("Result: Study progress has declined.")
        else:
            print("Result: Study progress remains unchanged.")

        print("==========================================")
        return comparison
