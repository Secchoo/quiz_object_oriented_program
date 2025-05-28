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

    def main(self):
        #Main function to run the quiz creator.
        print("Welcome to Quiz Creator!")
        print("Add questions to your quiz. Press Ctrl+C to finish.")
        try:
            while True:
                self.display_menu()
                choice = input("\nEnter your choice (1-5): ").strip()
                if choice == '1':
                    question = self.questions_getter()
                    answers = self.choices()
                    correct_answer_value = self.correct_answer(answers)
                    self.quiz_question_saver(question, answers, correct_answer_value)
                    print("\nQuestion added successfully!")
                elif choice == '2':
                    if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                        with open(self.filename, 'r') as file:
                            print("\n=== Available Questions ===")
                            print(file.read())
                    else:
                        print("\nNo questions available!")
                elif choice == '3':
                    self.edit_questions()
                elif choice == '4':
                    self.delete_questions()
                elif choice == '5':
                    print("\nQuiz creation completed!")
                    print(f"All questions have been saved to {self.filename}")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print("\n\nQuiz creation completed!")
            print(f"All questions have been saved to {self.filename}")