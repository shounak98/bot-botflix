import pandas as pd

## import telebot as tb
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, callbackcontext, updater





def suggest(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please Wait')
    suggest = pd.read_csv('netflix.csv')
    random_row  = suggest.sample()
    index = str(random_row.show_id.values[0])
    title = str(random_row['title'].values[0])
    description = str(random_row['description'].values[0])
    director = str(random_row['director'].values[0])
    cast = str(random_row['cast'].values[0])

    update.message.reply_text('<i>#' + index + '</i>\n<strong>Title: ' + title + '</strong> \nCast: [' + cast + '] \nDirector: ' + director + '\n\nDescription: '+description, parse_mode='HTML')







updater = Updater('2037547906:AAGXApXjW3gyBcw3pCMjhe2sV7aXmxF4dc8')
updater.dispatcher.add_handler(CommandHandler('suggest', suggest))   
updater.start_polling()
updater.idle()
