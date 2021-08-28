from flask.json import jsonify
from smartapi import SmartConnect
from flask_restful import Resource
from Utils.SmartAPI import get_position, get_holding, get_user_profile

class GetPosition(Resource):
    def __init__(self, connection: SmartConnect) -> None:
        """ Get the current positions\n
            Keyword Arguments:\n
            connection -- SmartConnect object
        """
        self.connection = connection
    def get(self):
        try:
            positions = get_position(self.connection)
        except:
            return {"message": "An error occurred while getting current positions."}, 500

        return jsonify(positions)

class GetHolding(Resource):
    def __init__(self, connection: SmartConnect) -> None:
        """ Get the current holdingss\n
            Keyword Arguments:\n
            connection -- SmartConnect object
        """
        self.connection = connection
    def get(self):
        try:
            holdings = get_holding(self.connection)
        except:
            return {"message": "An error occurred while getting current holdings."}, 500

        return jsonify(holdings)

class GetProfile(Resource):
    def __init__(self, connection: SmartConnect, data: bytes) -> None:
        """ Get the current user profile\n
            Keyword Arguments:\n
            connection -- SmartConnect object
            data -- bytes
        """
        self.connection = connection
        self.data = data
    def get(self):
        try:
            profile = get_user_profile(self.connection, self.data)
        except:
            return {"message": "An error occurred while getting user profile."}, 500

        return jsonify(profile)
