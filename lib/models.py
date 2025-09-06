# lib/models.py

class Task:
    """
    Represents a single task with a title and completion state.
    """
    def __init__(self, title: str):
        self.title = title
        self.completed = False

    def complete(self):
        # Mark complete and print confirmation (matches test expectation)
        if not self.completed:
            self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    """
    Represents a user who owns a list of tasks.
    """
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title: str):
        for t in self.tasks:
            if t.title == title:
                return t
        return None
