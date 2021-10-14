from datetime import datetime, timedelta
from typing import List

from smartapi.smartConnect import SmartConnect
from Models.models import Candle, HistoryParams, Holding, MovementAnalysisParams, MovementAnalysisResponse, Postion
from Utils.SmartAPI import get_history

intervals = {
    '1m': 'ONE_MINUTE',
    '3m': 'THREE_MINUTE',
    '5m': 'FIVE_MINUTE',
    '10m': 'TEN_MINUTE',
    '15m': 'FIFTEEN_MINUTE',
    '30m': 'THIRTY_MINUTE',
    '1h': 'ONE_HOUR',
    '1d': 'ONE_DAY'
}


def get_candles(candleData: List[List]) -> List[Candle]:
    return [Candle(candle) for candle in candleData]


def format_positions(positions: dict) -> List[Postion]:
    return [Postion(position) for position in positions]


def format_holdings(holdings: dict) -> List[Holding]:
    return [Holding(holding) for holding in holdings]


def get_interval(interval: str) -> str:
    return intervals[interval]


def get_formatted_date(date: str) -> str:
    return datetime.strptime(date, '%Y/%m/%d-%H:%M').strftime("%Y-%m-%d %H:%M")


def analyze_movement(connection: SmartConnect, params: MovementAnalysisParams) -> MovementAnalysisResponse:
    try:
        today = datetime.now()
        before = datetime.now() - timedelta(days=int(params.delta))
        history = get_history(connection, HistoryParams({
            "exchange": params.exchange,
            "symboltoken": params.symboltoken,
            "interval": params.interval,
            "fromdate": before.strftime("%Y-%m-%d %H:%M"),
            "todate": today.strftime("%Y-%m-%d %H:%M")
        }))
    except Exception as e:
        return {"message": f"An error occurred while getting historic data: {e}."}, 500
    
    candles: List[Candle] = get_candles(history["data"])
    candle_sizes = [candle.size for candle in candles]

    short_candle_flag: bool = candles[0].color == "green" and candles[1].color == "green" and candles[2].color == "red"
    long_candle_flag: bool = candles[0].color == "red" and candles[1].color == "red" and candles[2].color == "green"
    monotonically_increasing = all(x < y for x, y in zip(candle_sizes, candle_sizes[1:]))
    monotonically_dereasing = all(x > y for x, y in zip(candle_sizes, candle_sizes[1:]))
    body_proportion_flag = all([candle.get_body_ratio() >= params.body_ratio_threshold for candle in candles])
    swing_flag = candles[1].close >= candles[0].close and candles[1].close >= candles[2].close

    analysis = "INCONCLUSIVE"
    if monotonically_increasing and body_proportion_flag and swing_flag:
        if short_candle_flag:
            analysis = "SHORT"
        elif long_candle_flag:
            analysis = "LONG"
    
    return MovementAnalysisResponse(analysis, short_candle_flag, long_candle_flag, monotonically_increasing, monotonically_dereasing, swing_flag, candles)
