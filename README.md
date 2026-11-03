# PetPal – Pet Care Management System

The PetPal Project is a Python-based project that demonstrates the implementation of Object-Oriented Programming (OOP) concepts, including **Encapsulation, Inheritance, Polymorphism, and Abstraction**. It includes three main classes: `Pet`, `CareTask`, and `PetManager`, along with a frontend implemented in `main.py` and utility functions in `utility.py`. The project provides a simple platform for managing pet information and organising daily care activities while demonstrating the practical application of OOP principles.

## Table of Contents

- [Introduction](#introduction)
- [Classes](#classes)
  - [Pet](#pet)
  - [CareTask](#caretask)
  - [PetManager](#petmanager)
  - [Frontend](#frontend)
- [Utility Functions](#utility-functions)

## Introduction

The PetPal Project demonstrates the implementation of object-oriented programming concepts in Python. It provides a basic pet care management system where users can maintain pet profiles, organise care tasks, and track their completion status.

The project consists of three primary classes, each serving a distinct purpose:

### Pet

The `Pet` class represents an individual pet with the following attributes:

- `pet_id`: A unique identification number assigned to the pet.
- `name`: The name of the pet.
- `species`: The species of the pet.
- `breed`: The breed of the pet.
- `age`: The age of the pet.
- `care_tasks`: A list containing the care tasks associated with the pet.

This class provides methods to:

- Add care tasks to a pet.
- Display pet information.
- Convert pet details into a dictionary for data storage.
- Reconstruct pet objects from stored data.

### CareTask

The `CareTask` class represents an individual care activity associated with a pet. It includes the following attributes:

- `task_id`: A unique identification number for the task.
- `task_name`: The name or description of the care activity.
- `date`: The scheduled date of the activity.
- `notes`: Additional information about the task.
- `completed`: Indicates whether the task has been completed.

This class provides methods to:

- Mark a care task as completed.
- Display task information and its current status.
- Convert task details into a dictionary.
- Reconstruct care task objects from stored data.

### PetManager

The `PetManager` class is responsible for managing the collection of registered pets. It offers functionalities to:

- Add a new pet.
- View all registered pets.
- Search for a pet using its identification number.
- Add care tasks to a particular pet.
- View the care tasks associated with a pet.
- Mark care tasks as completed.
- Delete a pet from the system.
- Save and retrieve pet information using JSON file handling.

### Frontend

The frontend, implemented in `main.py`, provides a menu-driven interface for interacting with the `PetManager` class. Users can perform actions such as:

- Adding new pet profiles.
- Viewing all registered pets.
- Adding care tasks.
- Viewing existing care tasks.
- Marking tasks as completed.
- Deleting pet profiles.
- Exiting the application.

## Utility Functions

The `utility.py` file contains reusable helper functions that simplify input handling and improve the usability of the application.

It provides functionalities to:

- Validate pet age input.
- Validate dates entered by the user.
- Display formatted headings for different sections of the application.

## Data Storage

The project uses JSON file handling to store pet profiles and their associated care tasks in `pets.json`. This allows the application to retain information even after it has been closed and restarted.

## Technologies Used

- Python
- Object-Oriented Programming
- JSON
- File Handling
- Exception Handling
