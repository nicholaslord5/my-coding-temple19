# 1. City Infrastructure Management System
# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python 
# to build a simulated City Infrastructure Management System. This system will incorporate classes, 
# objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, 
# and events.

# Task 1: Vehicle Registration System

# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

#  - Code Example: Provide a basic structure for the Vehicle class without methods.

#    class Vehicle:
#        def __init__(self, reg_num, type, owner):
#            self.registration_number = reg_num
#            self.type = type
#            self.owner = owner
# - Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {new_owner} for vehicle with registration number {self.registration_number}")

vehicle1 = Vehicle("ABC123", "Car", "Homestar Runner")
vehicle2 = Vehicle("DEF456", "Truck", "Strong Bad")
vehicle3 = Vehicle("GHI789", "Van", "Marzipan")

#initial owner
print(f"Vehicle 1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
print(f"Vehicle 3 - Registration: {vehicle3.registration_number}, Type: {vehicle3.type}, Owner: {vehicle3.owner}")

#update owner
vehicle1.update_owner("Coach Z")
vehicle2.update_owner("Bubs")
vehicle3.update_owner("Homsar")

# display new owner
print(f"Vehicle 1 - Registration: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2 - Registration: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")
print(f"Vehicle 3 - Registration: {vehicle3.registration_number}, Type: {vehicle3.type}, Owner: {vehicle3.owner}")