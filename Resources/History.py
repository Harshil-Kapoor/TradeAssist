from flask.json import jsonify
from flask_restful import Resource
from flask import request
from Models.models import HistoryParams
from Utils.SmartAPI import get_connection, get_history

class GetHistory(Resource):
    def post(self):
        """ Endpoint for getting history\n
            Keyword Arguments:\n
            connection -- SmartConnect object
        """
        try:
            connection, data = get_connection()
            history = get_history(connection, HistoryParams(request.get_json()))
        except:
            return {"message": "An error occurred while getting historic data."}, 500

        return jsonify(history)