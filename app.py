from Resources.Strategies import MovementAnalysis
from Resources.Order import CreateGTT, GetGTTList, PlaceOrder
from flask import Flask
from flask_restful import Api
from Resources.Account import GetHolding, GetPosition, GetProfile
from Resources.History import GetHistory
import os


app = Flask(__name__)
api = Api(app)

api.add_resource(GetHistory, '/getHistory')
api.add_resource(GetPosition, '/getPosition')
api.add_resource(GetHolding, '/getHolding')
api.add_resource(GetProfile, '/getPosition')
api.add_resource(PlaceOrder, '/placeOrder')
api.add_resource(CreateGTT, '/createGTT')
api.add_resource(GetGTTList, '/getGTTList')
api.add_resource(MovementAnalysis, '/analyseMovement')

if __name__ == '__main__':
    if os.environ["ANGEL_ENV"] == "PRODUCTION":
        app.run(debug=True)
    else:
        app.run(port=5001, debug=True)
