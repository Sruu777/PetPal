import json
import os

from pet import Pet
from care_task import CareTask


class PetManager:

    def __init__(self):
        self.filename = "data/pets.json"
        self.pets = self.load_pets()

    def load_pets(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            data = json.load(file)

        pets = []

        for pet_data in data:
            pet = Pet.from_dict(pet_data)
            pets.append(pet)

        return pets

    def save_pets(self):
        data = []

        for pet in self.pets:
            data.append(pet.to_dict())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_pet(self, name, species, breed, age):
        pet_id = max(
            [pet.pet_id for pet in self.pets],
            default=0
        ) + 1

        pet = Pet(pet_id, name, species, breed, age)

        self.pets.append(pet)
        self.save_pets()

        print("\nPet added successfully!")

    def view_pets(self):
        if not self.pets:
            print("\nNo pets registered yet.")
            return

        for pet in self.pets:
            pet.display()

    def find_pet(self, pet_id):
        for pet in self.pets:
            if pet.pet_id == pet_id:
                return pet

        return None

    def add_care_task(self, pet_id, task_name, date, notes):
        pet = self.find_pet(pet_id)

        if pet is None:
            print("\nPet not found!")
            return

        task_id = len(pet.care_tasks) + 1

        task = CareTask(task_id, task_name, date, notes)

        pet.add_task(task)
        self.save_pets()

        print("\nCare task added successfully!")

    def view_care_tasks(self, pet_id):
        pet = self.find_pet(pet_id)

        if pet is None:
            print("\nPet not found!")
            return

        if not pet.care_tasks:
            print("\nNo care tasks available.")
            return

        for task in pet.care_tasks:
            print()
            task.display()

    def complete_task(self, pet_id, task_id):
        pet = self.find_pet(pet_id)

        if pet is None:
            print("\nPet not found!")
            return

        for task in pet.care_tasks:
            if task.task_id == task_id:
                task.mark_completed()
                self.save_pets()
                print("\nTask marked as completed!")
                return

        print("\nTask not found!")

    def delete_pet(self, pet_id):
        pet = self.find_pet(pet_id)

        if pet is None:
            print("\nPet not found!")
            return

        self.pets.remove(pet)
        self.save_pets()

        print("\nPet deleted successfully!")
