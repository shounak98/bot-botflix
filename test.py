import pandas as pd

import telebot as tb
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, callbackcontext, updater


suggest = pd.read_csv('netflix.csv')
random_row  = suggest.sample()
index = random_row.show_id.values[0]
title = random_row['title'].values[0]
description = random_row['description'].values[0]
#director = random_row['director'].values[0]
cast = random_row['cast'].values[0]
print(type(description))