from flask.json import jsonify
from flask_restful import Resource
from flask import request
from Models.models import HistoryParams
from Utils.SmartAPI import get_connection, get_history


class GetHistory(Resource):
    def post(self):
        """ Endpoint for getting history\n
            Accepts Input:\n
            {
                "exchange": "NSE",
                "symboltoken": "3045",
                "interval": "ONE_MINUTE",
                "fromdate": "2021-02-08 09:00", 
                "todate": "2021-02-08 09:16"\n
            }
        """
        try:
            connection, data = get_connection()
            history = get_history(connection, HistoryParams(request.get_json()))
        except Exception as e:
            return {"message": f"An error occurred while getting historic data: {e}."}, 500

        return jsonify(history)