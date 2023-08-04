from flask import Blueprint

from typing import Dict, List
from database.statservice import get_rating_db
from flask_restx import Api, Resource
from api import swagger_api as leaders_api

leaders_bp = Blueprint('leaders', __name__)
# leaders_api = Api(leaders_bp)


# Запрос на получение top 5 участников
@leaders_api.route('/leaders/<string:level>')
class GetTopFive(Resource):
    def get(self, level: str = 'all') -> Dict[str, List[Dict[int, int]]]:
        top_5_users = get_rating_db(level)

        return {'level': level, 'leaders': top_5_users}

