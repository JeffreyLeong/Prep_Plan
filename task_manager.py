def display_menu():
    print("\t1. Add a task")
    print("\t2. Remove a task")
    print("\t3. Edit a task")
    print("\t4. View all tasks")
    print("\t5. Quit")

def add_task(list, item): 
    list.append(item)
    return list
    
def remove_task(list, item):
    list.remove(item)
    return list

def edit_task():
    pass

def view_task(list):
    for index, task in enumerate(list):
        print(f"{index}. {task}")

def quit_program():
    print("Goodbye!")
    
    
def main():
    print("Welcome to the Task Manager!\n")
    while True: 
        display_menu()
        try:
            number_selection = int(input("\nPlease type a number for the menu selection: "))
        except ValueError:
            print("Invalid input. Please try again")
            continue
        
        my_tasks = ["sleep", "write"]
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
                rm_task = input("Enter a task: ")
            except ValueError:
                print("Invalid input. Please try again")
                continue
            remove_task(my_tasks, task)
        elif number_selection == 4:
            view_task(my_tasks)
        elif number_selection == 5:
            quit_program()
            break
        else:
            print("Invalid selection. Please try again.\n")
            
if __name__ == "__main__":
    main()