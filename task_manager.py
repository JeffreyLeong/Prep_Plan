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
    return list

def quit_program():
    print("Goodbye!")
    

def main():
    print("Welcome to the Task Manager!")
    while True: 
        display_menu()
        try:
            number_selection = int(input("Please type a number for the menu selection: "))
        except ValueError:
            print("Invalid input. Please try again")
            continue
        
        my_tasks = []
        if number_selection == 1:
            try:
                task = input("Enter a task: ")
            except ValueError:
                print("Invalid input. Please try again")
                continue
            add_task(my_tasks, task)
        elif number_selection == 2:
            try:
                rm_task = input("Enter a task: ")
            except ValueError:
                print("Invalid input. Please try again")
                continue
            remove_task(my_tasks, task)
            
            
                
        
        
        my_tasks = add_task(my_tasks, "eat")
        my_tasks = add_task(my_tasks, "sleep")
        print(my_tasks)
    
        


if __name__ == "__main__":
    main()