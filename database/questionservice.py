from database.models import Question, db

import random


# Получить вопросы
def get_questions_db(level):
    # Если level не указан
    if level == 'all':
        questions = []
        # Получаем все вопросы из базы
        all_questions = Question.query.all()

        # 20 рандомных вопросов
        for i in range(20):
            questions.append(random.choice(all_questions))

        return questions

    # если указал сложность, то фильтр по вопросам
    questions_from_level = Question.query.filter_by(level=level).all()
    questions = [random.choice(questions_from_level) for i in range(20)]

    return questions


# Проверка ответа пользователя
def check_user_answer_db(question_id, user_answer):
    current_question = Question.query.get(question_id)

    # проверка ответа пользователя с реальным ответом в базе
    if current_question.correct_answer == user_answer:
        return True

    return False


# Добавление вопросов в базу (ДЗ)

















