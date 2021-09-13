from Utils.SmartAPI import get_connection, get_current_value

class OrderParams:
    def __init__(self, obj):
        """ Class defining Order structure\n
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
        self.keys = ["tradingsymbol",
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

        self.quantity = "1"
        self.variety = "NORMAL"
        self.exchange = "NSE"
        self.ordertype = "LIMIT"
        self.producttype = "INTRADAY"
        self.duration = "DAY"
        for k, v in obj.items():
            if k in self.keys:
                self.__setattr__(k, v)
    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

class GTTParams:
    def __init__(self, obj):
        """ Class defining GTT structure\n
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
        self.keys = ["tradingsymbol",
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
            
        self.exchange = "NSE"
        self.producttype = "MARGIN"
        self.transactiontype = "BUY"
        for k, v in obj.items():
            if k in self.keys:
                self.__setattr__(k, v)
    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

class HistoryParams:
    def __init__(self, obj):
        """ Class defining paramteres for getting historic data\n
            Accepts Structure:\n
            {
                "exchange": "NSE",
                "symboltoken": "3045",
                "interval": "ONE_MINUTE",
                "fromdate": "2021-02-08 09:00",
                "todate": "2021-02-08 09:16"\n
            }
        """
        self.keys = [
            "exchange",
            "symboltoken",
            "interval",
            "fromdate",
            "todate"
        ]
            
        self.exchange = "NSE"
        self.interval = "ONE_MINUTE"
        for k, v in obj.items():
            if k in self.keys:
                self.__setattr__(k, v)
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
        dict = {k: v for k,v in zip(self.keys, obj)}
        for k, v in dict.items():
            if k in self.keys:
                self.__setattr__(k, v)
        
        if self.close >= self.open:
            self.color = "green"
        else:
            self.color = "red"
        
        self.size = abs(self.high - self.low)
        self.body = abs(self.close - self.open)

        self.keys.insert("color")
        self.keys.insert("size")
        self.keys.insert("body")

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

        dict = {k: v for k,v in zip(self.keys, obj)}
        for k, v in dict.items():
            if k in self.keys:
                self.__setattr__(k, v)
        
        connection, data = get_connection()
        self.current = get_current_value(connection, self)
        self.pl = self.current - self.netvalue
        self.netchange = self.pl / self.avgnetprice
        self.position = "BUY" if self.totalbuyvalue != 0 else "SELL"

        self.keys.insert("current")
        self.keys.insert("pl")
        self.keys.insert("netchange")
        self.keys.insert("position")

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

        dict = {k: v for k,v in zip(self.keys, obj)}
        for k, v in dict.items():
            if k in self.keys:
                self.__setattr__(k, v)

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.keys}

    def get_summary(self):
        return f'''Symbol: {self.tradingsymbol}
            Quantity: {self.quantity}\n
            P&L: {self.profitandloss}'''
