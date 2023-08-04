from database.models import Question, db, UserAnswers

import random


# Получить вопросы
def get_questions_db(level='all'):
    # Если level не указан
    if level == 'all':
        questions = []
        # Получаем все вопросы из базы
        all_questions = Question.query.all()

        # 20 рандомных вопросов
        # for i in range(20):
        #     questions.append(random.choice(all_questions))

        return all_questions

    # если указал сложность, то фильтр по вопросам
    questions_from_level = Question.query.filter_by(level=level).all()
    questions = [random.choice(questions_from_level) for i in range(20)]

    return questions


# Проверка ответа пользователя
def check_user_answer_db(user_id, question_id, user_answer):
    current_question = UserAnswers(user_id=user_id, q_id=question_id, user_answer=user_answer)

    db.session.add(current_question)
    db.session.commit()

    return True


# Добавление вопросов в базу (ДЗ)
def add_question_db(question_text):
    new_question = Question(main_question=question_text, correct_answer='some')

    db.session.add(new_question)
    db.session.commit()

    return True

















