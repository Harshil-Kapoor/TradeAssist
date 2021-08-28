from flask.json import jsonify
from flask_restful import Resource
from Utils.SmartAPI import get_connection, get_position, get_holding, get_user_profile

class GetPosition(Resource):
    def get(self):
        """ Endpoint for getting current positions"""
        try:
            connection, data = get_connection()
            positions = get_position(connection)
        except:
            return {"message": "An error occurred while getting current positions."}, 500

        return jsonify(positions)

class GetHolding(Resource):
    def get(self):
        """ Endpoint for getting current holdings"""
        try:
            connection, data = get_connection()
            holdings = get_holding(connection)
        except:
            return {"message": "An error occurred while getting current holdings."}, 500

        return jsonify(holdings)

class GetProfile(Resource):
    def get(self):
        """ Endpoint for getting current user profile"""
        try:
            connection, data = get_connection()
            profile = get_user_profile(connection, data)
        except:
            return {"message": "An error occurred while getting user profile."}, 500

        return jsonify(profile)
