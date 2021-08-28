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
