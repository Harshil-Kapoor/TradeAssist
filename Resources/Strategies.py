from Utils.Utils import analyze_movement
from flask.json import jsonify
from flask_restful import Resource, reqparse
from Models.models import MovementAnalysisParams, MovementAnalysisResponse
from Utils.SmartAPI import get_connection

parser = reqparse.RequestParser()
parser.add_argument('exchange', type=str, required=False)
parser.add_argument('symbolToken', type=str, required=True)
parser.add_argument('interval', type=str, default="ONE_DAY", required=False)
parser.add_argument('frequency', type=int, default=3, required=False)
parser.add_argument('body_ratio_threshold', type=float, default=0.45, required=False)


class MovementAnalysis(Resource):
    def post(self):
        """ Endpoint for Movement Analysis\n
            Accepts Input:\n
            {
                "tradingsymbol" : "SBIN-EQ",
                "exchange": "NSE",
                "symboltoken": "3045",
                "interval": "ONE_MINUTE",
                "frequency": "3"\n
            }
        """
        args = parser.parse_args()
        exchange = args['exchange']
        symbolToken = args['symbolToken']
        interval = args['interval']
        delta = args['frequency']
        body_ratio_threshold = args['body_ratio_threshold']

        connection, data = get_connection()
        result: MovementAnalysisResponse = analyze_movement(connection, MovementAnalysisParams(exchange, symbolToken, interval, delta, body_ratio_threshold))

        return jsonify(result.get_dict())
