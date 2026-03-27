import json
import sys
from asyncio import tasks
from datetime import datetime


class Task:
    def __init__(self,id,title,status="Todo"):
        self.id = id
        self.title = title
        self.status= status
        self.created_at =datetime.now()

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "status":self.status,
            "created_at":self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["id"], data["title"], data["status"])
        task.created_at = datetime.fromisoformat(data["created_at"])  # Convert string back to datetime
        return task

class TaskManager:
    def __init__(self,file_path = "tasks.json"):
        self.file_path=file_path
        self.tasks=[]
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path) as f:
                tasks_data = json.load(f)
                self.tasks=[Task.from_dict(d) for d in tasks_data]
        except FileNotFoundError:
            self.tasks=[]
        except json.JSONDecodeError:
            print("Warning: JSON file is corrupt. Starting with empty task list.")
            self.tasks = []

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def new_task_id(self):
        if(self.tasks == []):
            return 1
        else:
            return max(task.id for task in self.tasks)+1


    def add_task(self,title):
        new_id = self.new_task_id()
        task=Task(id=new_id,title=title)
        self.tasks.append(task)
        self.save_tasks()
        print("Task Added with title",title)

    def complete_task(self,id):
        for task in self.tasks:
            if(task.id == id):
                task.status = "Done"
                self.save_tasks();
                print("Task Status updated with title",task.title)

    def list_tasks(self):
        for task in self.tasks:
            print(f"{task.id:8} || {task.title:9} || {task.status:9} || {task.created_at}")

    def delete_task(self,id):
        for oldTask in self.tasks:
            if(oldTask.id == id):
                self.tasks.remove(oldTask)
                self.save_tasks()
                print("Task Deleted with id",id)
                break

def main():
    manager = TaskManager()
    if len(sys.argv) < 2:
        print("Please provide a command: add, list, delete, done")
        return
    command = sys.argv[1]

    if command == "add":
        title = sys.argv[2]
        manager.add_task(title)

    elif command == "list":
        manager.list_tasks()

    elif command == "delete":
        task_id = int(sys.argv[2])
        manager.delete_task(task_id)

    elif command == "done":
        task_id = int(sys.argv[2])
        manager.complete_task(task_id)

    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

