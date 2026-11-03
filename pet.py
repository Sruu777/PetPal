from care_task import CareTask


class Pet:

    def __init__(self, pet_id, name, species, breed, age):
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.care_tasks = []

    def add_task(self, task):
        self.care_tasks.append(task)

    def display(self):
        print("\n-------------------------")
        print("Pet ID:", self.pet_id)
        print("Name:", self.name)
        print("Species:", self.species)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print("Number of care tasks:", len(self.care_tasks))
        print("-------------------------")

    def to_dict(self):
        return {
            "pet_id": self.pet_id,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "care_tasks": [task.to_dict() for task in self.care_tasks]
        }

    @classmethod
    def from_dict(cls, data):
        pet = cls(
            data["pet_id"],
            data["name"],
            data["species"],
            data["breed"],
            data["age"]
        )

        for task_data in data["care_tasks"]:
            task = CareTask.from_dict(task_data)
            pet.add_task(task)

        return pet
