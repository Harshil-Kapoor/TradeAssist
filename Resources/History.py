from flask.json import jsonify
from flask_restful import Resource
from flask import request
from smartapi.smartConnect import SmartConnect
from Models.models import HistoryParams
from Utils.SmartAPI import get_history

class GetHistory(Resource):
    def __init__(self, connection: SmartConnect) -> None:
        self.connection = connection
    def post(self):
        try:
            history = get_history(self.connection, HistoryParams(request.get_json()))
        except:
            return {"message": "An error occurred while getting historic data."}, 500

        return jsonify(history)