import os
import tkinter as tk

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task.strip()}' deleted successfully.")
    else:
        print("Invalid task index.")

def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_tasks(filename='tasks.txt'):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.readlines()
    return tasks

def command_line_version():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == '4':
            save_tasks(tasks)
            print("Quitting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def gui_version():
    root = tk.Tk()
    root.title("Combined To-Do List")

    entry = tk.Entry(root, width=40, highlightbackground="pink", highlightthickness=2)
    entry.pack(pady=10)

    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, highlightbackground="pink", highlightthickness=2)
    listbox.pack(pady=10)

    def add_task_gui():
        new_task = entry.get()
        if new_task:
            listbox.insert(tk.END, new_task)
            entry.delete(0, tk.END)

    def delete_task_gui():
        selected_task_index = listbox.curselection()
        if selected_task_index:
            listbox.delete(selected_task_index)

    add_button = tk.Button(root, text="Add Task", command=add_task_gui)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
    delete_button.pack()

    root.mainloop()

def main():
    use_gui = input("Do you want to use the GUI version? (y/n): ").lower() == 'y'

    if use_gui:
        gui_version()
    else:
        command_line_version()

if __name__ == "__main__":
    main()
