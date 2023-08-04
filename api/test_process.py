from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from api import swagger_api as test_api
from typing import Dict, List, Optional
from pydantic import BaseModel
from database.questionservice import get_questions_db, check_user_answer_db, add_question_db
from database.statservice import get_user_position

test_bp = Blueprint('test_process', __name__)
# test_api = Api(test_bp)
question_model = test_api.model('add_question', {'main_text': fields.String})


# Валидатор вопросов
class Questions(BaseModel):
    # timer: int
    questions: List[Dict]


# Запрос на получение всех вопросов
@test_api.route('/get-questions')
class GetUserQuestions(Resource):
    def get(self) -> Questions.json:
        # Обращение к базе вопросов
        questions = get_questions_db()

        if questions:
            result = []
            timer = 0

            # пройдемся по каждому вопросу
            for question in questions:
                # generated_question = {'question_text': question.main_question}
                result.append({'question_id': question.id, 'question_text': question.main_question})
                # timer = question.timer

            return Questions(**{'questions': result}).json()

        return Questions(questions=[]).json()


# Запрос на проверку ответа от пользователя
@test_api.route('/set-answer/<int:question_id>/<int:user_answer>/<int:user_id>', methods=['POST'])
class CheckCurrentAnswer(Resource):
    def post(self, question_id: int, user_answer: str, user_id: int) -> Dict[str, int]:
        result = check_user_answer_db(user_id, question_id, user_answer)

        return {'status': 1 if result else 0}


# Запрос на вывод результата
# @test_api.route('/done/<int:user_id>/<int:correct_answers>/<string:level>', methods=['POST'])
# class UserDoneTest(Resource):
#     def post(self, user_id: int, correct_answers: int, level: str) -> Dict[str, int]:
#         user_position = get_user_position(user_id, level, correct_answers)
#
#         return {'status': 1, 'correct_answers': correct_answers, 'position_on_top': user_position}


# Запрос на проверку ответа от пользователя
@test_api.route('/add-question', methods=['POST'])
class CheckCurrentAnswer(Resource):
    @test_api.expect(question_model)
    def post(self):
        data = request.json
        main_text = data.get('main_text')
        result = add_question_db(main_text)

        return {'status': 1 if result else 0}
