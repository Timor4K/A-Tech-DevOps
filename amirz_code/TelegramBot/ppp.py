from telegram.ext import Updater, CommandHandler

with open('token.txt','r') as f:
    TOKEN = f.read()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

def main():
    # Create an Updater object with your bot token
    updater = Updater(TOKEN, update_queue=True)

    # Get the Dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
