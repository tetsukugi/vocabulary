import random
import re


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
        self.hint = self.answer_word
        first_space = self.hint.find(' ')
        if first_space == -1:
            h1 = self.hint[:1]
            h2 = self.hint[1:]
            h3 = re.sub(r'[a-z]', '*', h2)
            self.hint = h1 + h3
            return self.hint
        else:
            h1 = self.hint[:first_space]
            h2 = h1[:1]
            h3 = h1[1:]
            h4 = re.sub(r'[a-z]', '*', h3)
            h5 = h2 + h4
            h6 = self.hint[first_space:]
            self.hint = h5 + h6
            return self.hint



class Quiz(object):

    def __init__(self, data, times):
        self.data = data
        self.times = times
        self.quiz_header(self.times)
        self.words = MakeQA(self.data)
        self.answer = self.words.answer_word
        self.question = self.words.question_phrase
        self.make_hint = MakeHint(self.answer)
        self.hint = self.make_hint.hint


    def quiz_header(self, times):
        print("== question%s =="%times)
        print()

    def ask_a_question(self):
        question_pharase = self.question
        print('---')
        if type(question_pharase) == list:
            for item in question_pharase:
                print(item)
        print('---')
        print("hint: %s"%self.hint)
        user_answer = input("Enter word: ")
        return user_answer


    def judge(self, user_answer):
        print("")
        if user_answer == self.answer:
            print("You are genius!!!")
        else:
            print("oooooops!")
            print("answer word: %s"%self.answer)
        print("")
 