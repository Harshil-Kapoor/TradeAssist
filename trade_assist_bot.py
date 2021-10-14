"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
import os
from telegram import Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, MessageHandler, Filters
from Models.models import HistoryParams, MovementAnalysisParams, MovementAnalysisResponse
from Utils.SmartAPI import get_connection, get_history, get_holding, get_position
from Utils.Utils import analyze_movement, format_holdings, format_positions, get_candles, get_formatted_date, get_interval

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
TOKEN = os.environ["BOT_TOKEN"]
PORT = int(os.environ.get('PORT', '8443'))


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def positions(update: Update, context: CallbackContext) -> None:
    """Get the user positions."""
    connection, data = get_connection()
    if connection is not None:
        update.message.reply_text("Connection established!")
    else:
        return

    userPositions = get_position(connection, logger)
    if userPositions is not None:
        if userPositions["data"] is not None:
            update.message.reply_text("Positions have been retrieved!")
        else:
            update.message.reply_text("You have no open positions...")
            return

    lines = [position.get_summary() for position in format_positions(userPositions["data"])]
    for position in lines:
        update.message.reply_text(position)


def holdings(update: Update, context: CallbackContext) -> None:
    """Get the user holdings."""
    connection, data = get_connection()
    if connection is not None:
        update.message.reply_text("Connection established!")
    else:
        return

    userHoldings = get_holding(connection, logger)
    if userHoldings is not None:
        if userHoldings["data"] is not None:
            update.message.reply_text("Holdings have been retrieved!")
        else:
            update.message.reply_text("You have no holdings...")
            return

    lines = [holding.get_summary() for holding in format_holdings(userHoldings["data"])]
    for holding in lines:
        update.message.reply_text(holding)


def history(update: Update, context: CallbackContext) -> None:
    """Get historical data."""
    historicParams = HistoryParams({
        "exchange": context.args[0] or "NSE",
        "symboltoken": context.args[1],
        "interval": get_interval(context.args[2]),
        "fromdate": get_formatted_date(context.args[3]),
        "todate": get_formatted_date(context.args[4])
    })

    connection, data = get_connection()
    if connection is not None:
        update.message.reply_text("Connection established!")
    else:
        return

    candles = get_history(connection, historicParams)
    if candles is not None:
        if candles["data"] is not None:
            update.message.reply_text("History has been retrieved!")
        else:
            update.message.reply_text("Could not get History...")
            return

    lines = [candle.get_summary() for candle in get_candles(candles["data"])]
    for candle in lines:
        update.message.reply_text(candle)


def analyzeMovement(update: Update, context: CallbackContext) -> None:
    """Perform Monement analysis."""
    params = MovementAnalysisParams(
        symbolToken=context.args[0],
        interval=context.args[1],
        delta=context.args[2],
        body_ratio_threshold=context.args[3],
        exchange=context.args[4])

    connection, data = get_connection()
    if connection is not None:
        update.message.reply_text("Connection established!")
    else:
        return

    result: MovementAnalysisResponse = analyze_movement(connection, params)
    if result is not None:
        update.message.reply_text("Analysis preformed:")

    update.message.reply_text(result.get_summary())


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query.split(' ')

    try:
        connection, data = get_connection()
    except Exception:
        update.inline_query.answer("Could not connect to Trading API.", is_personal=True)

    update.inline_query.answer("Invalid Command", is_personal=True)


    # results = [
    #     InlineQueryResultArticle(
    #         id=str(uuid4()),
    #         title="Caps",
    #         input_message_content=InputTextMessageContent(query.upper()),
    #     ),
    #     InlineQueryResultArticle(
    #         id=str(uuid4()),
    #         title="Bold",
    #         input_message_content=InputTextMessageContent(
    #             f"*{escape_markdown(query)}*", parse_mode=ParseMode.MARKDOWN
    #         ),
    #     ),
    #     InlineQueryResultArticle(
    #         id=str(uuid4()),
    #         title="Italic",
    #         input_message_content=InputTextMessageContent(
    #             f"_{escape_markdown(query)}_", parse_mode=ParseMode.MARKDOWN
    #         ),
    #     ),
    # ]

    # update.inline_query.answer(results)


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("positions", positions))
    dispatcher.add_handler(CommandHandler("holdings", holdings))
    dispatcher.add_handler(CommandHandler("history", history))
    dispatcher.add_handler(CommandHandler("analyzeMovement", analyzeMovement))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # on inline command - perform the task requested
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    # updater.start_polling

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url='https://trade-assist.herokuapp.com/' + TOKEN)

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
