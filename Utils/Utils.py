from typing import List
from Models.models import Candle, Holding, Postion


def get_candles(candleData: List[List]) -> List[Candle]:
    return [Candle(candle) for candle in candleData]


def format_positions(positions: bytes) -> List[Postion]:
    return [Postion(position) for position in positions["data"]]


def format_holdings(holdings: bytes) -> List[Holding]:
    return [Holding(holding) for holding in holdings["data"]]
