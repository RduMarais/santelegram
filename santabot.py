#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to make a Telegram advent calendar.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
"""
import configparser
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

try:
	import json
except ImportError:
	import simplejson as json


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,filename="santabot.log")

logger = logging.getLogger(__name__) # i.e le logger va afficher de quel fichier du package
DEBUG = True # if True, accepte des demandes à des moments random
MONTH = 12
config_file_name = "config.ini" # super original hein


## READ config file and set Auth variables
def init_api():
	config=configparser.ConfigParser()
	config.read(config_file_name)
	API_KEY = config['API']['TOKEN']
	CONVERSATIONS =  json.loads(config['API']['conversations'])
	START_TIME = int(config['CONFIG']['STARTTIME'])
	STOP_TIME = int(config['CONFIG']['STOPTIME'])
	return(API_KEY,CONVERSATIONS, START_TIME, STOP_TIME)

## SET GLOBAL VARIABLES
(API_KEY,CONVS, START_TIME, STOP_TIME) = init_api()

########### FUNCTIONS ######## 

"""Ouvre le fichier de config et lit le tip dans la catégorie qui va bien
   chat_id doit être un string
"""
def read_config(section,key):
	config=configparser.ConfigParser()
	config.read(config_file_name)
	config_value = config[section][key]
	# logger.info("read "+str(key)+" : "+config_value)
	return(config_value)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
	"""Send a message when the command /start is issued."""
	start_text = read_config("CONFIG","starttext")
	update.message.reply_text(start_text)

# TODO : proposer des tips
def tip(update, context):
	"""Send a random msg when the command /tip is issued."""
	tips = json.loads(read_config("CONFIG","tips"))
	for tip in tips:
		update.message.reply_text(tip)

"""TODO : m'envoyer un msg quand on fait /tip"""
def notify(text):
	logger.error("TODO")

"""retourne le jour si on est en décembre (ou au mois MONTH) entre 9 et 11h"""
def is_time_ok(date):
	if(date.month == MONTH or DEBUG):
		if(date.hour >= START_TIME and date.hour <= STOP_TIME or DEBUG):
			return date.day
		else:
			return False
	else:
		return False

def open(update,context):
	"""Sends a tip if and only if the right sender issues /open"""
	# logger.info(update)
	if(str(update.message.chat.id) in CONVS):
		chat = CONVS[str(update.message.chat.id)]
		# logger.info("chat : "+chat)
		day=is_time_ok(update.message.date)
		# logger.info("day : "+str(day))
		if(day):
			authorized_users = json.loads(read_config(chat,"users"))[day-1]
			logger.info("users : "+str(authorized_users)+" , open request from : "+str(update.message.from_user.id)+":"+update.message.from_user.first_name)
			logger.info(update.message.from_user.username)
			if(update.message.from_user.id in authorized_users):
				update.message.reply_text(read_config("CONFIG","opentext")+" "+str(update.message.from_user.first_name))
				array = json.loads(read_config(chat,"messages")) # -1 vu que l'array, contrairement au mois, commence à zéro
				tip = array[day-1]
				logger.info(tip)
				for line in tip:
					update.message.reply_text(line)
			else:
				update.message.reply_text("Désolé, ce n'est pas à toi d'ouvrir le calendrier")

def help(update, context):
	"""Send a message when the command /help is issued."""
	helplines = json.loads(read_config("CONFIG","help"))
	for line in helplines:
		update.message.reply_text(line)


def erreur(update, context):
	"""Echo the user message."""
	# update.message.reply_text(read_config("CONFIG",'error'))
	logger.info("erreur : "+update)


def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater(API_KEY, use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	#dp.add_handler(CommandHandler("tip", tip))
	dp.add_handler(CommandHandler("open", open))

	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler(Filters.text, erreur))

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
