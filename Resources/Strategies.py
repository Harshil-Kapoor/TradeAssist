from Utils.Utils import get_candles
from datetime import datetime, timedelta
from typing import List
from flask.json import jsonify
from flask_restful import Resource, reqparse
from Models.models import Candle, HistoryParams
from Utils.SmartAPI import get_connection, get_history

parser = reqparse.RequestParser()
parser.add_argument('symbolToken', type=str)
parser.add_argument('delta', type=int, default=3, required=False)
parser.add_argument('body_ratio_threshold', type=float, default=0.45, required=False)

class MovementAnalysis(Resource):
    def get(self):
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
        try:
            args = parser.parse_args()
            symbolToken = args['symbolToken']
            delta = args['delta']
            body_ratio_threshold = args['body_ratio_threshold']

            connection, data = get_connection()
            today = datetime.now()
            before = datetime.now() - timedelta(days=delta)
            history = get_history(connection, HistoryParams({
                "exchange": "NSE",
                "symboltoken": symbolToken,
                "interval": "ONE_DAY",
                "fromdate": today.strftime("%Y-%m-%d %H:%M"),
                "todate": before.strftime("%Y-%m-%d %H:%M")
            }))
        except:
            return {"message": "An error occurred while getting historic data."}, 500
        
        candles: List[Candle] = get_candles(history["data"])
        candle_sizes = [candle.size for candle in candles]

        short_candle_flag: bool = candles[0].color == "green" and candles[1].color == "green" and candles[2].color == "red"
        long_candle_flag: bool = candles[0].color == "red" and candles[1].color == "red" and candles[2].color == "green"
        monotonically_increasing = all(x < y for x, y in zip(candle_sizes, candle_sizes[1:]))
        monotonically_dereasing = all(x > y for x, y in zip(candle_sizes, candle_sizes[1:]))
        body_proportion_flag = all([candle.get_body_ratio() >= body_ratio_threshold for candle in candles])
        swing_flag = candles[1].close >= candles[0].close and candles[1].close >= candles[2].close

        if monotonically_increasing and body_proportion_flag and swing_flag:
            if short_candle_flag:
                analysis = "SHORT"
            elif long_candle_flag:
                analysis = "LONG"

        response = {
            "candles": candles.__dict__,
            "short_candle_flag": short_candle_flag,
            "long_candle_flag": long_candle_flag,
            "monotonically_increasing": monotonically_increasing,
            "monotonically_dereasing": monotonically_dereasing,
            "swing_flag": swing_flag,
            "analysis": analysis
        }

        return jsonify(response)
