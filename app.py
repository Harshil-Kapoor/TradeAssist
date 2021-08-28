from flask import Flask
from flask_restful import Api
from Utils.SmartAPI import get_connection
from Resources.Account import GetHolding, GetPosition, GetProfile
from Resources.History import GetHistory


app = Flask(__name__)
api = Api(app)

connection, data = get_connection()

api.add_resource(GetHistory(connection), '/getHistory')
api.add_resource(GetPosition(connection), '/getPosition')
api.add_resource(GetHolding(connection), '/getHolding')
api.add_resource(GetProfile(connection, data), '/getPosition')
api.add_resource(GetHolding(connection), '/getHolding')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
