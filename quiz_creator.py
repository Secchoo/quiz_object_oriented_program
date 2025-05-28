import os
from quiz import Quiz
from colorama import Fore


class QuizCreator(Quiz):
    #class to manage the quiz creation process

    def __init__(self, filename="quiz_record.txt"):
        super().__init__(filename)
    
    def questions_getter(self):
        #getter for questions
        while True:
            question = input("\n Enter your question: ")
            if question:
                return question
            print(Fore.RED + "Question cannot be empty. Please try again.")
            
    def choices(self):
        #get four choices from the user
        letters = ['a', 'b', 'c', 'd']
        answers = []

        for letter in letters:
            while True:
                answer = input(f"\nEnter answer ({letter}): ").strip()
                if answer:
                    answers.append(answer)
                    break
                print("Answer cannot be empty!")
        return answers 

    def correct_answer(self, answers):
        #Get the correct answer from the user.
        letters = ['a', 'b', 'c', 'd']
        while True:
            print("\nSelect the correct answer:")
            for letter, answer in zip(letters, answers):
                print(f"{letter}. {answer}")
            choice = input("Enter the letter of the correct answer: ").lower().strip()
            if choice in letters:
                return choice
            print("Invalid choice! Please enter a, b, c, or d.")

    def quiz_question_saver(self, question, answers, correct_answer):
        #Save the quiz data to a text file.
        with open(self.filename, 'a') as file:
            file.write(f"Question: {question}\n")
            letters = ['a', 'b', 'c', 'd']
            for letter, answer in zip(letters, answers):
                file.write(f"{letter}. {answer}\n")
            file.write(f"Correct answer: {correct_answer}\n\n")

    def display_menu(self):
        """Display the main menu with colors and emojis."""
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        RESET = '\033[0m'
        print(f"\n{CYAN}=== 🎉 Quiz Creator Menu 🎉 ==={RESET}")
        print(f"{GREEN}1️⃣  ➕ Add Question{RESET}")
        print(f"{YELLOW}2️⃣  👁️  View Questions{RESET}")
        print(f"{CYAN}3️⃣  ✏️  Edit Question{RESET}")
        print(f"{RED}4️⃣  🗑️  Delete Question{RESET}")
        print(f"{GREEN}5️⃣  ✅ Exit{RESET}")