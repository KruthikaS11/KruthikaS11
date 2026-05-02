tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    except:
        tasks = []

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Load tasks at start
load_tasks()

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")