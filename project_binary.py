import pickle

stu_data = []

def entry(reg_n, nam, contact, cat, fb):
    feedback_entry = [reg_n, nam.upper(), contact, cat, fb]
    
    # Open the feedback file in binary append mode
    with open("feedback.bin", "ab") as y:
        # Dump feedback data into the binary file
        pickle.dump(feedback_entry, y)
        print("Feedback recorded successfully\n")


# Load the student data from the binary file
try:
    with open("student_data.bin", "rb") as x:
        while True:
            try:
                # Load each record one by one
                student_data = pickle.load(x)
                reg_no = student_data[0]
                name = student_data[1]
                mob = int(student_data[4])
                stu_data.append([reg_no, name.lower(), mob])
            except EOFError:
                break
except FileNotFoundError:
    print("Student data file not found. Please ensure the file exists.")

# To accept name and reg. no.:
nam = input("Enter your name: ").lower()
reg_n = input("Enter your registration number: ")
contact = int(input("Enter your mobile number: "))

# Check whether the student is present in the list and accept feedback:
student_found = False
for i in stu_data:
    if reg_n == i[0] and nam == i[1]:
        student_found = True
        print("Hello! Welcome to the feedback registration system")
        cat = input("Input the Category of your feedback (answer only in one word; e.g., faculty, library, clubs, technical): ")
        fb = input("Enter your detailed feedback: ")
        print(" ")
        print(f"Your final feedback related to '{cat}' is '{fb}'\n")
        ans = input("Final Submit (Y/N): ").lower()
        print(" ")
        if ans == 'y':
            entry(reg_n, nam, contact, cat, fb)
        break

if not student_found:
    print("Sorry! You are not registered in our system. Please contact the admin to register yourself\n")
