from flask import Blueprint

from flask_restx import Api, Resource
from typing import Dict, List
from database.userservice import register_user_db
from api import swagger_api as registration_api
registration_bp = Blueprint('registration', __name__)
# registration_api = Api(registration_bp)


# Запрос на регистрацию
@registration_api.route('/register/<string:name>/<string:number>', methods=['POST'])
class RegisterUser(Resource):
    def post(self, name: str, number: str) -> Dict[str, int]:
        user_id = register_user_db(name, number)

        return {'status': 1, 'user_id': user_id}


















