import json
from typing import List
from Models.models import Candle, Holding, Postion


def get_candles(candleData: List[List]) -> List[Candle]:
    return [Candle(candle) for candle in candleData]


def format_positions(positions: bytes) -> List[Postion]:
    return [Postion(position) for position in json.loads(positions.decode('utf-8'))["data"]]


def format_holdings(holdings: bytes) -> List[Holding]:
    return [Holding(holding) for holding in json.loads(holdings.decode('utf-8'))["data"]]
