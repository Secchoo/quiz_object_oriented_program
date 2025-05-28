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
