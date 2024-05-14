import os

from classes.Task import Task

class TodoList:

    fileName=""

    def __init__(self, fileName):
        self.fileName = fileName
        self.tasks_list = []
        self.load_tasks()
        pass

    def load_tasks(self):
        if os.path.exists(self.fileName) :
            with open(self.fileName, "r") as f:
                for line in f :
                    description, priority, completed = line.strip().split('//')
                    self.tasks_list.append(Task(description, priority, completed))
    
