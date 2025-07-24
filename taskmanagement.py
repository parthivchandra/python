class Task:
    task_id = 1

    def __init__(self, name, description):
        self.id = Task.task_id
        self.name = name
        self.description = description
        self.status = False  
        Task.task_id += 1

    def update(self,status):
        self.status = status


class Taskslist:
    def __init__(self):
        self.tasks = []

    def createtask(self):
        name = input('Enter your task name: ')
        description = input('Enter your task description: ')
        task = Task(name, description)
        self.tasks.append(task)
        print('Task added successfully.')

    def showlist(self):
        if len(self.tasks) == 0:
            print('No tasks found.')
        else:
            for task in self.tasks:
                print(f'\nTask ID: {task.id}')
                print(f'Name: {task.name}')
                print(f'Description: {task.description}')
                print(f'Status: {task.status}')

    def find_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self):
        try:
            task_id = int(input('Enter task ID to update: '))
            task = self.find_task(task_id)
            if task:
                status_input = input('Enter new status (true/false): ')
                status = True if status_input == 'true' else False
                task.update(status)
                print('Task status updated successfully.')
            else:
                print('Task not found.')
        except ValueError:
            print('Invalid task ID.')

    def delete(self):
        try:
            task_id = int(input('Enter task ID to delete: '))
            task = self.find_task(task_id)
            if task:
                self.tasks.remove(task)
                print('Task deleted successfully.')
            else:
                print('Task not found.')
        except ValueError:
            print('Invalid task ID.')

task_manager = Taskslist()

while True:
    print('\nTask Manager')
    print('1. Add task')
    print('2. Show tasks')
    print('3. Update task')
    print('4. Delete task')
    print('5. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        task_manager.createtask()
    elif choice == '2':
        task_manager.showlist()
    elif choice == '3':
        task_manager.update_task()
    elif choice == '4':
        task_manager.delete()
    elif choice == '5':
        break
    else:
        print('Invalid choice')