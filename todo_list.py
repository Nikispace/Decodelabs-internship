print("TO-DO LISTS")


task_list = []
def addtasks():
    while True:
        adding_task = input("\nWanna add task? (yes/no):")
        if ((adding_task).lower() == "yes"):
            task = input("\nEnter the task:")
            task_list.append({"task_name": task, "completed": False })
        else:
            break
def display_all_tasks():
    print("\nAll Tasks")
    if task_list != []:
        for i,t in enumerate(task_list,1):
            if t["completed"]:
                status = "[Done]"
            else:
                status = "[ ]"
            print(f'{i} {t["task_name"]} - {status}')
    elif task_list == []:
        print("\nYou haven't addded any tasks yet! Start adding tasks!")
    else:
        print("\nSorry some error occured")
def add_completed_Tasks():
    n = int(input("Enter the task number that you've finished"))
    for i,t in enumerate(task_list,1):
        if i == n:
            t["completed"] = True
def completed_tasks():
    if task_list != []:
        for i,t in enumerate(task_list,1):
            if t["completed"]:
                status = "[Done]"
                print(f'{i} {t["task_name"]} - {status}')
def pending_tasks():
    if task_list != []:
        for i,t in enumerate(task_list,1):
            if not t["completed"]:
                status = "[ ]"
                print(f'{i} {t["task_name"]} - {status}')
def delete_task():
    if not task_list:
        print("\nNothing to delete!")

    try:
        n = int(input("\nEnter the task number you want to delete: "))
        if 1 <= n <= len(task_list):
            removed = task_list.pop(n-1)
            print(f"Task '{removed['task_name']}' deleted!")
        else:
            print("Invalid number.")
    except ValueError:
        print("\nPlease enter a valid number.")

def main_menu():
    while True:
        print("\nWELCOME TO TASKMASTER")
        print("\nTO-DO LIST MENU")
        print("1. Add Task")
        print("2. Display All Tasks")
        print("3. Mark The Tasks Completed")
        print("4. View Pending Tasks")
        print("5. View Completed Tasks")
        print("6. Delete a Task")
        print("7. Exit")
        
        ch = input("\nWhat would you like to do? (1-7): ")

        if ch == '1':
            addtasks()
        elif ch == '2':
            display_all_tasks()
        elif ch == '3':
            add_completed_Tasks()
        elif ch == '4':
            pending_tasks()
        elif ch == '5':
            completed_tasks()
        elif ch == '6':
            delete_task()
        elif ch == '7':
            print("Goodbye!")
            break  
        else:
            print("Invalid choice, please pick a number between 1 and 6.")

main_menu()

    
            
    
