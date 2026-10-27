import json
from pathlib import Path


class ImprovementTracker:
    def __init__(self, file_path="data/improvement_tasks.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self._save_tasks([])

    def _load_tasks(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                tasks = json.load(file)
                return tasks if isinstance(tasks, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def _save_tasks(self, tasks):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)

    def add_task(self, description):
        description = description.strip()
        if not description:
            raise ValueError("Task description cannot be empty.")

        tasks = self._load_tasks()
        next_id = max(
            (task.get("id", 0) for task in tasks),
            default=0
        ) + 1

        task = {
            "id": next_id,
            "description": description,
            "completed": False
        }

        tasks.append(task)
        self._save_tasks(tasks)
        return task

    def get_tasks(self):
        return self._load_tasks()

    def mark_completed(self, task_id):
        tasks = self._load_tasks()

        for task in tasks:
            if task.get("id") == task_id:
                task["completed"] = True
                self._save_tasks(tasks)
                return True

        return False