from typing import List
from Models.models import Candle, Holding, Postion


def get_candles(candleData: List[List]) -> List[Candle]:
    return [Candle(candle) for candle in candleData]


def format_positions(positions: dict) -> List[Postion]:
    return [Postion(position) for position in positions]


def format_holdings(holdings: dict) -> List[Holding]:
    return [Holding(holding) for holding in holdings]
