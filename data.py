import random
import datetime
import pickle

# Expanded lists of random Indian first and last names
first_names = [
    "Aarav", "Vivaan", "Aditya", "Ishaan", "Vihaan", "Aanya", "Diya", 
    "Anika", "Aarohi", "Saanvi", "Ayush", "Priyanshu", "Anshu", "Priya", 
    "Rohan", "Arjun", "Kavya", "Sneha", "Neha", "Riya"
]
last_names = [
    "Sharma", "Verma", "Gupta", "Patel", "Mehta", "Agarwal", "Reddy", 
    "Singh", "Kumar", "Pandey", "Thakur", "Joshi", "Mishra", "Yadav", 
    "Choudhary", "Nair", "Pillai", "Desai", "Bose", "Chatterjee"
]
branches = ["CSE", "ECE", "ME", "CE", "EE", "IT", "AERO", "CHEM", "BIO", "ARCH"]

# Function to generate a random name
def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

# Function to generate a random email ID
def generate_email(name, index):
    email_provider = random.choice(["gmail.com", "yahoo.com", "outlook.com", "college.edu"])
    email_name = name.lower().replace(" ", ".")
    return f"{email_name}{index+1:04d}@{email_provider}"

# Function to generate random data for a student
def generate_student_data(index):
    reg_number = f"REG{index+1:04d}"  # Unique registration number, e.g., REG0001
    name = generate_name()  # Random Indian name
    branch = random.choice(branches)  # Randomly chosen branch
    dob = datetime.date(random.randint(1995, 2005), random.randint(1, 12), random.randint(1, 28))  # Random DOB
    mobile = f"9{random.randint(100000000, 999999999)}"  # Random mobile number
    email = generate_email(name, index)  # Random email

    return [reg_number, name, branch, dob, mobile, email]

# Generate data for 2000 students and store it in a binary file
with open("student_data.bin", "wb") as file:
    # First 3 students with specific details
    pickle.dump(["REG0001", "Ayush Karan", "CSE", "2000-01-15", "8873718596", "ayush.karan0001@gmail.com"], file)
    pickle.dump(["REG0002", "Kumar Priyanshu", "CSE", "2001-02-20", "8409701368", "kumar.priyanshu0002@yahoo.com"], file)
    pickle.dump(["REG0003", "Anshu Priya", "CSE", "1999-03-25", "9142714797", "anshu.priya0003@outlook.com"], file)

    # Generate the remaining random students
    for i in range(3, 2000):
        student_data = generate_student_data(i)
        pickle.dump(student_data, file)

print("Student data has been written to student_data.bin.")
