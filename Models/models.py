class OrderParams:
    def __init__(self, obj):
        """ Class defining Order structure\n
        Accepts Structure:\n
        orderparams = {
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

class GTTParams:
    def __init__(self, obj):
        """ Class defining GTT structure\n
            Accepts Structure:\n
            gttCreateParams={
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

class HistoryParams:
    def __init__(self, obj):
        """ Class defining paramteres for getting historic data\n
            Accepts Structure:\n
            historicParam={
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