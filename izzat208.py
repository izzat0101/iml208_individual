# UniMail Delivery System for UiTM Students

# Sample data for three students
students = [
    {"id": 2023167405, "name": "Ijat", "package": "Guitar"},
    {"id": 2023401832, "name": "Bella", "package": "Laptop"},
    {"id": 2023712463, "name": "Zaty", "package": "Album"},
]

# Function to display all students and their packages
def display_students():
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Package: {student['package']}")
    print("---------------------")

# Function to add a new student and package
def add_student():
    print("\n--- Add Student ---")
    new_id = int(input("Enter ID: "))
    new_name = input("Enter Name: ")
    new_package = input("Enter Package: ")
    students.append({"id": new_id, "name": new_name, "package": new_package})
    print(f"Student {new_name} added successfully!")

# Function to update a student's package
def update_package():
    print("\n--- Update Package ---")
    student_id = int(input("Enter Student ID: "))
    for student in students:
        if student["id"] == student_id:
            new_package = input(f"Enter new package for {student['name']}: ")
            student["package"] = new_package
            print(f"Package updated for {student['name']}!")
            return
    print("Student not found.")

# Function to delete a student
def delete_student():
    print("\n--- Delete Student ---")
    student_id = int(input("Enter Student ID: "))
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print(f"Student {student['name']} deleted successfully!")
            return
    print("Student not found.")

# Main menu
def main():
    while True:
        print("\n--- UniMail Delivery System ---")
        print("1. View All Students")
        print("2. Add New Student")
        print("3. Update Student Package")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            update_package()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()