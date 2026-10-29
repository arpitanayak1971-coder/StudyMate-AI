
import json
from datetime import date
from pathlib import Path


class ImprovementHistory:
    def __init__(self, file_path="data/improvement_history.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self._save_history([])

    def _load_history(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                records = json.load(file)
                return records if isinstance(records, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def _save_history(self, records):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    def record_snapshot(self, tasks):
        total = len(tasks)
        completed = sum(
            1 for task in tasks if task.get("completed", False)
        )
        pending = total - completed
        percentage = completed / total * 100 if total else 0

        snapshot = {
            "date": date.today().isoformat(),
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_percentage": round(percentage, 2)
        }

        history = self._load_history()
        history.append(snapshot)
        self._save_history(history)
        return snapshot

    def get_history(self):
        return self._load_history()

    def display_history(self):
        history = self.get_history()

        if not history:
            print("No improvement history recorded yet.")
            return

        print("\n====== STUDY IMPROVEMENT HISTORY ======")
        for record in history:
            print(
                f"{record['date']} | "
                f"Completed: {record['completed']}/"
                f"{record['total']} | "
                f"Pending: {record['pending']} | "
                f"Rate: {record['completion_percentage']:.2f}%"
            )
