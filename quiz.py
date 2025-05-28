import os
import random
from colorama import Fore, Style


class Question:


    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
    
    def is_correct(self, answer):
        #checks if the answer is correct
        return answer == self.correct_answer
    

class Quiz:
    #Base class to manage quiz functionality

    def __init__(self, filename="quiz_record.txt"):
        seld.filename = filename
        self.questions = self.load_questions()

    def load_questions(self):
        #loads questions from a file
        questions = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                current_question = {}
                collecting_options = False

                for line in file:
                    line = line.strip()
                    if line.startswith("Question:"):
                        current_question = {
                            'text': line[10:],
                            'options': [],
                            'correct': None
                        }
                        collecting_options = True
                    elif line.startswith(('a. ', 'b. ', 'c. ', 'd. ')) and collecting_options:
                        current_question['options'].append(line[3:])
                    elif line.startswith("Correct answer: "):
                        correct_letter = line[16:].lower()
                        current_question['correct'] = current_question['options'][
                            ord(correct_letter) - ord('a')]
                        questions.append(Question(current_question['text'], current_question['options'], current_question['correct']))
                        collecting_options = False

        except FileNotFoundError:
            print(Fore.RED + "Quiz file not found. Please ensure the file exists.")
            exit(1)
        
        return questions
    
