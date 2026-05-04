def get_user_numbers():
    number_1 = float(input("Please enter a number: "))
    number_2 = float(input("Please enter a second number: "))
    return number_1, number_2

def display_menu():
    print("\t1. Add")
    print("\t2. Subtract")
    print("\t3. Multiply")
    print("\t4. Divide")
    print("\t5. Quit")
    
def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    if number_2 == 0:
        return None
    return number_1 / number_2

def display_answer(ans):
    print(f"\nResult: {ans:.2f}!\n")
    
def end_program():
    print("Goodbye!")

def calculate(operation):
    number_1, number_2 = get_user_numbers()
    answer = operation(number_1, number_2)
    if answer is None:
        print("Cannot divide by zero.\n")
        return
    display_answer(answer)
    
operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
}

def main():
    print("Welcome!\n")
    while True:
        display_menu()
        print()
        try:
            selection = int(input("Please select a number to request a operation: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        if selection in operations:
            calculate(operations[selection])
        elif selection == 5:
            end_program()
            break
        else:
            print("Invalid selection. Try again.\n")
        
if __name__ == "__main__":
    main()   