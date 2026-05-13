def display_menu():
    print("\t1. Add a task")
    print("\t2. Remove a task")
    print("\t3. Change a task")
    print("\t4. View all tasks")
    print("\t5. Quit")

def add_task(tasks_list, item): 
    tasks_list.append(item)

def remove_task(tasks_list, item):
    tasks_list.pop(item)

def change_task(tasks_list, index, new_value):
    index = index - 1
    tasks_list[index] = new_value
    
def view_task(tasks_list):
    for index, task in enumerate(tasks_list):
        print(f"{index+1}. {task.capitalize()}")

def quit_program():
    print("Goodbye!")
    
def main():
    print("Welcome to the Task Manager!\n")
    my_tasks = []
    while True: 
        display_menu()
        try:
            number_selection = int(input("\nPlease type a number for the menu selection: "))
        except ValueError:
            print("Invalid input. Please try again")
            continue
        if number_selection == 1:
            try:
                task = input("Enter a task: ")
            except ValueError:
                print("Invalid input. Please try again")
                continue
            add_msg = "Adding task ..."
            print()
            for i in range(3):
                print(add_msg)
            add_task(my_tasks, task)
            print("\nTask added.\n")
        elif number_selection == 2:
            try:
                user_facing_task_number = int(input("Type in task number: "))
                actual_index_list = user_facing_task_number - 1
            except ValueError:
                print("Invalid input. Please try again")
                continue
            remove_task(my_tasks, actual_index_list)
        elif number_selection == 3:
            try:
                task_selection_index = int(input("Type in a task number: "))
                new_task = input("Please enter a new task: ")
            except ValueError:
                print("Invalid input. Please try again")
                continue
            change_task(my_tasks, task_selection_index, new_task)
        elif number_selection == 4:
            view_task(my_tasks)
            if my_tasks == []:
                print("No tasks")
        elif number_selection == 5:
            quit_program()
            break
        else:
            print("Invalid selection. Please try again.\n")
            
if __name__ == "__main__":
    main()