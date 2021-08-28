# from Models.models import GTTParams, HistoryParams, OrderParams
# from Utils.SmartAPI import create_gtt, get_connection, get_holding, get_hosition, get_user_profile, get_gtt_list, get_history, logout_session, place_order
# #import smartapi.smartExceptions(for smartExceptions)

# def __init__():
#     connection, data = get_connection()

#     # profile = getUserProfile(connection, data)

#     # holdings = getHolding(connection)

#     # positions = getPosition(connection)

#     # order_id = place_order(connection, OrderParams({
#     #     "variety": "NORMAL",
#     #     "tradingsymbol": "SBIN-EQ",
#     #     "symboltoken": "3045",
#     #     "transactiontype": "BUY",
#     #     "exchange": "NSE",
#     #     "ordertype": "LIMIT",
#     #     "producttype": "INTRADAY",
#     #     "duration": "DAY",
#     #     "price": "19500",
#     #     "squareoff": "0",
#     #     "stoploss": "0",
#     #     "quantity": "1"
#     # }))

#     # gtt_id = create_gtt(connection, GTTParams({
#     #     "tradingsymbol" : "SBIN-EQ",
#     #     "symboltoken" : "3045",
#     #     "exchange" : "NSE",
#     #     "producttype" : "MARGIN",
#     #     "transactiontype" : "BUY",
#     #     "price" : 100000,
#     #     "qty" : 10,
#     #     "disclosedqty": 10,
#     #     "triggerprice" : 200000,
#     #     "timeperiod" : 365
#     # }))

#     # gtt_list = get_gtt_list(connection)

#     history = get_history(connection, HistoryParams({
#         "exchange": "NSE",
#         "symboltoken": "INE467B01029",
#         "interval": "ONE_DAY",
#         "fromdate": "2021-08-17 09:00",
#         "todate": "2021-02-22 09:16"
#     }))
#     print(history)

#     logout = logout_session(connection)
