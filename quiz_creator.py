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

    def edit_questions(self):
        #Edit existing questions in the quiz.
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            print("\nNo questions available to edit!")
            return

        with open(self.filename, 'r') as file:
            lines = file.readlines()

        questions = []
        current_question = []

        for line in lines:
            if line.strip() == "":
                if current_question:
                    questions.append(current_question)
                    current_question = []
            else:
                current_question.append(line)
        if current_question:
            questions.append(current_question)

        print("\n=== Edit Questions ===")
        for i, question in enumerate(questions, start=1):
            print(f"{i}. {question[0].strip()}")

        try:
            choice = int(input("\nEnter the number of the question to edit: ").strip())
            if 1 <= choice <= len(questions):
                selected_question = questions[choice - 1]
                print("\nEditing question:")
                print("".join(selected_question))

                new_question = self.questions_getter()
                new_answers = self.choices()
                new_correct_answer = self.correct_answer(new_answers)

                updated_question = [f"Question: {new_question}\n"]
                letters = ['a', 'b', 'c', 'd']
                for letter, answer in zip(letters, new_answers):
                    updated_question.append(f"{letter}. {answer}\n")
                updated_question.append(f"Correct answer: {new_correct_answer}\n\n")

                questions[choice - 1] = updated_question

                with open(self.filename, 'w') as file:
                    for question in questions:
                        file.writelines(question)

                print("\nQuestion updated successfully!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")