#Paola Ramos Mendes
#CH7 Assignment
def main():
    # Here I created an empty list to store all the to-do items
    todoList = []
    
    # Here I initialized the variable 'choice' to control the loop
    choice = 0
    
    # Here I made a loop that keeps running until the user chooses option 4 (quit)
    while choice != 4:
        # Here I call the function to get the user's menu choice
        choice = GetMenuChoice()
        
        # Here I check if the user wants to add an item
        if choice == 1:
            AddItem(todoList)
        
        # Here I check if the user wants to remove an item
        elif choice == 2:
            RemoveItem(todoList)
        
        # Here I check if the user wants to display the list
        elif choice == 3:
            print(todoList)
        
        # Here I check if the user wants to quit the program
        elif choice == 4:
            print("Goodbye")
            

def GetMenuChoice():
    # Here I display the menu options for the user
    print("1) Add item to list \n2) Remove item from list \n3) Display list \n4) Quit program")
    
    # Here I ask the user to choose an option and convert it to an integer
    userChoice = int(input("Choose one of the options above: "))
    
    # Here I make sure the user enters a valid option (1–4)
    while userChoice not in [1, 2, 3, 4]:
        print("Invalid choice")
        userChoice = int(input("Choose one of the options above: "))
    
    # Here I return the valid choice back to the main function
    return userChoice

    
def AddItem(todoList):
    # Here I ask the user to enter a new to-do item
    userAdd = input("Enter the next To-Do item: ")
    
    # Here I add the item to the list
    todoList.append(userAdd)
    

def RemoveItem(todoList):
    # Here I ask the user which item they want to remove
    userRemove = input("What do you want to remove from the list? ")
    # Here I check if the item exists in the list
    if userRemove in todoList:
        # Here I remove the item from the list
        todoList.remove(userRemove)
    else:
        # Here I tell the user the item was not found
        print(f"{userRemove} was not found in the list")



# Here I make sure the program runs only when this file is executed
if __name__ == '__main__': 
   main()