"""
Student Record Manager
A menu-driven program to manage student records with file operations.
Author: Student
Date: May 2026
"""

import json
import os
from typing import List, Dict

# Global list to store student records
students: List[Dict] = []
FILENAME = "students.json"


def displayMenu() -> None:
    """Display the main menu and instructions."""
    print("\n" + "=" * 40)
    print("   STUDENT RECORD MANAGER")
    print("=" * 40)
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Show Statistics")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")
    print("=" * 40)


def validateMarks(marks: str) -> bool:
    """Validate that marks are between 0 and 100."""
    try:
        mark_value = float(marks)
        return 0 <= mark_value <= 100
    except ValueError:
        return False


def validateAge(age: str) -> bool:
    """Validate that age is a positive integer."""
    try:
        age_value = int(age)
        return age_value > 0
    except ValueError:
        return False


def addStudent() -> None:
    """Allow user to input student details with validation."""
    print("\n--- Add New Student ---")
    
    # Get Student ID
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Error: Student ID cannot be empty.")
        return
    
    # Check if ID already exists
    if any(student["id"] == student_id for student in students):
        print(f"Error: Student ID {student_id} already exists.")
        return
    
    # Get Name
    name = input("Enter Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    # Get Age with validation
    while True:
        age = input("Enter Age: ").strip()
        if validateAge(age):
            age = int(age)
            break
        print("Error: Please enter a valid positive age.")
    
    # Get Marks with validation
    while True:
        marks = input("Enter Marks (0-100): ").strip()
        if validateMarks(marks):
            marks = float(marks)
            break
        print("Error: Marks must be between 0 and 100.")
    
    # Add student to the list
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    print("✓ Student added successfully.")


def displayStudents() -> None:
    """Display all stored student records in a structured format."""
    if not students:
        print("\nNo student records found.")
        return
    
    print("\n" + "=" * 70)
    print(f"{'ID':<12} {'Name':<20} {'Age':<8} {'Marks':<10}")
    print("=" * 70)
    
    for student in students:
        print(f"{student['id']:<12} {student['name']:<20} {student['age']:<8} {student['marks']:<10.2f}")
    
    print("=" * 70)
    print(f"Total Students: {len(students)}")


def searchStudent() -> None:
    """Search for a student using Student ID."""
    if not students:
        print("\nNo student records found.")
        return
    
    student_id = input("\nEnter Student ID to search: ").strip()
    
    for student in students:
        if student["id"] == student_id:
            print("\n--- Student Found ---")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Marks: {student['marks']:.2f}")
            return
    
    print(f"\n✗ Student with ID '{student_id}' not found.")


def calculateStatistics() -> None:
    """Calculate and display statistics (highest, lowest, average marks)."""
    if not students:
        print("\nNo student records found.")
        return
    
    marks_list = [student["marks"] for student in students]
    
    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)
    
    print("\n" + "=" * 40)
    print("   STATISTICS")
    print("=" * 40)
    print(f"Total Students: {len(students)}")
    print(f"Highest Marks: {highest:.2f}")
    print(f"Lowest Marks: {lowest:.2f}")
    print(f"Average Marks: {average:.2f}")
    print("=" * 40)


def saveToFile() -> None:
    """Store all student records in a text file."""
    if not students:
        print("\nNo student records to save.")
        return
    
    try:
        with open(FILENAME, 'w') as file:
            json.dump(students, file, indent=4)
        print(f"✓ {len(students)} student record(s) saved to '{FILENAME}' successfully.")
    except IOError as e:
        print(f"✗ Error saving to file: {e}")


def loadFromFile() -> None:
    """Read records from a file and reconstruct data."""
    global students
    
    if not os.path.exists(FILENAME):
        print(f"\n✗ File '{FILENAME}' not found.")
        return
    
    try:
        with open(FILENAME, 'r') as file:
            loaded_data = json.load(file)
            if isinstance(loaded_data, list):
                students = loaded_data
                print(f"✓ {len(students)} student record(s) loaded from '{FILENAME}' successfully.")
            else:
                print("✗ Invalid file format.")
    except (IOError, json.JSONDecodeError) as e:
        print(f"✗ Error loading from file: {e}")


def main() -> None:
    """Main program loop - displays menu and processes user choices."""
    print("\nWelcome to Student Record Manager!")
    
    while True:
        displayMenu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            addStudent()
        elif choice == '2':
            displayStudents()
        elif choice == '3':
            searchStudent()
        elif choice == '4':
            calculateStatistics()
        elif choice == '5':
            saveToFile()
        elif choice == '6':
            loadFromFile()
        elif choice == '7':
            print("\nThank you for using Student Record Manager. Goodbye!")
            break
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
