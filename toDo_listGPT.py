# قائمة لتخزين المهام
todo_list = []

while True:
    # طلب إدخال من المستخدم
    user_action = input("Please enter a command (add, view, remove, exit): ").strip().lower()

    # إضافة مهمة جديدة
    if user_action == "add":
        task = input("What's your task? ").strip()
        if task in todo_list:
            print("This task is already added!")
        else:
            todo_list.append(task)
            print("Task added successfully!")

    # عرض جميع المهام
    elif user_action == "view":
        if not todo_list:
            print("Your ToDo list is empty!")
        else:
            print("Your ToDo List:")
            for index, task in enumerate(todo_list, 1):
                print(f"{index}. {task}")

    # إزالة مهمة
    elif user_action == "remove":
        if not todo_list:
            print("There are no tasks to remove!")
        else:
            task = input("What task would you like to remove? ").strip()
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed successfully!")
            else:
                print("Task not found!")
                print(f"Your ToDo list: {todo_list}")

    # الخروج من البرنامج
    elif user_action == "exit":
        print("Goodbye!")
        break

    # معالجة الأوامر غير الصحيحة
    else:
        print("Invalid command! Please try again.")