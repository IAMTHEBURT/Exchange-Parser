#import telegram
#from telegram.ext import CommandHandler, Updater
#from telegram.ext import MessageHandler, Filters, ConversationHandler
#from telegram.ext import MessageHandler, filters, ConversationHandler

import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


# async def send_info(msg):
# 	await bot.send_message(chat_id=str(config['TELEGRAM']['id_channel']), text=msg)


def send_info(msg):
	
    apiToken = config['TELEGRAM']['bot_key']
    chatID = str(config['TELEGRAM']['id_channel'])
    
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': msg})
        #print(response.text)
    except Exception as e:
        print(e)

