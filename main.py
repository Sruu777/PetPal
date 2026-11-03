from pet_manager import PetManager


def display_menu():
    print("\n========== PETPAL ==========")
    print("1. Add a pet")
    print("2. View all pets")
    print("3. Add a care task")
    print("4. View care tasks")
    print("5. Mark task as completed")
    print("6. Delete a pet")
    print("7. Exit")
    print("============================")


def main():

    manager = PetManager()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter pet name: ")
            species = input("Enter species: ")
            breed = input("Enter breed: ")
            age = int(input("Enter age: "))

            manager.add_pet(name, species, breed, age)

        elif choice == "2":

            manager.view_pets()

        elif choice == "3":

            pet_id = int(input("Enter pet ID: "))
            task_name = input("Enter task name: ")
            date = input("Enter date (DD-MM-YYYY): ")
            notes = input("Enter notes: ")

            manager.add_care_task(
                pet_id, task_name, date, notes
            )

        elif choice == "4":

            pet_id = int(input("Enter pet ID: "))
            manager.view_care_tasks(pet_id)

        elif choice == "5":

            pet_id = int(input("Enter pet ID: "))
            task_id = int(input("Enter task ID: "))

            manager.complete_task(pet_id, task_id)

        elif choice == "6":

            pet_id = int(input("Enter pet ID: "))
            manager.delete_pet(pet_id)

        elif choice == "7":

            print("\nThank you for using PetPal!")
            break

        else:

            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
