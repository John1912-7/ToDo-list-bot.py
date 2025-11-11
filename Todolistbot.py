todo_list = []
while True:
    if len(todo_list) == 0:
        print("Your toDo list is empthy")
    else:  
        index = 1
    for task in todo_list:
        print(f"{index}. {task}")
        index += 1
    print("Options")
    print("1) Add task")
    print("2) Remove task")
    print("3) Quit")
    choice = input()
    if choice == "1":
        print("Adding task")
        new_task = input("Write a task: ")
        todo_list.append(new_task)
        print(f"Task {new_task} added")
    elif choice == "2":
        if len(todo_list) == 0:
            print("Your toDo list is empthy")
        elif todo_list.pop():
            print("Removing task")
    elif choice == "3":
        print("Quitting")
        break
    
    
    