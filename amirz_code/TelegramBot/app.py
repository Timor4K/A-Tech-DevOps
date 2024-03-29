from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

with open('token.txt','r') as f:
    TOKEN: Final = f.read()

BOT_USERNAME: Final = '#@amirzaidBot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Heelo I am a BOT ...")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Help ...")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom ...")

# Logic to responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        # Chat AI can be used
        return 'Hi there!'

    return 'Hmmmmmmm Noop'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if it is private or group chat
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f' User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        # private chat
        response: str = handle_response(text)

    print('Bot:', response)
    await  update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting the Bot...')
    app = Application.builder().token(TOKEN).build()
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('start', help_command))
    app.add_handler(CommandHandler('start', custom_command))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # Errors
    app.add_error_handler(error)
    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)




