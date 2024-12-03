# from typing import Final
# from telegram import Update
# import os 
# from dotenv import load_dotenv
# dotenv_path = "./.env" 
# load_dotenv(dotenv_path)
# BOT_TOKEN = os.environ.get('BOT_TOKEN')
# from telegram.ext import Application, CommandHandler,ContextTypes, MessageHandler, filters
# TOKEN: Final = BOT_TOKEN
# BOT_USERNAME:Final= 'qazxsw741_bot'
# # COMMANDS
# async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello! Thanks for chatting with me. I am sampath Kumar")
# async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("I am sampath Kumar, Please start typing something")
# async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("this is custom command")
# # 
# # responses
# def handle_response(text:str) -> str:
#     processed: str = text.lower()
#     if ('hello' in processed):
#         return "hey there"
#     if ('how are you' in processed):
#         return "i am happy"
#     if ("i love you" in processed):
#         return "I love you back"
#     return "i don`t understand what you wrote"
# # HANDLE MESSAGES
# async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
#     message_type:str=update.message.chat.type
#     test: str=update.message.text
#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
#     if message_type == 'group':
#         if BOT_USERNAME in text:
#             new_text:str = text.replace(BOT_USERNAME,'').strip()
#             response:str=handle_response(new_text)
#         return
#     else:
#         response:str=handle_response(text)
#     print("Bot :", response)
#     await update.message.reply_text(response)
# async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
#     print(f"Update {update} caused error {context.error}")
# if __name__ =="main":
#     print("starting bot")
#     app=Application.builder().token(BOT_TOKEN).build()
#     # COMMADS
#     app.add_handler(CommandHandler('start',start_command))
#     app.add_handler(CommandHandler('help',help_command))
#     app.add_handler(CommandHandler('custom',custom_command))
#     # MESAGES
#     app.app_handler(MessageHandler(filters.Text,handle_message))
#     # ERROR
#     app.add_error_handler(error)
#     # POLLING
#     print("polling")
#     app.run_polling(poll_interval=5)
# # 
# from typing import Final
# from telegram import Update
# import os 
# from dotenv import load_dotenv
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# # Load environment variables
# dotenv_path = "./.env" 
# load_dotenv(dotenv_path)
# BOT_TOKEN = os.environ.get('BOT_TOKEN')

# # Define constants
# TOKEN: Final = BOT_TOKEN
# BOT_USERNAME: Final = 'qazxsw741_bot'

# # COMMAND HANDLERS
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello! Thanks for chatting with me. I am Sampath Kumar.")

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("I am Sampath Kumar. Please start typing something.")

# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("This is a custom command.")

# # Response function
# def handle_response(text: str) -> str:
#     processed: str = text.lower()
#     if 'hello' in processed:
#         return "Hey there!"
#     if 'how are you' in processed:
#         return "I am happy!"
#     if "i love you" in processed:
#         return "I love you back!"
#     return "I don’t understand what you wrote."

# # MESSAGE HANDLER
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text  # Fixed variable name from "test" to "text"

#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     if message_type == 'group':
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#             await update.message.reply_text(response)  # Added to ensure group responses are sent
#         return
#     else:
#         response: str = handle_response(text)
#     print("Bot:", response)
#     await update.message.reply_text(response)

# # ERROR HANDLER
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f"Update {update} caused error {context.error}")

# # MAIN FUNCTION
# if __name__ == "__main__":  # Fixed condition from "main" to "__main__"
#     print("Starting bot...")
#     app = Application.builder().token(BOT_TOKEN).build()

#     # COMMAND HANDLERS
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))

#     # MESSAGE HANDLER
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Fixed filter syntax

#     # ERROR HANDLER
#     app.add_error_handler(error)

#     # POLLING
#     print("Polling...")
#     app.run_polling(poll_interval=5)
# 
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_command(update, context):
    await update.message.reply_text("Hello! I'm your sampath kumar`s Bot!")
async def help_command(update, context):
    await update.message.reply_text("what help you need")
async def custom_command(update, context):
    await update.message.reply_text("hello this is custom command")

if __name__ == "__main__":
    # Initialize application with retry and increased timeout
    app = Application.builder().token(BOT_TOKEN).connect_timeout(60).build()

    # Add command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Start polling
    print("Bot is polling...")
    app.run_polling(poll_interval=5)
