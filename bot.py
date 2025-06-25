import os
import django
from telegram.ext import Updater, CommandHandler
from decouple import config

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')
django.setup()

from api.models import TelegramUser

# /start command handler
def start(update, context):
    user = update.message.from_user
    username = user.username

    if not username:
        update.message.reply_text("❗ Error: Your Telegram account does not have a username set. Please set one to continue.")
        return

    TelegramUser.objects.get_or_create(username=username)
    update.message.reply_text(f"Hi {username}, you've been registered!")

# Bot main function
def main():
    print("Starting Telegram bot...")  # Console log for clarity

    updater = Updater(token=config('TELEGRAM_BOT_TOKEN'), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("Bot is now running. Send /start in Telegram.")  # Important for demo
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()