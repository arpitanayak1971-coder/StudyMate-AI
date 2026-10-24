import json
from pathlib import Path
from datetime import datetime


class MonthlyPerformanceHistory:
    def __init__(self, file_path="data/performance_history.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self._save([])

    def _load(self):
        with self.file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _save(self, history):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def save_performance(self, month, year, result):
        history = self._load()

        record = {
            "month": month,
            "year": year,
            "overall_score": result["overall_score"],
            "rating": result["rating"],
            "goal_score": result["goal_score"],
            "time_score": result["time_score"],
            "session_score": result["session_score"],
            "saved_at": datetime.now().isoformat(timespec="seconds")
        }

        for index, existing in enumerate(history):
            if existing["month"] == month and existing["year"] == year:
                history[index] = record
                self._save(history)
                return "Monthly performance record updated."

        history.append(record)
        history.sort(key=lambda item: (item["year"], item["month"]))
        self._save(history)
        return "Monthly performance record saved."

    def get_history(self):
        return self._load()

    def display_history(self):
        history = self.get_history()

        if not history:
            print("No monthly performance history available.")
            return

        print("\n========== MONTHLY PERFORMANCE HISTORY ==========")
        print(f"{'Month':<15}{'Score':<12}{'Rating':<22}")
        print("-" * 49)

        for record in history:
            period = f"{record['month']} {record['year']}"
            score = f"{record['overall_score']}/100"
            print(f"{period:<15}{score:<12}{record['rating']:<22}")

        print("=" * 49)

    def compare_months(self, month1, year1, month2, year2):
        history = self.get_history()

        first = next(
            (r for r in history
             if r["month"] == month1 and r["year"] == year1),
            None
        )
        second = next(
            (r for r in history
             if r["month"] == month2 and r["year"] == year2),
            None
        )

        if first is None or second is None:
            print("One or both monthly records were not found.")
            return None

        difference = round(
            second["overall_score"] - first["overall_score"], 2
        )

        if difference > 0:
            status = "Improved"
        elif difference < 0:
            status = "Declined"
        else:
            status = "Unchanged"

        print("\n========== MONTHLY COMPARISON ==========")
        print(f"First month: {month1} {year1} - {first['overall_score']}/100")
        print(f"Second month: {month2} {year2} - {second['overall_score']}/100")
        print(f"Score difference: {difference:+.2f}")
        print(f"Performance: {status}")
        print("========================================")

        return {"difference": difference, "status": status}
