import json
import os


class TaskManager:
    def __init__(self):
        self.file_path = "data/tasks.json"
        self.tasks = []

        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({
            "task": task,
            "completed": False
        })

        self.save_tasks()

        print(f"Task added: {task}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n--- Study Tasks ---")

        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "○"
            print(f"{i}. [{status}] {task['task']}")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True

            self.save_tasks()

            print("Task completed!")
        else:
            print("Invalid task number.")