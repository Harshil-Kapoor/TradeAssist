from flask import request
from flask.json import jsonify
from flask_restful import Resource
from Models.models import GTTParams, OrderParams
from Utils.SmartAPI import create_gtt, get_connection, get_gtt_list, place_order

class PlaceOrder(Resource):
    def post(self):
        try:
            order_id = place_order(get_connection(), OrderParams(request.get_json()))
        except Exception as e:
            return {"message": f"An error occurred while placing order: {e}."}, 500

        return jsonify(order_id)

class CreateGTT(Resource):
    def post(self):
        try:
            gtt_id = create_gtt(get_connection(), GTTParams(request.get_json()))
        except Exception as e:
            return {"message": f"An error occurred while getting historic data: {e}."}, 500

        return jsonify(gtt_id)

class GetGTTList(Resource):
    def get(self):
        try:
            gtt_list = get_gtt_list(get_connection())
        except Exception as e:
            return {"message": f"An error occurred while getting historic data: {e}."}, 500

        return jsonify(gtt_list)
