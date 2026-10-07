class StudyProgress:

    def __init__(self, tasks):
        self.tasks = tasks

    def total_tasks(self):
        return len(self.tasks)

    def completed_tasks(self):
        return sum(
            1 for task in self.tasks
            if task["completed"]
        )

    def pending_tasks(self):
        return self.total_tasks() - self.completed_tasks()

    def completion_percentage(self):
        total = self.total_tasks()

        if total == 0:
            return 0

        completed = self.completed_tasks()

        return (completed / total) * 100