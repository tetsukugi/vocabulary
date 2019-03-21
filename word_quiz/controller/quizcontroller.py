from word_quiz.controller import load_jsondata
from word_quiz.models import quizmodel


def start_quiz():

    data_loader = load_jsondata.LoadJsonData()
    data = data_loader.load_json_data()

    for i in range(3):
        quiz = quizmodel.Quiz(data, i)
        user_answer = quiz.ask_a_question()
        quiz.judge(user_answer)
