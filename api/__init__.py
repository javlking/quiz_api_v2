from flask_restx import Api
from flask import Blueprint

swagger_bp = Blueprint('swagger', __name__, url_prefix='/docs')
swagger_api = Api(swagger_bp)

from api import registration, test_process