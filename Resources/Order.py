from flask import request
from flask.json import jsonify
from flask_restful import Resource
from Models.models import GTTParams, OrderParams
from Utils.SmartAPI import create_gtt, get_connection, get_gtt_list, place_order

class PlaceOrder(Resource):
    def post(self):
        """ Endpoint for placing an order\n
            Accepts Input:\n
            {
                "variety": "NORMAL",
                "tradingsymbol": "SBIN-EQ",
                "symboltoken": "3045",
                "transactiontype": "BUY",
                "exchange": "NSE",
                "ordertype": "LIMIT",
                "producttype": "INTRADAY",
                "duration": "DAY",
                "price": "19500",
                "squareoff": "0",
                "stoploss": "0",
                "quantity": "1"\n
            }
        """
        try:
            connection, data = get_connection()
            order_id = place_order(connection, OrderParams(request.get_json()))
        except Exception as e:
            return {"message": f"An error occurred while placing order: {e}."}, 500

        return jsonify(order_id)

class CreateGTT(Resource):
    def post(self):
        """ Endpoint for creating a Good To Go Trigger (GTT)\n
            Accepts Input:\n
            {
                "tradingsymbol" : "SBIN-EQ",
                "symboltoken" : "3045",
                "exchange" : "NSE", 
                "producttype" : "MARGIN",
                "transactiontype" : "BUY",
                "price" : 100000,
                "qty" : 10,
                "disclosedqty": 10,
                "triggerprice" : 200000,
                "timeperiod" : 365\n
            }
        """
        try:
            connection, data = get_connection()
            gtt_id = create_gtt(connection, GTTParams(request.get_json()))
        except Exception as e:
            return {"message": f"An error occurred while getting historic data: {e}."}, 500

        return jsonify(gtt_id)

class GetGTTList(Resource):
    def get(self):
        """ Endpoint for getting list of GTTs created\n
            Keyword Arguments:\n
            connection -- SmartConnect object
        """
        try:
            connection, data = get_connection()
            gtt_list = get_gtt_list(connection)
        except Exception as e:
            return {"message": f"An error occurred while getting historic data: {e}."}, 500

        return jsonify(gtt_list)
