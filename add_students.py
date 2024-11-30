import pickle

# Function to add a new student
def add_student():
    reg_no = input("Enter registration number: ")
    name = input("Enter student name: ").title()
    branch = input("Enter branch: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    mobile = input("Enter mobile number: ")
    email = input("Enter email address: ")

    student_entry = [reg_no, name, branch, dob, mobile, email]

    try:
        # Append new student entry to the binary file
        with open("student_data.bin", "ab") as f:
            pickle.dump(student_entry, f)
        print("Student data added successfully.\n")

    except FileNotFoundError:
        print("Student data file not found. Creating a new file.")
        with open("student_data.bin", "wb") as f:
            pickle.dump(student_entry, f)
        print("Student data file created and student data added successfully.\n")

# Main loop for adding students
while True:
    print("1. Add New Student")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        print("Exiting system.")
        break
    else:
        print("Invalid choice, please try again.\n")
