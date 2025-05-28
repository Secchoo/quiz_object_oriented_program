from quiz_creator import QuizCreator
from quiz_taker import QuizTaker
import random

def main():
    #Main entry point for the quiz application.
    print("Welcome to the Quiz Application!")
    print("1. Create a Quiz")
    print("2. Take a Quiz")
    choice = input("Select an option (1 or 2): ").strip()

    if choice == '1':
        quiz_creator = QuizCreator()
        quiz_creator.main()  # Run the quiz creator
    elif choice == '2':
        quiz_taker = QuizTaker()
        quiz_taker.main(random)  # Pass random as argument
    else:
        print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
