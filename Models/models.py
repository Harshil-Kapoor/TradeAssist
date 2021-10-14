class OrderParams:
    def __init__(self, tradingsymbol, symboltoken, transactiontype, price, squareoff, stoploss, quantity, variety, exchange, ordertype, producttype, duration) -> None:
        """ Class defining Order structure\n
            Keyword Arguments:\n
            tradingsymbol -- Symbol to trade\n
            symboltoken -- Token for symbol to trade\n
            transactiontype -- Transaction Type\n
            price -- Price\n
            squareoff -- Square Off\n
            stoploss -- Stoploss\n
            quantity -- Quantity\n
            variety -- Variety\n
            exchange -- Exchange\n
            ordertype -- Order type\n
            producttype -- Product type\n
            duration -- Duration\n
        """
        self.tradingsymbol = tradingsymbol
        self.symboltoken = symboltoken
        self.transactiontype = transactiontype
        self.price = price
        self.squareoff = squareoff
        self.stoploss = stoploss
        self.quantity = quantity
        self.variety = variety
        self.exchange = exchange
        self.ordertype = ordertype
        self.producttype = producttype
        self.duration = duration

    @classmethod
    def fromJson(cls, obj):
        """ Create OrderParams from a json string
            Accepts Structure:\n
            {
                "variety": "NORMAL",
                "tradingsymbol": "SBIN-EQ",
                "symboltoken": "3045",
                "transactiontype": "BUY",
                "exchange": "NSE",
                "ordertype": "LIMIT",
                "producttype": "INTRADAY",
                "duration": "DAY",
                "price": "19500",
                "squareoff": "0",
                "stoploss": "0",
                "quantity": "1"\n
            }
        """
        params = cls('', '', '', '', '')
        params.keys = [
            "tradingsymbol",
            "symboltoken",
            "transactiontype",
            "price",
            "squareoff",
            "stoploss",
            "quantity",
            "variety",
            "exchange",
            "ordertype",
            "producttype",
            "duration"
        ]

        params.quantity = "1"
        params.variety = "NORMAL"
        params.exchange = "NSE"
        params.ordertype = "LIMIT"
        params.producttype = "INTRADAY"
        params.duration = "DAY"
        for k, v in obj.items():
            if k in params.keys:
                setattr(params, k, v)
        return params

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}


class GTTParams:
    def __init__(self, tradingsymbol, symboltoken, exchange, producttype, transactiontype, price, qty, disclosedqty, triggerprice, timeperiod) -> None:
        """ Class defining GTT structure\n
            Keyword Arguments:\n
            tradingsymbol -- Symbol to trade\n
            symboltoken -- Token for symbol to trade\n
            exchange -- Exchange\n
            producttype -- Product type\n
            transactiontype -- Transaction type\n
            price -- Price\n
            qty -- Quantity\n
            disclosedqty -- Disclosed Quantity\n
            triggerprice -- Trigger price\n
            timeperiod -- Time period\n
        """
        self.tradingsymbol = tradingsymbol
        self.symboltoken = symboltoken
        self.exchange = exchange
        self.producttype = producttype
        self.transactiontype = transactiontype
        self.price = price
        self.qty = qty
        self.disclosedqty = disclosedqty
        self.triggerprice = triggerprice
        self.timeperiod = timeperiod

    @classmethod
    def fromJson(cls, obj):
        """ Create GTTParams from a json string
            Accepts Structure:\n
            {
                "tradingsymbol" : "SBIN-EQ",
                "symboltoken" : "3045",
                "exchange" : "NSE",
                "producttype" : "MARGIN",
                "transactiontype" : "BUY",
                "price" : 100000,
                "qty" : 10,
                "disclosedqty": 10,
                "triggerprice" : 200000,
                "timeperiod" : 365\n
            }
        """
        params = cls('', '', '', '', '')
        params.keys = [
            "tradingsymbol",
            "symboltoken",
            "exchange",
            "producttype",
            "transactiontype",
            "price",
            "qty",
            "disclosedqty",
            "triggerprice",
            "timeperiod"
        ]

        params.exchange = "NSE"
        params.producttype = "MARGIN"
        params.transactiontype = "BUY"
        for k, v in obj.items():
            if k in params.keys:
                setattr(params, k, v)
        return params

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}


