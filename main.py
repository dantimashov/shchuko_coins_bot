from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, view, dao, config
from coin import CoinHandler

token = config.env['TOKEN_TELEGRAM']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text(dao.get_instructions())


def get_list_coins(bot, update):
    coins = CoinHandler()
    update.message.reply_text(view.coins_to_string(coins.listCoins))


def get_categories(bot, update):
    coins = CoinHandler()
    update.message.reply_text(view.categories_to_string(coins.categories))


def handler_plain_text(bot, update):
    update.message.reply_text("Пожалуйста, воспользуйтесь командами из списка команд.\n"
                              "Чтобы получить список команд наберите /help")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("categories", get_categories))
    dp.add_handler(CommandHandler("list_coins", get_list_coins))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, handler_plain_text))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()