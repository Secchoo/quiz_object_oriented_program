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