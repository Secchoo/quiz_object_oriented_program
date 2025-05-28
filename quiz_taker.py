from quiz import Quiz
from colorama import Fore, Style

class QuizTaker(Quiz):
    #Class to run the quiz program.
    
    def __init__(self, filename="quiz_record.txt"):
        super().__init__(filename)

    def main(self, random):
        #Main quiz program execution.
        total_questions = len(self.questions)
        if total_questions == 0:
            print(Fore.RED + Style.BRIGHT + "\n😞 No questions found in the quiz file!")
            return
        
        random.shuffle(self.questions)
        score = 0

        for index, question in enumerate(self.questions, 1):
            shuffled_options = self.present_question(question, index, total_questions)
            user_choice = self.get_user_choice()
            
            selected_option = shuffled_options[ord(user_choice) - ord('A')]
            score += question.is_correct(selected_option)
            
            input(Fore.WHITE + Style.BRIGHT + "\nPress Enter to continue...")

        self.show_final_results(score, total_questions)

    def get_user_choice(self):
        #Get and validate user's answer choice.
        while True:
            choice = input(Fore.GREEN + Style.BRIGHT + 
                           "\n✏️  Your answer (A-D): ").upper()
            if choice in {'A', 'B', 'C', 'D'}:
                return choice
            print(Fore.RED + Style.BRIGHT + "⚠️  Invalid choice! Please enter A, B, C, or D")

__all__ = ["QuizTaker"]
