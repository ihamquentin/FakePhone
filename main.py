import constants as keys 
from telegram.ext import *
from FakePhone import Fake_Phone
import logging
import os

print('Bot Started...')


PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start_command(update, context):
    update.message.reply_text('this bot is designed to provide numbers for verifications, \nHow To Use:\n /get_number provides you with 5 numbers to pick from \n/get_message provides you with the last 2 message received by that number.\n\n\n THANK YOU')

def help_command(update, context):
    update.message.reply_text('How To Use:\n /get_number provides you with 5 numbers to pick from \n/get_message provides you with the last 2 message received by your selected number.\n\n\n THANK YOU')

def get_number(update, context):
    calla = Fake_Phone()
    response = calla.free_sms_num() #['number']
    for i,j in zip(response,range(1,6)):
        update.message.reply_text(f"{j}. {i['number']} \nLink: {i['receive_link']}")


def get_message(update, context, number=0):
    calla = Fake_Phone()
    g_number = calla.free_sms_num()
    response = calla.free_sms_child(g_number, number)
    for i in response:
        update.message.reply_text(f"Number: {g_number[number]['number']} \nTime received: {i['duration']} \nMessage: {i['body']}")
        #update.message.reply_text(i)


def handle_message(update, context):
    text = str(update.message.text)
    calla = Fake_Phone()
    g_number = calla.free_sms_num()
    if text.isnumeric():
        if int(text) in [1,2,3,4,5]:
            response = calla.free_sms_child(g_number, int(text)-1)
            for i in response:
                update.message.reply_text(f"Number: {g_number[int(text)-1]['number']} \nTime received: {i['duration']} \nMessage: {i['body']}")
        else:
            update.message.reply_text('INVALID SELECTION!!!')
    else:
        update.message.reply_text('Only Numbers can be picked')
    
def error(update, context):
    print(f'Update {update} caused error {context.error}')

def donate(update, context):
    a = "With Varity+ you'd be getting Free Burna numbers to use for any form of verifications, more country numbers are being added to the platform regularly.\n"
    b= "We accept donations to keep our servers and scrappers running. feel free to support us with cryptocurrency."
    c= "\n\nBitcoin:\n1BLyRA9faucg1c6aoegtBa4WZ84dswTF46\n\nEtherium:\n0xae068687d25b59c408a90aad76d20bdd312261df\n\nBNB(BEP20):\n0xae068687d25b59c408a90aad76d20bdd312261df"
    update.message.reply_text(a+b+c)



def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('get_number', get_number))
    dp.add_handler(CommandHandler('get_message', get_message))
    dp.add_handler(CommandHandler('donate', donate))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",port=int(PORT), url_path=keys.API_KEY)
    updater.bot.setWebhook('https://floating-cove-45279.herokuapp.com/' + keys.API_KEY)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()