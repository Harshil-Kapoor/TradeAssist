from typing import Tuple
from smartapi import SmartConnect
from Models.models import HistoryParams, OrderParams, GTTParams

def get_connection() -> Tuple[SmartConnect, bytes]:
    #create object of call
    connection=SmartConnect(api_key="ILnSIQp8")
    # ,
                    #optional
                    #access_token = "your access token",
                    #refresh_token = "your refresh_token")

    #login api call
    data = connection.generateSession("","")

    #fetch the feedtoken
    # feedToken=connection.getfeedToken()

    return connection, data

def get_user_profile(connection: SmartConnect, data: bytes):
    """ Fetch User Profile\n
        Keyword Arguments:\n
        connection -- SmartConnect object
    """
    try:
        refreshToken= data['data']['refreshToken']
        return connection.getProfile(refreshToken)
    except Exception as e:
        print(f"Could not get user profile: {e}")

def get_holding(connection: SmartConnect):
    """ Get Holding Information\n
        Keyword Arguments:\n
        connection -- SmartConnect object
    """
    try:
        return connection.holding()
    except Exception as e:
        print(f"Could not get holdings: {e}")

def get_position(connection: SmartConnect):
    """ Fetch Position Information\n
        Keyword Arguments:\n
        connection -- SmartConnect object
    """
    try:
        return connection.position()
    except Exception as e:
        print(f"Could not get positions: {e}")

def place_order(connection: SmartConnect, order: OrderParams) -> int:
    """ Place order with given paramters\n
        Keyword Arguments:\n
        connection -- SmartConnect object\n
        order -- OrderParams object
    """
    try:
        orderId=connection.placeOrder(order)
        print("The order id is: {}".format(orderId))
        return orderId
    except Exception as e:
        print(f"Order placement failed: {e}")

def create_gtt(connection: SmartConnect, gtt: GTTParams) -> int:
    """ Create a GTT rulw with given paramters]n
        Keyword Arguments:\n
        connection -- SmartConnect object\n
        gtt -- GTTParams object
    """
    try:
        ruleid=connection.gttCreateRule(gtt)
        print("The GTT rule id is: {}".format(ruleid))
        return ruleid
    except Exception as e:
        print(f"GTT Rule creation failed: {e}")

def get_gtt_list(connection: SmartConnect):
    """ Get the GTT rule list\n
        Keyword Arguments:\n
        connection -- SmartConnect object
    """
    try:
        status=["FORALL"] #should be a list
        page=1
        count=10
        return connection.gttLists(status, page, count)
    except Exception as e:
        print(f"GTT Rule List failed: {e}")

def get_history(connection: SmartConnect, history: HistoryParams):
    """ Historic api\n
        Keyword Arguments:\n
        connection -- SmartConnect object\n
        gtt -- HistoricPArams object
    """
    try:
        return connection.getCandleData(history)
    except Exception as e:
        print(f"Historic Api failed: {e}")

def logout_session(connection: SmartConnect):
    """ Logout and close the connection]n
        Keyword Arguments:\n
        connection -- SmartConnect object
    """
    try:
        logout=connection.terminateSession('Your Client Id')
        print("Logout Successfull")
        return logout
    except Exception as e:
        print(f"Logout failed: {e}")