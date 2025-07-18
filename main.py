import logging
import os
import random

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def roll_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        number = random.randint(1, 6)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You rolled a {number}!")
    except Exception as e:
        logging.error(f"Error handling /roll command: {e}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred.")


if __name__ == '__main__':
    try:
        TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
    except KeyError:
        logging.critical("TELEGRAM_BOT_TOKEN environment variable not set.")
        exit(1)

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    roll_handler = CommandHandler('roll', roll_command)
    application.add_handler(roll_handler)

    # Add error handler
    application.add_error_handler(lambda update, context: logging.error(f"Unhandled error: {context.error}"))

    application.run_polling()

