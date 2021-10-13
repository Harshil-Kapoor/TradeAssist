from datetime import datetime
from typing import List
from Models.models import Candle, Holding, Postion

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
