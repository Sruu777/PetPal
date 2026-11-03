class CareTask:

    def __init__(self, task_id, task_name, date, notes):
        self.task_id = task_id
        self.task_name = task_name
        self.date = date
        self.notes = notes
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"

        print("Task ID:", self.task_id)
        print("Task:", self.task_name)
        print("Date:", self.date)
        print("Notes:", self.notes)
        print("Status:", status)

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_name": self.task_name,
            "date": self.date,
            "notes": self.notes,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["task_id"],
            data["task_name"],
            data["date"],
            data["notes"]
        )

        task.completed = data["completed"]
        return task
