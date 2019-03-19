import json
import random


class MakeQA(object):

    def __init__(self, words):
        self.words = words
        self.answer()
        self.question()

    def answer(self):
        self.answer_word = random.choice(list(self.words))

    def question(self):
        self.question_phrase = self.words[self.answer_word]


class MakeHint(object):

    def __init__(self, answer_word):
        self.answer_word = answer_word
        self.makehint()

    def makehint(self):
        self.hint_word = self.answer_word


def quiz():

    with open('test.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)

    words = MakeQA(dic)
    hint = MakeHint(words.answer_word)

    def question():
        question_pharase = words.question_phrase
        print('===')
        if type(question_pharase) == list:
            for item in question_pharase:
                print(item)
        print('===')
        print("hint: %s"%hint.hint_word)

    def judge():
        user_answer = input("Enter word: ")
        print("")
        if user_answer == words.answer_word:
            print("You are genius!!!")
        else:
            print("oooooops!")
            print("answer word: %s"%words.answer_word)
        print("")

    question()
    judge()
