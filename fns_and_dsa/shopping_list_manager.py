def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item you want to add: ")
            shopping_list.append(item)
            print(f"You added {item} to your shopping list.")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            if len(shopping_list) == 0:
                print("There are no items in your list to remove")
            else:
                remove_item = input("Enter item you want to remove from shopping list")
                if remove_item not in shopping_list:
                    print("Item is not in list")
                else:
                    shopping_list.remove(remove_item)
                    print(f'You removed {remove_item} from your list')
            pass
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()