class HistoryParams:
    def __init__(self, exchange, symboltoken, interval, fromdate, todate) -> None:
        """ Class defining HistoryParams structure\n
            Keyword Arguments:\n
            exchange -- Exchange\n
            symboltoken -- Token for symbol to trade\n
            interval -- Interval\n
            fromdate -- From date\n
            todate -- To date\n
        """
        self.exchange = exchange
        self.symboltoken = symboltoken
        self.interval = interval
        self.fromdate = fromdate
        self.todate = todate

    @classmethod
    def fromJson(cls, obj):
        """ Create HistoryParams from a json string
            Accepts Structure:\n
            {
                "exchange": "NSE",
                "symboltoken": "3045",
                "interval": "ONE_MINUTE",
                "fromdate": "2021-02-08 09:00",
                "todate": "2021-02-08 09:16"\n
            }
        """
        params = cls('', '', '', '', '')
        params.keys = [
            "exchange",
            "symboltoken",
            "interval",
            "fromdate",
            "todate"
        ]

        params.exchange = "NSE"
        params.interval = "ONE_MINUTE"
        for k, v in obj.items():
            if k in params.keys:
                setattr(params, k, v)
        return params

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}


class Candle:
    def __init__(self, obj):
        """ Class defining paramteres for a candle\n
            Accepts Structure:\n
            [
               "2021-02-10T09:15:00+05:30",
               394.05,
               397.7,
               394,
               396.3,
               722616
            ]
        """
        self.keys = [
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
        dict = {k: v for k, v in zip(self.keys, obj)}
        for k, v in dict.items():
            if k in self.keys:
                self.__setattr__(k, v)

        if self.close >= self.open:
            self.color = "green"
        else:
            self.color = "red"

        self.size = abs(self.high - self.low)
        self.body = abs(self.close - self.open)

        self.keys.append("color")
        self.keys.append("size")
        self.keys.append("body")

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

    def get_body_ratio(self):
        return self.body / self.size

    def get_summary(self):
        return f'''Timestamp: {self.timestamp}\n
            Open: {self.open}\n
            High: {self.high}\n
            Low: {self.low}\n
            Close: {self.close}\n
            Volume: {self.volume}'''


class Postion:
    def __init__(self, obj):
        """ Class defining paramteres for a Position\n
            Accepts Structure:\n
            {
               "exchange": "NSE",
               "symboltoken": "2885",
               "producttype": "DELIVERY",
               "tradingsymbol": "RELIANCE-EQ",
               "symbolname": "RELIANCE",
               "instrumenttype": "",
               "priceden": "1",
               "pricenum": "1",
               "genden": "1",
               "gennum": "1",
               "precision": "2",
               "multiplier": "-1",
               "boardlotsize": "1",
               "buyqty": "1",
               "sellqty": "0",
               "buyamount": "2235.80",
               "sellamount": "0",
               "symbolgroup": "EQ",
               "strikeprice": "-1",
               "optiontype": "",
               "expirydate": "",
               "lotsize": "1",
               "cfbuyqty": "0",
               "cfsellqty": "0",
               "cfbuyamount": "0",
               "cfsellamount": "0",
               "buyavgprice": "2235.80",
               "sellavgprice": "0",
               "avgnetprice": "2235.80",
               "netvalue": "- 2235.80",
               "netqty": "1",
               "totalbuyvalue": "2235.80",
               "totalsellvalue": "0",
               "cfbuyavgprice": "0",
               "cfsellavgprice": "0",
               "totalbuyavgprice": "2235.80",
               "totalsellavgprice": "0",
               "netprice": "2235.80"
            }
        """
        self.keys = [
            "exchange",
            "symboltoken",
            "tradingsymbol",
            "instrumenttype",
            "buyqty",
            "sellqty",
            "strikeprice",
            "lotsize",
            "buyavgprice",
            "sellavgprice",
            "avgnetprice",
            "netvalue",
            "netqty",
            "totalbuyvalue",
            "totalsellvalue",
            "totalbuyavgprice",
            "totalsellavgprice",
            "netprice"
        ]

        dict = {k: v for k, v in zip(self.keys, obj)}
        for k, v in dict.items():
            if k in self.keys:
                self.__setattr__(k, v)

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

    def get_summary(self):
        if self.position == "BUY":
            return f'''Symbol: {self.tradingsymbol}
                Avg. Buy Price: {self.buyavgprice}\n
                Current Price: {self.current}\n
                Quantity: {self.buyqty}\n
                Net Price: {self.netprice}\n
                P&L: {self.pl}\n
                Net Change: {self.netchange}'''
        else:
            return f'''Symbol: {self.tradingsymbol}
                Avg. Sell Price: {self.sellavgprice}\n
                Current Price: {self.current}\n
                Quantity: {self.sellqty}\n
                Net Price: {self.netprice}\n
                Net Change: {self.netchange}'''

    def set_position_properties(self, current_val_delegate):
        self.current = current_val_delegate(self)
        self.pl = self.current - self.netvalue
        self.netchange = self.pl / self.avgnetprice
        self.position = "BUY" if self.totalbuyvalue != 0 else "SELL"

        self.keys.append("current")
        self.keys.append("pl")
        self.keys.append("netchange")
        self.keys.append("position")


class Holding:
    def __init__(self, obj):
        """ Class defining paramteres for a Holding\n
            Accepts Structure:\n
            {
                "tradingSymbol":"RELIANCE-EQ",
                "exchange":"NSE",
                "isin":"0INE002A01018",
                "t1quantity":"0",
                "realisedquantity":"0",
                "quantity":"0",
                "authorisedquantity":"0",
                "profitandloss":"0",
                "product":"DELIVERY",
                "collateralquantity":"0",
                "collateraltype":"null",
                "haircut":"0",
            }
        """
        self.keys = [
            "tradingSymbol",
            "exchange",
            "isin",
            "t1quantity",
            "realisedquantity",
            "quantity",
            "authorisedquantity",
            "profitandloss",
            "product",
            "collateralquantity",
            "collateraltype",
            "haircut"
        ]

        dict = {k: v for k, v in zip(self.keys, obj)}
        for k, v in dict.items():
            if k in self.keys:
                self.__setattr__(k, v)

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

    def get_summary(self):
        return f'''Symbol: {self.tradingsymbol}
            Quantity: {self.quantity}\n
            P&L: {self.profitandloss}'''


class MovementAnalysisParams:
    def __init__(self, exchange, symbolToken, interval, delta, body_ratio_threshold):
        """ Class defining response for Movement analysis strategy\n
            Keyword Arguments:\n
            exchange -- Stock echange, defaults to NSE\n
            symbolToken -- Symbol Token to perform movement analysis for\n
            interval -- Interval for candles, defaults to 1 day\n
            delta -- Number of candles for analysis, defaults to 3 candles\n
            body_ratio_threshold -- Threshold for Body ratio, defaults to 0.5\n
        """
        self.keys = [
            "exchange",
            "symbolToken",
            "interval",
            "delta",
            "body_ratio_threshold"
        ]

        self.exchange = exchange or "NSE"
        self.symbolToken = symbolToken
        self.interval = interval or "1d"
        self.delta = delta or "3"
        self.body_ratio_threshold = body_ratio_threshold or "0.5"

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}


