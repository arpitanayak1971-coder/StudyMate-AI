class TaskManager: #taskmanager class object 
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({
            "task": task,
            "completed": False
        })
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
            print("Task completed!")
        else:
            print("Invalid task number.")


def main():
    manager = TaskManager()

    manager.add_task("Study Python")
    manager.add_task("Practice Machine Learning")
    manager.add_task("Read GenAI basics")

    manager.show_tasks()

    manager.complete_task(1)

    manager.show_tasks()


if __name__ == "__main__":
    main()
