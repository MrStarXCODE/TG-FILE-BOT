from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re
import logging
import random
import string   
from dotenv import load_dotenv
import os
# -------------------------------------------------------------------------------------------------
# Title: Basic Telegram Storage Bot
# Author: $Kek (MrStarXCODE)
# Date (IST): 22-07-2023
# -------------------------------------------------------------------------------------------------
# This program is used to create a Telegram bot that stores files in a private channel and retrieves them on request.
# The bot accepts files of various types from users, stores them in a specified Telegram channel, and generates a unique identifier
# for each file. Users can retrieve stored files by sending the bot the unique identifier associated with the file.
# -------------------------------------------------------------------------------------------------
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = "YOUR_CHANNEL_ID"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please send me a file and I will store it for you.')
    logger.info(f"Bot started by user {update.effective_user['username']}")

def handle_message(update: Update, context: CallbackContext) -> None:
    logger.info(f"Received message from user {update.effective_user['username']}")
    if update.message.document or update.message.photo or update.message.audio or update.message.video or update.message.voice:
        logger.info(f"Received a file from user {update.effective_user['username']}")
        msg = context.bot.forward_message(chat_id=CHANNEL_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

        # Generate a random string of length 5
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        file_id = f"{msg.message_id}-{random_str}"

        # Present the file ID in monospace format
        update.message.reply_text(f'Your file has been stored. You can access it using the following code: `FILE_ID:{file_id}`', parse_mode='Markdown')
    elif update.message.text:
        match = re.match(r'FILE_ID:(\d+)-(\w+)', update.message.text)
        if match:
            logger.info(f"Received file request from user {update.effective_user['username']}")
            # We only need the message ID to forward the message, so we discard the random string
            msg = context.bot.forward_message(chat_id=update.message.chat_id, from_chat_id=CHANNEL_ID, message_id=int(match.group(1)))
        else:
            update.message.reply_text('Please send a valid file request code.')

def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, handle_message))  # Handle all types of updates

    dp.add_error_handler(error_handler)

    updater.start_polling()

    logger.info("Bot started and polling...")

    updater.idle()

if __name__ == '__main__':
    main()