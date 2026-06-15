import json


while True:
    print(f"1.Create a task\n2.Show all tasks")
    sel_number = int(input("Select number: "))
    if sel_number == 1:
        text = input("Enter task: ")
        deadline = input("Enter deadline: ")
        priority = input("Enter priority: ")
        task = {
            'text': text,
            'deadline': deadline,
            'priority': priority,
            'status': True
        }
        try:
            with open("task_list.json", "r", encoding="utf-8") as file:
                list_tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            list_tasks = []

        list_tasks.append(task)

        with open("task_list.json", "w", encoding="utf-8") as file:
            json.dump(list_tasks, file, ensure_ascii=False, indent=4)

        print('Task successfully added!')
        ques = input("Do you want continue?: ")
        if ques == 'yes':
            continue
        else:
            print('Goodbye!')
            break
    if sel_number == 2:
        try:
            with open("task_list.json", "r", encoding="utf-8") as file:
                list_tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("The list is empty.")

        print(list_tasks)
        ques = input("What task is completed?: ")
        for i in list_tasks:
            if i['text'].lower() == ques.lower():
                i['status'] = False

        with open("task_list.json", "w", encoding="utf-8") as file:
            json.dump(list_tasks, file, ensure_ascii=False, indent=4)

        if ques == 'no':
            print('Goodbye!')
            break
