todo_list = []

while (True):

     user_action = input("Please enter a command (add, view, remove, exit): ")

     if (user_action == "add"):
            task = input("what's your task?")
            if task in todo_list:
                print("this task is already added")
            else:
                todo_list.append(task)
                print("task added.")

     elif(user_action == "view"):
          if not todo_list:
             print("your list is empty!")
          else:
             print(f"Your ToDo List is:" , todo_list)

     elif(user_action == "remove"):
          if not todo_list:
                 print("there are no tasks to remove")
                 
          else:
               task = input("what's your task?")
               if task in todo_list :
                    todo_list.remove(task)
                    print("your task is removed.")
               else:
                    print("task not found")
                    print( f"Your ToDo list is" , todo_list)
        
     elif (user_action == "exit"):
         print("good bye!")
         break
     else :
          print("Invaled Command!")
