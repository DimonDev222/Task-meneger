import json

FILE_NAME = "task_list.json"


def load_tasks():
    """Загрузка задач из файла."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    """Сохранение задач в файл."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


while True:
    print("\n1. Create a task\n2. Show all tasks\n3. Exit")

    try:
        sel_number = int(input("Select number: "))
    except ValueError:
        print("Please enter a valid number (1, 2, or 3)!")
        continue

    if sel_number == 1:
        task = {
            'text': input("Enter task: "),
            'deadline': input("Enter deadline: "),
            'priority': input("Enter priority: "),
            'status': True
        }

        list_tasks = load_tasks()
        list_tasks.append(task)
        save_tasks(list_tasks)
        print('Task successfully added!')

    elif sel_number == 2:
        list_tasks = load_tasks()

        if not list_tasks:
            print("The list is empty.")
            continue

        print("\n--- YOUR TASKS ---")
        for idx, t in enumerate(list_tasks, 1):
            status = "🟢 Active" if t['status'] else "🔴 Completed"
            print(
                f"{idx}. {t['text']} (Deadline: {t['deadline']}, Priority: {t['priority']}) - {status}")

        ques = input(
            "\nEnter the task name to complete (or press Enter to skip): ")
        if ques:
            task_found = False
            for t in list_tasks:
                if t['text'].lower() == ques.lower():
                    t['status'] = False
                    task_found = True

            if task_found:
                save_tasks(list_tasks)
                print("Task status updated!")
            else:
                print("Task not found.")

    elif sel_number == 3:
        print('Goodbye!')
        break

    else:
        print("Unknown option. Please choose 1, 2, or 3.")
