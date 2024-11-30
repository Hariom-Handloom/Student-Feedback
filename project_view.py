# PROGRAM FOR FACULTY TO VIEW THE FEEDBACK

import pickle
import os

# Function to view all feedback
def view_feedback():
    try:
        with open("feedback.bin", "rb") as f:
            print("\n--- All Feedbacks ---")
            while True:
                try:
                    feedback_entry = pickle.load(f)
                    print(f"Reg No: {feedback_entry[0]}, Name: {feedback_entry[1]}, Contact: {feedback_entry[2]}")
                    print(f"Category: {feedback_entry[3]}, Feedback: {feedback_entry[4]}\n")
                except EOFError:
                    break
    except FileNotFoundError:
        print("Feedback file not found. No feedbacks to display.\n")

# Function to respond to feedback
def respond_feedback():
    try:
        with open("feedback.bin", "rb") as f:
            feedbacks = []
            while True:
                try:
                    feedback_entry = pickle.load(f)
                    feedbacks.append(feedback_entry)
                except EOFError:
                    break

        if feedbacks:
            print("\n--- Available Feedbacks ---")
            for idx, feedback_entry in enumerate(feedbacks, start=1):
                print(f"{idx}. Reg No: {feedback_entry[0]}, Name: {feedback_entry[1]}, Category: {feedback_entry[3]}")
            choice = int(input("\nSelect feedback to respond (Enter number): ")) - 1

            if 0 <= choice < len(feedbacks):
                response = input(f"Enter your response to feedback from {feedbacks[choice][1]}: ")
                feedbacks[choice].append(response)
                print("Response recorded successfully.\n")

                # Save updated feedback with response
                with open("feedback.bin", "wb") as f:
                    for fb in feedbacks:
                        pickle.dump(fb, f)

            else:
                print("Invalid selection.\n")
        else:
            print("No feedbacks available to respond.\n")

    except FileNotFoundError:
        print("Feedback file not found. No feedbacks to respond to.\n")

# Function to delete specific feedback
def delete_feedback():
    try:
        with open("feedback.bin", "rb") as f:
            feedbacks = []
            while True:
                try:
                    feedback_entry = pickle.load(f)
                    feedbacks.append(feedback_entry)
                except EOFError:
                    break

        if feedbacks:
            print("\n--- Available Feedbacks ---")
            for idx, feedback_entry in enumerate(feedbacks, start=1):
                print(f"{idx}. Reg No: {feedback_entry[0]}, Name: {feedback_entry[1]}, Category: {feedback_entry[3]}")
            choice = int(input("\nSelect feedback to delete (Enter number): ")) - 1

            if 0 <= choice < len(feedbacks):
                feedbacks.pop(choice)
                print("Feedback deleted successfully.\n")

                # Save updated feedbacks after deletion
                with open("feedback.bin", "wb") as f:
                    for fb in feedbacks:
                        pickle.dump(fb, f)

            else:
                print("Invalid selection.\n")
        else:
            print("No feedbacks available to delete.\n")

    except FileNotFoundError:
        print("Feedback file not found. No feedbacks to delete.\n")

# Main loop for faculty actions
while True:
    print("1. View Feedbacks")
    print("2. Respond to Feedback")
    print("3. Delete Feedback")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        view_feedback()
    elif choice == '2':
        respond_feedback()
    elif choice == '3':
        delete_feedback()
    elif choice == '4':
        print("Exiting system.")
        break
    else:
        print("Invalid choice, please try again.\n")
