import os

class Task:

    def __init__(self, description, priority=0, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed

    def __str__(self):
        return f"{self.description} (Priority: {self.priority})"