class MovementAnalysisResponse:
    def __init__(self, analysis, short_candle_flag, long_candle_flag, monotonically_increasing, monotonically_dereasing, swing_flag, candles):
        """ Class defining response for Movement analysis strategy\n
            Keyword Arguments:\n
            analysis -- Final analysis: INCONCLUSIVE, SHORT or LONG\n
            short_candle_flag -- Flag indicating movement deteceted for entering short position\n
            long_candle_flag -- Flag indicating movement deteceted for entering short position\n
            monotonically_increasing -- Flag indicating the candles have monotonically increasing sizes\n
            monotonically_dereasing -- Flag indicating the candles have monotonically decreasing sizes\n
            swing_flag -- Flag indicating detection of a swing\n
            candles -- List of Candles\n
        """
        self.keys = [
            "analysis",
            "short_candle_flag",
            "long_candle_flag",
            "monotonically_increasing",
            "monotonically_dereasing",
            "swing_flag",
            "candles"
        ]

        self.analysis = analysis
        self.short_candle_flag = short_candle_flag
        self.long_candle_flag = long_candle_flag
        self.monotonically_increasing = monotonically_increasing
        self.monotonically_dereasing = monotonically_dereasing
        self.swing_flag = swing_flag
        self.candles = candles

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

    def get_summary(self):
        return f'''Analyis: {self.analysis}
        short_candle_flag: {self.short_candle_flag}\n
        long_candle_flag: {self.long_candle_flag}\n
        monotonically_increasing: {self.monotonically_increasing}\n
        monotonically_dereasing: {self.monotonically_dereasing}\n
        swing_flag: {self.swing_flag}'''
