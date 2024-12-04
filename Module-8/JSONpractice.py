#Jose Franco
#12/03/2024
#Assignment 8.2 - JSON Practice
#Creating a Python program that loads, modifies,
#and optionally saves changes to a JSON file containing student information.

import json

# File path
file_path = "student.json"

# Function to print student list
def print_students(student_list, message):
    print(message)
    for student in student_list:
        print(f"{student['F_Name']}, {student['L_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")
    print()

# Function to load student list
def load_students(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Function to save updated student list to JSON file
def save_students(file_path, student_list):
    with open(file_path, "w") as file:
        json.dump(student_list, file, indent=4)

# Main program flow
if __name__ == "__main__":
    # Step 1: Load and print the original student list
    students = load_students(file_path)
    print_students(students, "Original Student List:")

    # Step 2: Append new student details
    new_student = {
        "F_Name": "Jose",
        "L_Name": "Franco",
        "Student_ID": 16411875,
        "Email": "jofranco@my365.bellevue.edu"
    }
    students.append(new_student)

    # Step 3: Print the updated student list
    print_students(students, "Updated Student List:")

    # Step 4: Save updated student list to the file
    save_students(file_path, students)
    print("The student.json file was updated.")
