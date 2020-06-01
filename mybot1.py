from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram.ext import Updater
from logging import Logger
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)





def start(update,context):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    author=update.message.from_user.first_name
    msg="hello!{}".format(author)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    
def echo_txt(update,context):
    reply= update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
def error(update,context) :
     Logger.logger.error("error '%s' due to '%s",context,context.error) 
    

TOKEN = '1279310117:AAGYBsOMxsr05upeTHFHm5f6bPx8bCGNkOA'
updater = Updater(token=TOKEN,use_context=True)

dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(MessageHandler(Filters.text, echo_txt))
dispatcher.add_error_handler(error)
updater.start_polling()
updater.idle()
