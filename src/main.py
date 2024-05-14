from classes.TodoList import TodoList

def display_menu():
    print("Selectionnez une des options suivantes :")
    print("1 - Afficher la todolist")
    print("2 - Ajouter une tâche")
    print("3 - Retirer une tâche")
    print("4 - Exit")

def option1():
    pass

def option2():
    pass

def option3():
    pass

# Main function to handle menu
def main():

    task_file="tasks.txt"
    todolist = TodoList(task_file)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(todolist.tasks_list)1
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Check if the script is run as the main module
if __name__ == "__main__":
    # Call the main function
    main()