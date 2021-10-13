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
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from Utils.SmartAPI import get_connection, get_history, get_holding, get_position
from Utils.Utils import format_holdings, format_positions, get_candles

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Create the Updater and pass it your bot's token.
updater = Updater(os.environ["BOT_TOKEN"])


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query.split(' ')

    try:
        connection, data = get_connection()
    except Exception:
        update.inline_query.answer("Could not connect to Trading API.", is_personal=True)

    if query[0] == "positions":
        positions = format_positions(get_position(connection))
        lines = [position.get_summary() for position in positions]
        for position in lines:
            update.inline_query.answer(position, is_personal=True)
    elif query[0] == "holdings":
        holdings = format_holdings(get_holding(connection))
        lines = [holding.get_summary() for holding in holdings]
        for holding in lines:
            update.inline_query.answer(holding, is_personal=True)
    elif query[0] == "history":
        candles = get_candles(get_history(connection, query[1:].__dict__)["data"])
        lines = [candle.get_summary() for candle in candles]
        for holding in lines:
            update.inline_query.answer(holding, is_personal=True)
    else:
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
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
